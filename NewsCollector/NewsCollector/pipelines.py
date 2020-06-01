# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem
from scrapy import settings
import logging
from pymongo import MongoClient



class NewscollectorPipeline:
    collection = 'articles_collection'

    def __init__(self):
        client = MongoClient("mongodb+srv://micca55:wIE079CMw8fT0FNo@cluster0-sweiq.mongodb.net/test?retryWrites=true&w=majority")
        db = client.get_database('nyt_db')
        self.collection = db.articles_collection

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('Missing %s of blogpost from %s' % (data, item['url']))

        if valid:
            news = [{
                'url' : item['url'],
                'headline' : item['headline'],
                'author' : item['author'],
                'publishDate' : item['publishDate'],
                'text' : item['text']
            }]

            self.collection.insert(news)
            logging.info('Item wrote to MongoDB database')

        return item
