# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class SignPipeline(object):
    def __init__(self):
        self.connection = pymongo.MongoClient('120.76.54.5', 27017)
        # db_auth = self.connection.admin
        # db_auth.authenticate("admin", "123456")
        self.db = self.connection.PPIM  # 切换到scrapy数据库
        self.collection = self.db.sign  # 获取到qiubai集合

    def process_item(self, item, spider):
        if not self.connection or not item:
            return
        self.collection.save(item)

    def __del__(self):
        if self.connection:
            self.connection.close()
