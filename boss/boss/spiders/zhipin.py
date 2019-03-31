# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem


class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101280100/?query=python&page=1&ka=page-1']

    rules = (
        # 匹配职位列表页的规则
        Rule(LinkExtractor(allow=r'.+\?query=python&page=\d'), follow=True),
        # 匹配职位详情页的规则
        Rule(LinkExtractor(allow=r'.+job_detail/.+\.html'), callback='parse_detail', follow=False)
    )

    def parse_detail(self, response):
        title = response.xpath("//div[@class='name']/h1/text()").get()
        salary = response.xpath("//span[@class='salary']/text()").get().strip()
        company = response.xpath("//div[@class='detail-content']//div[@class='name']/text()").get()
        job_info = response.xpath("//div[@class='info-primary']//p/text()").getall()
        city = job_info[0]
        work_years = job_info[1]
        education = job_info[2]
        item = BossItem(title=title, salary=salary, company=company, city=city, work_years=work_years, education=education)
        yield item


