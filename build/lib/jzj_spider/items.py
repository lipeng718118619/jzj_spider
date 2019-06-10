# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QjSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    # 标题
    title = scrapy.Field()

    pro_logo = scrapy.Field()
    # 经营模式
    corp_business_model = scrapy.Field()
    # 品牌源地
    brand_source = scrapy.Field()
    # 门店总数
    total_number_of_store = scrapy.Field()
    # 合同期限
    contract_period = scrapy.Field()
    # 经营产品
    operating_products = scrapy.Field()
    # 适合人群
    suitable_for_the_crowd = scrapy.Field()
    # 投资金额
    investment_amount = scrapy.Field()

    # 一级行业
    primary_industry = scrapy.Field()

    # 二级行业
    secondary_industry = scrapy.Field()

    # 行业
    industry_code = scrapy.Field()

    # 名称
    tag = scrapy.Field()

    # 公司地址
    corp_address = scrapy.Field()

    # 公司名称
    corp_name = scrapy.Field()

    # 公司成立时间
    corp_create_time = scrapy.Field()

    join_details = scrapy.Field()

    # 项目介绍
    product_introduce = scrapy.Field()

    # 项目优势
    project_benefits = scrapy.Field()

    # 支持
    project_support = scrapy.Field()

    # 流程
    project_flow = scrapy.Field()

    # 条件
    project_condition = scrapy.Field()

    # 加盟费用
    project_feiyong = scrapy.Field()

    # 项目类型
    project_type = scrapy.Field()

    # 项目关键字
    project_keyword = scrapy.Field()

    # 店铺面积
    store_area = scrapy.Field()

    # 加盟区域
    jmqy = scrapy.Field()


