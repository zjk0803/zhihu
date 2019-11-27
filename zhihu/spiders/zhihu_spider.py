# -*- coding: utf-8 -*-
import scrapy
import re
from lxml import etree
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.utils.project import get_project_settings
from zhihu.items import InformationItem, RelationshipsItem,zhihuItem

import requests
import time

import datetime
from bs4 import BeautifulSoup
import sys

class ZhihuSpiderSpider(scrapy.Spider):
    name = "zhihu_spider"
    allowed_domains = ["www.zhihu.com/people"]
    start_urls = ['https://www.zhihu.com/people/xia-si-gou/activities']

    def start_requests(self,response):
        '''start_uids = [
            'xia-si-gou',  # 吓死狗
            'emily-48-91-53'

        ]
        for uid in start_uids:
            yield Request(url="https://www.zhihu.com/people/%s/activities" % uid, callback=self.parse_information)
            '''
        #info_item = InformationItem()
        #selector = Selector(response)
        #info_item['name'] = selector.xpath('//span[@class="ProfileHeader-name"]/text()').extract()
        self.log("title:%s" % response.xpath('//span[@class="ProfileHeader-name"]/text()').extract())

        #yield info_item
        #scrapyprint(info_item['name'])

        ''' def parse_information(self, response):
        """ 抓取个人信息 """

        info_item = InformationItem()
        selector = Selector(response)
        info_item['name'] = selector.xpath('//span[@class="ProfileHeader-name"]/text()').extract()
        yield info_item
        #print(name)'''
#1pritn




