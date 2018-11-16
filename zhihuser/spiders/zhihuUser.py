# -*- coding: utf-8 -*-
import scrapy


class ZhihuuserSpider(scrapy.Spider):
    name = 'zhihuUser'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    def parse(self, response):
        pass
