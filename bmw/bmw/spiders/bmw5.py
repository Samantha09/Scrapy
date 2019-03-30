# -*- coding: utf-8 -*-
import scrapy
from bmw.items import BmwItem


class Bmw5Spider(scrapy.Spider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        uiboxes = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxes:
            category = uibox.xpath("./div[@class='uibox-title']/a/text()").get()
            image_urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            image_urls = list(map(lambda url: "https:" + url, image_urls))
            item = BmwItem(category=category, image_urls=image_urls)
            yield item

