# -*- coding: utf-8 -*-

import scrapy
from scrapy import Spider

from scrapy.http import Request

from zhipin.items import ZhipinItem

#from scrapy_redis.spiders import RedisSpider

class zhipinSpider(Spider):

    name ="zhipin"
    start_urls = ['http://www.zhipin.com/job_detail/?query=php&scity=100010000&source=1']
    allowed_domains = ["www.zhipin.com"]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url,callback=self.parse)

    def parse(self,response):
        lianjie =response.xpath('//div[@class="job-primary"]')
        for dizhi in lianjie:
            item = ZhipinItem()
            item['name'] = dizhi.xpath('div[@class="info-primary"]/h3[@class="name"]/a/text()').extract()[0]
            item['xinzi'] = dizhi.xpath('div[@class="info-primary"]/h3[@class="name"]/a/span[@class="red"]/text()').extract()[0]
            item['dizhi'] = dizhi.xpath('div[@class="info-primary"]/p/text()').extract()[0]
            item['gongsi'] = dizhi.xpath('div[@class="info-company"]/div[@class="company-text"]/h3[@class="name"]/a/text()').extract()[0]
            item['hangye'] = dizhi.xpath('div[@class="info-company"]/div[@class="company-text"]/p/text()').extract()[0]
            item['jieduan'] = dizhi.xpath('div[@class="info-company"]/div[@class="company-text"]/p/text()').extract()[1]
            item['guimo'] = dizhi.xpath('div[@class="info-company"]/div[@class="company-text"]/p/text()').extract()[2]
            yield item
            jj = response.xpath('//div[@class="page"]/a/@href').extract()[-1]
            print jj
            #exit(0)
            if jj !='javascript:;':
                ff ='http://www.zhipin.com/'+jj
                yield Request(url=ff,callback=self.parse,dont_filter = True)