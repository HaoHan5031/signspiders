# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SignItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    sign = scrapy.Field()

if __name__ == "__main__":
    strs = '1、We are all stories in the end'

    npos = strs.find('、')
    print npos
    strs.replace('、', '9999')
    # if npos != -1:
    #     strsub = strs[0:npos+2]
    #     print strsub
    #     strs.replace('、', '')
    print strs
