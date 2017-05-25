# -*- coding: utf-8 -*-

import scrapy
from .. import items


class AlexaSpider(scrapy.Spider):
    name = "alexa"
    allowed_domains = ["http://www.alexa.com/topsites"]

    def start_requests(self):
        urls = [
            {'country': 'global', 'url': 'http://www.alexa.com/topsites/'},
            {'country': 'cn', 'url': 'http://www.alexa.com/topsites/countries/CN'},
            {'country': 'us', 'url': 'http://www.alexa.com/topsites/countries/US'},
        ]

        for d in urls:
            yield scrapy.Request(d['url'], meta={'country': d['country']})

    def parse(self, response):

        sites = response.selector.css('.AlexaTable .listings .site-listing')
        for site in sites:
            country = response.meta.get('country')

            item = items.AlexaSiteItem()
            item['_collection'] = 'alexa_sites'
            item['_tags'] = ['site', 'alexa', "country:{}".format(country)]
            item['rank'] = site.css('.number::text').extract()[0]
            item['domain'] = site.css('.DescriptionCell > p > a::text').extract()[0]

            desc = site.css('.DescriptionCell > .description')
            item['description'] = ''.join(desc.xpath('text()').extract() + desc.css('span::text').extract())\
                .replace(u'\u2026', '').replace('\n', '').replace(u'\xa0', '')

            yield item
