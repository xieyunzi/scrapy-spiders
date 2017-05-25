# -*- coding: utf-8 -*-
import scrapy


class AlexaChinazSpider(scrapy.Spider):
    name = "alexa-chinaz"
    allowed_domains = ["http://alexa.chinaz.com"]
    start_urls = ['http://http://alexa.chinaz.com/Country/index_CN.html']

    def parse(self, response):
        pass
