# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo
from scrapy.exceptions import DropItem
from scrapy import logformatter


class MongoDBPipeline(object):


    def __init__(self):
        connection = pymongo.MongoClient(
            'localhost', 27017
        )
        db = 'news'
        self.collection = 'url'

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing data!")
        if valid:
            logformatter.msg("Urls are added to MongoDB database!",
                    level=logformatter.DEBUG, spider=spider)
        return item


