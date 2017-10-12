# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhipinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    xinzi = scrapy.Field()
    dizhi = scrapy.Field()
    jingyan = scrapy.Field()
    dengji = scrapy.Field()
    gongsi = scrapy.Field()
    hangye = scrapy.Field()
    jieduan = scrapy.Field()
    guimo = scrapy.Field()
    pass
