# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import NewscollectorItem


class NytSpider(CrawlSpider):
    name = 'nyt_spider'
    allowed_domains = ['nytimes.com']
    start_urls = ['https://www.nytimes.com/']

    rules = (
        Rule(LinkExtractor(deny_domains=('https://www.nytimes.com/video')), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        print("processing: "+response.url)

        item = NewscollectorItem()
        # item['title'] = response.css("title::text").get()
        # item['byauthor'] = response.xpath('//meta[@name="byl"]/@content').get()
        structuralStr = response.xpath('//script[@type="application/ld+json"]/text()').get()
        item['url'] = response.url
        structuralJSON = json.loads(structuralStr)
        item['headline'] = structuralJSON["headline"]
        item['author'] = structuralJSON["author"][0]["name"]
        item['publishDate'] = structuralJSON["datePublished"]
        item['text'] = ' '.join(response.css("p::text").getall())

        yield item
