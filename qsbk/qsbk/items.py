# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QsbkItem(scrapy.Item):
    """固定可以传哪些参数，不会传多"""
    author = scrapy.Field()
    content = scrapy.Field()
    fans = scrapy.Field()
