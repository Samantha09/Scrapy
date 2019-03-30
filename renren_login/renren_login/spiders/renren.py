# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"

        data = {
            "email": '15692036272',
            "password": "951218/lucky",
        }
        request = scrapy.FormRequest(url, formdata=data, callback=self.parse_page)  # 发送post请求，推荐使用scrapy.FormRequest
        yield request

    def parse_page(self, response):
        with open('renren.html', 'w', encoding='utf8') as fp:
            fp.write(response.text)
