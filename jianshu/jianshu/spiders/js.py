# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from jianshu.items import ArticleItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z].*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath("//h1[@class='title']/text()").get()
        avatar = response.xpath("//a[@class='avatar']/img/@src").get()
        author = response.xpath("//span[@class='name']/a/text()").get()
        pub_time = response.xpath("//span[@class='publish-time']/text()").get()
        url = response.url
        article_id = re.match(r'.*?/p/([0-9a-z]{12})[\?]*.*?', response.url).group(1)
        content = response.xpath("//div[@class='show-content']").get()
        content = re.sub(r"<.*?>", "", content).strip()

        word_count  = response.xpath("//span[@class='wordage']/text()").get()
        comment_count = response.xpath("//span[@class='comments-count']/text()").get()
        like_count = response.xpath("//span[@class='likes-count']/text()").get()
        read_count = response.xpath("//span[@class='views-count']/text()").get()

        subjects = ",".join(response.xpath("//div[@class='include-collection']/a/div/text()").getall())

        item = ArticleItem(
            title=title,
            avatar=avatar,
            author=author,
            origin_url=url,
            pub_time=pub_time,
            article_id=article_id,
            content=content,
            word_count=word_count,
            comment_count=comment_count,
            like_count=like_count,
            read_count=read_count,
            subjects=subjects
        )
        yield item
