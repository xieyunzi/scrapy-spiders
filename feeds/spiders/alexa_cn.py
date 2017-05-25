# -*- coding: utf-8 -*-
import scrapy


class AlexaCnSpider(scrapy.Spider):
    name = "alexa-cn"
    allowed_domains = ["http://www.alexa.cn"]
    start_urls = ['http://http://www.alexa.cn/siterank']

    def parse(self, response):
        pass
