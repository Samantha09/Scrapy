# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bmw.items import BmwItem


class Bmw52Spider(CrawlSpider):
    name = 'bmw52'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/65.+'), callback='parse_page', follow=True),  # 还有第二页
    )

    def parse_page(self, response):
        category = response.xpath("//div[@class='uibox']/div/text()").get()
        srcs = response.xpath("//div[contains(@class, 'uibox')]/ul/li//img/@src").getall()
        urls = list(map(lambda x: "https:" + x.replace("t_", ""), srcs))
        item = BmwItem(category=category, image_urls=urls)
        yield item


    def test_spider(self, response):
        pass
