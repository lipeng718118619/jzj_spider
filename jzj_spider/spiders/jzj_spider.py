# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from selenium import webdriver

COOKIE_JAR = 'cookiejar'

options = webdriver.ChromeOptions()
# options.headless = True  # 设置启动无界面化
# options.add_argument('window-size=1920,1080')
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')


class QjSpider(RedisSpider):
    """

    """
    name = 'jzj_spider'

    allowed_domains = ['www.zhms.cn']

    def __init__(self, name=None, **kwargs):
        self.options = options
        self.host = 'http://www.zhms.cn'
        self.driver = webdriver.Chrome(options=self.options)  # 启动时添加定制的选项
        super(QjSpider, self).__init__(name, **kwargs)

    def start_requests(self):
        start_urls = ['http://www.zhms.cn/jm/']

        for url in start_urls:
            yield Request(url=url, meta={COOKIE_JAR: 1}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        # 提取二级界面links
        selectors = response.css(".xm-list-H224.clearfix").css('li')

        for next_url_selector in selectors:
            next_url = self.host + next_url_selector.css('a[href]').attrib['href']

            yield Request(url=next_url, meta={COOKIE_JAR: 1}, callback=self.next_parse, dont_filter=False)

        main_url = self.host + response.css(".next").attrib['href']

        yield Request(url=main_url, meta={COOKIE_JAR: 1}, callback=self.parse, dont_filter=True)

    def next_parse(self, response):
        # 二级解析函数
        # logo url
        # pro_logo = response.css('.roundimgx').css('img')[0].attrib['src']
        pro_logo = response.css('a.pic').css('img')[0].attrib['src']
        # 标题
        title = response.css('p.tit').css('a::text')[0].extract()

        mt = response.css('.qita.clearfix.mt15').css('li')

        feiyong = response.css('ul.feiyong').css('li')

        # 经营模式
        corp_business_model = mt[1].css('span::text')[0].extract()
        # 品牌源地
        brand_source = ""
        # 门店总数
        total_number_of_store = feiyong[2].css('p::text')[0].extract()
        # 合同期限
        contract_period = ""
        # 经营产品
        operating_products = response.css('p.det').css('span::text')[0].extract()
        # 适合人群
        suitable_for_the_crowd = mt[3].css('span::text')[0].extract()

        # 投资金额
        investment_amount = response.css('.store-right.fr').css('li')[0].css('strong::text')[0].extract()

        # 一级行业
        primary_industry = response.css('div.weizhi').css('a[href]::text')[2].extract()

        # 二级行业
        secondary_industry = ""

        # 公司地址
        corp_address = ""

        # 公司名称
        corp_name = title

        # 公司成立时间
        corp_create_time = mt[4].css('span::text')[0].extract()

        # 加盟区域
        jmqy = mt[0].css('span::text')[0].extract()

        # 店铺面积
        store_area = feiyong[3].css('p::text')[0].extract()

        keys = response.css('.stair-wz.f16').css('b.s-oe::text').extract()

        values = response.css('div.det-jies.f16')

        product_introduce = ""
        project_benefits = ""
        project_support = ""
        project_flow = ""
        project_condition = ""
        project_feiyong = ""
        for key in keys:

            if key.strip() == "品牌介绍" or key.strip() == "产品特色":
                product_introduce = product_introduce + "".join(values[keys.index(key)].css('p').extract())

            elif key.strip() == "加盟详情":
                product_introduce = product_introduce + "".join(values[keys.index(key)].css('p').extract())

            elif key.strip() == "加盟前景":
                product_introduce = product_introduce + "".join(values[keys.index(key)].css('p').extract())

            elif key.strip() == "加盟优势":
                project_benefits = "".join(values[keys.index(key)].css('p').extract())

            elif key.strip() == "加盟支持":
                project_support = "".join(values[keys.index(key)].css('p').extract())

            elif key.strip() == "加盟流程":
                project_flow = "".join(values[keys.index(key)].css('p').extract())

            elif key.strip() == "加盟条件":

                project_condition = "".join(values[keys.index(key)].css('p').extract())
            elif key.strip() == "加盟费用":
                project_feiyong = "".join(values[keys.index(key)].css('p').extract())

            elif key.strip() == "投资分析":
                project_feiyong = project_feiyong + "".join(values[keys.index(key)].css('p').extract())

            elif key.strip() == "费用分析":
                project_feiyong = project_feiyong + "".join(values[keys.index(key)].extract())

        yield {"title": title,
               "corp_business_model": corp_business_model,
               "brand_source": brand_source,
               "investment_amount": investment_amount,
               "total_number_of_store": total_number_of_store,
               "contract_period": contract_period,
               "operating_products": operating_products,
               "suitable_for_the_crowd": suitable_for_the_crowd,
               "primary_industry": primary_industry,
               'secondary_industry': secondary_industry,
               "corp_address": corp_address,
               "corp_name": corp_name,
               'corp_create_time': corp_create_time,
               "product_introduce": product_introduce,
               'project_benefits': project_benefits,
               'project_support': project_support,
               'project_flow': project_flow,
               'project_condition': project_condition,
               'pro_logo': pro_logo,
               'project_feiyong': project_feiyong,
               'project_keyword': title,
               'jmqy': jmqy,
               'store_area': store_area
               }

    def close(self, spider):
        self.driver.close()
        self.driver.quit()
