# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from sign.items import SignItem
from scrapy_redis.spiders import RedisSpider

class SignSpiders(CrawlSpider):
    name = "sign"
    allowed_domains = ["woyaogexing.com"]
    start_urls = [
        "http://www.woyaogexing.com/gexing/z/geci/index.html",
    ]

    def start_requests(self):
        yield Request(url='http://www.woyaogexing.com/gexing/z/geci/index.html',
                      callback=self.parse_ph_key)

    def parse_ph_key(self, response):
        selector = Selector(response)
        items = selector.xpath('//div[@class="txtContent z"]//p/text()').extract()

        for i in items:
            item = SignItem()
            item['sign'] = i
            yield item

        url_nextcon = selector.xpath(u'//a[contains(.//text(), "下一页")]/@href').extract()
        yield Request(url='http://www.woyaogexing.com/' + url_nextcon[0],
                      callback=self.parse_ph_key)



    # def parse_sign_key(self, response):
    #     selector = Selector(response)
    #     items = selector.xpath('//div[@class="txtContent z"]//p/text()').extract()
    #
    #     for i in items:
    #         i = i.encode('utf-8')
    #         npos = i.find('、')
    #         if npos != -1:
    #             strsub = i[:npos]
    #             i.replace(strsub, '')
    #         item = SignItem()
    #         item['sign'] = i
    #         yield item


