# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import os
import re
import time
import uuid
from os import path

import pymysql
import wget
from DBUtils.PooledDB import PooledDB
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

logger = logging.getLogger(__name__)


def corp_business_model_trans2_enum(corp_business_model):
    result = []
    if '合作' in corp_business_model or '加盟' in corp_business_model:
        result.append('加盟合作')

    if '特许' in corp_business_model or '直营' in corp_business_model:
        result.append('单店特许')

    if '连锁' in corp_business_model:
        result.append('自由连锁')

    if '代理' in corp_business_model or '经销' in corp_business_model:
        result.append("区域代理")

    if '开发' in corp_business_model:
        result.append('区域开发')

        result.append('加盟合作')

    return ','.join(result)


def suitable_for_the_crowd_trans2_enum(suitable_for_the_crowd):
    result = []
    if not suitable_for_the_crowd:
        result.append("自主创业")
        result.append("白手起家")
        result.append('在岗创业')
        result.append('白领创业')
        result.append("青年创业")
        result.append('大学生创业')
        return ','.join(result)

    if '自由' in suitable_for_the_crowd:
        result.append('自主创业')
        result.append('白手起家')
    if '在岗' in suitable_for_the_crowd:
        result.append('在岗创业')
        result.append('白领创业')
    if '毕业生' in suitable_for_the_crowd:
        result.append("青年创业")
        result.append('大学生创业')

    if '其他' in suitable_for_the_crowd:
        result.append("自主创业")
    if not result:
        result.append("自主创业")
        result.append("在岗创业")
        result.append("白领创业")
    return ','.join(result)


db_name = settings.get("DB_NAME")
host = settings.get("DB_HOST")
port = settings.get("DB_PORT")
user = settings.get("DB_USER")
password = settings.get("DB_PASSWORD")
pool = PooledDB(pymysql, 10, 60, database=db_name, host=host, port=port, user=user,
                password=password, charset="utf8")


class QjSpiderPipeline(object):
    # spider 开启时调用
    def __init__(self):

        self.dr = re.compile(r'<[^>]+>', re.S)

        self._pool = pool

        self._insert_cyjm_archives_sql = """INSERT INTO `cyjm_archives` (id,`typeid`,`typeid2`,`voteid`,`sortrank`,
        `channel`,`arcrank`,ismake,`title`,`writer`,`source`,`pubdate`,`senddate`,`keywords`,`description`)
        VALUES(%s,%s,'0',0,666666666,5 ,-1,-1,%s,'spider','zhms-network',%s,%s,%s,%s)"""

        self._insert_cyjm_project_sql = """INSERT INTO `cyjm_project` (`aid`,`typeid`,`pro_logo`,`pro_brand`,
        `pro_tzmoney`,`pro_hangye`,pro_mianji,`pro_dmnum`,`pro_clsj`,`pro_ppfyd`,`pro_jyms`,`pro_jmfy`,pro_jmqy,`pro_comname`,
        `pro_comaddress`,`pro_zycp`,`pro_tzrq`,`pro_jmys`,`pro_jmzc`,`pro_jmtj`,`pro_jmlc`,`pro_jmcost`,
        pro_seotitle,body)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        self._insert_cyjm_arctiny = """INSERT INTO `cyjm_arctiny` (`typeid`, `typeid2`, `arcrank`, `channel`, 
        `senddate`, `sortrank`, `mid`) VALUES (%s, '0', -1, 5, %s, 666666666, 2)"""

    def process_item(self, item, spider):
        try:
            conn = self._pool.connection()
            with conn.cursor() as cur:
                self.insert_cyjm_arctiny(item, cur)
                self.insert_cyjm_archives(item, cur)
                self.insert_cyjm_project(item, cur)
                conn.commit()
        except Exception as e:
            logger.error("data write db error! data: " + item)
            logger.error(repr(e))
            raise e
        finally:
            conn.close()
        return item

    def insert_cyjm_project(self, item, cur):
        values = (item['id'],
                  item['project_type'],
                  item['pro_logo'],
                  item['title'],
                  item['investment_amount'],
                  item['industry_code'],
                  item['store_area'],
                  item['total_number_of_store'],
                  item['corp_create_time'],
                  item['brand_source'],
                  corp_business_model_trans2_enum(item['corp_business_model']),
                  item['investment_amount'],
                  item['jmqy'],
                  item['corp_name'],
                  item['corp_address'],
                  item['operating_products'],
                  suitable_for_the_crowd_trans2_enum(item['suitable_for_the_crowd']),
                  item['project_benefits'],
                  item['project_support'],
                  item['project_condition'],
                  item['project_flow'],
                  item['project_feiyong'],
                  "",
                  item['product_introduce']
                  )
        cur.execute(self._insert_cyjm_project_sql, values)

    def insert_cyjm_archives(self, item, cur):

        values = (item['id'],
                  item['project_type'],
                  item['title'],
                  int(time.time()),
                  int(time.time()),
                  item['project_keyword'] + "," + item['project_keyword']+"加盟",
                  self.dr.sub('', item['product_introduce']).strip()[0:250]
                  )
        cur.execute(self._insert_cyjm_archives_sql, values)

    def insert_cyjm_arctiny(self, item, cur):
        values = (item['project_type'], int(time.time()))
        cur.execute(self._insert_cyjm_arctiny, values)
        cur.execute("SELECT LAST_INSERT_ID()")
        results = cur.fetchall()
        item['id'] = results[0][0]

    # spider 关闭时调用
    def close_spider(self, spider):
        if self._pool is not None:
            self._pool.close()


class CityTransferPipeline(object):
    """
    城市转换
    """

    def __init__(self):
        city_code_source_dict = settings.get('CITY_CODE')

        self.city_code = {}

        for key in city_code_source_dict:
            val_dict = city_code_source_dict[key]
            title = val_dict['title']

            self.city_code[title] = key

    def process_item(self, item, spider):

        if item['brand_source']:

            if item['brand_source'] in self.city_code:
                item['brand_source'] = self.city_code[item['brand_source']]

        return item


class TagTransferPipeline(object):
    """
    标签
    """

    def __init__(self):
        self._pool = pool

    def _query_tag_index(self, tag, item):
        try:
            conn = self._pool.connection()
            with conn.cursor() as cur:
                cur.execute("select id from cyjm_tagindex where tag = %s", (tag))
                result = cur.fetchone()
                if result:
                    return result[0]
                time_now = int(time.time())
                cur.execute("insert into cyjm_tagindex(tag,typeid,weekup,monthup,addtime) values(%s,%s,%s,%s,%s)",
                            (tag, item['project_type'], time_now, time_now, time_now))
                cur.execute("SELECT LAST_INSERT_ID()")
                result = cur.fetchone()
                return result[0]
            conn.commit()
        except Exception as e:
            logger.error(repr(e))
            raise e
        finally:
            conn.close()

    def _insert_tag(self, item):

        if "加盟" not in item['primary_industry']:
            item['primary_industry'] = item['primary_industry'] + "加盟"

        tid1 = self._query_tag_index(item['primary_industry'], item)

        tid2 = self._query_tag_index(item['tag'], item)

        tag_value_list = ((tid1, item['id'], item['project_type'], item['primary_industry']),
                          (tid2, item['id'], item['project_type'], item['tag']))
        try:
            conn = self._pool.connection()
            with conn.cursor() as cur:
                cur.executemany("insert into cyjm_taglist(tid,aid,typeid,tag) values (%s,%s,%s,%s)", tag_value_list)
            conn.commit()

            self._update_count((tid1, tid2), conn)
            conn.commit()

        except Exception as e:
            logger.error(repr(e))
            raise e
        finally:
            conn.close()

    def _update_count(self, tids, conn):
        with conn.cursor() as cur:
            cur.execute('UPDATE cyjm_tagindex SET total = total + 1   WHERE id in (%s)' % ','.join(['%s'] * len(tids)),
                        tids)

    def process_item(self, item, spider):
        self._insert_tag(item)


class IndustryTransferPipeline(object):
    """
    行业置换
    """

    def __init__(self):
        self.industry_dict = settings.get("INDUSTRY")

    def process_item(self, item, spider):

        if item['primary_industry']:
            key = item['primary_industry']

            for index in (5, 4, 3, 2):
                if len(key) >= index:
                    if key[0:index] in self.industry_dict:
                        code = self.industry_dict[key[0:index]]
                        item['industry_code'] = code
                        item['tag'] = key[0:index]
                        return item

            if len(key) >= 3:
                if key[1:3] in self.industry_dict:
                    code = self.industry_dict[key[1:3]]
                    item['industry_code'] = code
                    item['tag'] = key[1:3]
                    return item

            if len(key) >= 4:
                if key[2:4] in self.industry_dict:
                    code = self.industry_dict[key[2:4]]
                    item['industry_code'] = code
                    item['tag'] = key[2:4]
                    return item

            if len(key) >= 5:
                if key[3:5] in self.industry_dict:
                    code = self.industry_dict[key[3:5]]
                    item['industry_code'] = code
                    item['tag'] = key[3:5]
                    return item

            if key[0:1] in self.industry_dict:
                code = self.industry_dict[key[0:1]]
                item['industry_code'] = code
                item['tag'] = key[0:1]
                return item

        item['industry_code'] = 200
        item['tag'] = "未知"
        return item


class InvestmentAmountPipeline(object):
    """
    投资额置换
    """

    def process_item(self, item, spider):

        try:
            investment_amount = item['investment_amount'].strip()

            investment_amount = re.sub("￥|万|以下", "", investment_amount)

            investment_amount = investment_amount.split("-")[0]

            amount = float(investment_amount)

            if amount <= 10:
                item['investment_amount'] = 23

            elif amount <= 20:
                item['investment_amount'] = 24

            elif amount <= 50:
                item['investment_amount'] = 25
            elif amount <= 100:
                item['investment_amount'] = 26

            else:
                item['investment_amount'] = 27

            return item
        except Exception as e:
            logger.error(repr(e))

        return item


class RegularProcessingPipeline(object):
    """
    正则式处理
    """

    def process_item(self, item, spider):

        if item['project_benefits']:
            item['project_benefits'] = re.sub('<div class="joincontit"(.|\n)*</div>\n', "", item['project_benefits'])

        if item['project_support']:
            item['project_support'] = re.sub('<div class="joincontit"(.|\n)*</div>\n', "", item['project_support'])

        if item['project_flow']:
            item['project_flow'] = re.sub('<div class="joincontit"(.|\n)*</div>\n', "", item['project_flow'])

        if item['project_condition']:
            item['project_condition'] = re.sub('<div class="joincontit"(.|\n)*</div>\n', "", item['project_condition'])

        if item['project_feiyong']:
            item['project_feiyong'] = re.sub('<div class="joincontit"(.|\n)*</div>\n', "", item['project_feiyong'])

        # 剔除内连接
        if item['product_introduce']:
            item['product_introduce'] = re.sub("href=\"http.*? target", "1_target", item['product_introduce'])

        if item['project_benefits']:
            item['project_benefits'] = re.sub("href=\"http.*? target", "1_target", item['project_benefits'])

        if item['project_support']:
            item['project_support'] = re.sub("href=\"http.*? target", "1_target", item['project_support'])

        if item['project_flow']:
            item['project_flow'] = re.sub("href=\"http.*? target", "1_target", item['project_flow'])

        if item['project_condition']:
            item['project_condition'] = re.sub("href=\"http.*? target", "1_target", item['project_condition'])

        if item['project_feiyong']:
            item['project_feiyong'] = re.sub("href=\"http.*? target", "1_target", item['project_feiyong'])

        return item


class DownloadPicturePipeline(object):
    """
    下载需要的图片 并替换路径
    """

    def __init__(self):
        self.date = time.strftime('%Y%m%d', time.localtime())

        self.download_path = settings.get("DOWNLOAD_PATH") + "/" + self.date + '/'

        self.prefix_url = "/uploads/allimg/"

        self.domain_name = settings.get('DOMAIN_NAME')

        self.regular = 'img.*src="(.*?)"'

        if not path.exists(self.download_path):
            os.makedirs(self.download_path, exist_ok=True)

    def download_file(self, url):
        if not url:
            return url
        file_name = str(uuid.uuid1()).replace("-", "") + '.' + re.sub("\\?.*", "", url).split('.')[-1]
        file_path = self.download_path + file_name
        logger.info('download picture: ' + file_path)
        wget.download(url, file_path)
        return self.prefix_url + self.date + "/" + file_name

    def process_item(self, item, spider):
        pro_logo_url = self.download_file(item['pro_logo'])

        item['pro_logo'] = '{dede:img text=\'\' width=\'206\' height=\'155\'} ' + pro_logo_url + ' {/dede:img}'

        if item['product_introduce']:
            pic_urls = re.findall(self.regular, item['product_introduce'], re.S)

            for url in pic_urls:
                item['product_introduce'] = item['product_introduce'].replace(url, self.download_file(url))

        if item['project_benefits']:
            pic_urls = re.findall(self.regular, item['project_benefits'], re.S)

            for url in pic_urls:
                item['project_benefits'] = item['project_benefits'].replace(url, self.download_file(url))

        if item['project_support']:
            pic_urls = re.findall(self.regular, item['project_support'], re.S)

            for url in pic_urls:
                item['project_support'] = item['project_support'].replace(url, self.download_file(url))

        if item['project_flow']:
            pic_urls = re.findall(self.regular, item['project_flow'], re.S)

            for url in pic_urls:
                item['project_flow'] = item['project_flow'].replace(url, self.download_file(url))

        if item['project_condition']:
            pic_urls = re.findall(self.regular, item['project_condition'], re.S)

            for url in pic_urls:
                item['project_condition'] = item['project_condition'].replace(url, self.download_file(url))

        if item['project_feiyong']:
            pic_urls = re.findall(self.regular, item['project_feiyong'], re.S)

            for url in pic_urls:
                item['project_feiyong'] = item['project_feiyong'].replace(url, self.download_file(url))

        return item


class ProjectTypeTransfer(object):

    def process_item(self, item, spider):
        item['project_type'] = 73
        return item


class DBDataIsExist(object):
    """
    判断数据库是否存在数据
    """

    def __init__(self):
        db_name = settings.get("DB_NAME")
        host = settings.get("DB_HOST")
        port = settings.get("DB_PORT")
        user = settings.get("DB_USER")
        password = settings.get("DB_PASSWORD")

        self._pool = PooledDB(pymysql, 10, 60, database=db_name, host=host, port=port, user=user,
                              password=password, charset="utf8")

        self._is_exist_sql = """select id from cyjm_archives where title = %s"""

    def process_item(self, item, spider):
        result = None
        try:

            conn = self._pool.connection()
            with conn.cursor() as cur:
                cur.execute(self._is_exist_sql, (item['title']))
                result = cur.fetchall()
            conn.close()
        except Exception as e:
            logger.error("query is exist project db operate error! exception: " + repr(e))
            raise DropItem('query is exist project error! project_name: ' + item['title'])

        if result:
            raise DropItem('query is exist project error! project_name: ' + item['title'])

        return item
