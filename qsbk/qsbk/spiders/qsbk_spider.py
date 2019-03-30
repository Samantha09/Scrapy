# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from scrapy.http.response.html import HtmlResponse
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    base_domain = "https://www.qiushibaike.com"
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        div_list = response.xpath("//div[@id='content-left']/div")

        for div in div_list:
            author = div.xpath("./div[@class='author clearfix']//h2/text()").get().strip()  # 获取html标签中的文字
            content = div.xpath(".//div[@class='content']//text()").getall()  # getall提取所有信息，并返回一个列表
            detail_url = div.xpath("./a[@class='contentHerf']/@href").get()
            content = "".join(content).strip()
            item = {"author": author, "content": content}
            yield scrapy.Request(self.base_domain + detail_url, callback=self.detail_parse, meta={"item": item})

        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()

        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain + next_url, callback=self.parse)

    def detail_parse(self, response):
        item = response.meta["item"]
        fans = response.xpath("//div[@class='side-line1'][1]/text()").get()
        item = QsbkItem(author=item["author"], content=item["content"], fans=fans)
        yield item
