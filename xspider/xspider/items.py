# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Position_Url_List(scrapy.Item):

    # 这里专门收集符合条件的所有岗位详情页的列表，例如 https://www.lagou.com/jobs/3353388.html 这样子
    position_url = scrapy.Field()

class Position_Info(scrapy.Item):
    
    # 职位的详细数据

    position_name = scrapy.Field()
    position_company = scrapy.Field()
    position_pay = scrapy.Field()
    position_detail = scrapy.Field()
    position_location = scrapy.Field()
    position_url = scrapy.Field()

    pass