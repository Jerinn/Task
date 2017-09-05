# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CtripItem(scrapy.Item):

    hotel_name = scrapy.Field()
    price = scrapy.Field()
    rate = scrapy.Field()
    image_src = scrapy.Field()

