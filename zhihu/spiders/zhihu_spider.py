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
import sys
import os
from PIL import Image
from bs4 import BeautifulSoup
import time
import re
import json
import configparser
import requests
import http.cookiejar as cookielib
import traceback
import base64
class ZhihuSpiderSpider(scrapy.Spider):
    name = "zhihu_spider"
    allowed_domains = ["zhihu.com"]
    start_urls = ['https://www.zhihu.com/people/xia-si-gou/activities']
    #login_url = 'https://www.zhihu.com/api/v3/oauth/sign_in'
    #captcha_url = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=en'
    #follow_url = ['https://www.zhihu.com/people/xia-si-gou/following?page=1']
    def parse(self, response):
        item = InformationItem()
        selector = Selector(response)
        infos = selector.xpath('//div[@id="ProfileHeader"]')
        for info in infos():
            try:
                name = info.xpath('//span[@class = "ProfileHeader-name"]/text()').extract()[0].strip()
                place = info.xpath('//div[@class = "ProfileHeader-detailValue"]/span/text()').extract()[0].strip()
                work = info.xpath('//div[@class = "ProfileHeader-detailItem"]/div[@class = "ProfileHeader-detailValue"]/text()').extract()[0].strip()
                brief_introduction = info.xpath('//div[@class = "ztext ProfileHeader-detailValue"]/text()').extract()[0].strip()
                #brief_success = info.xpath('span[@class = "ProfileHeader-name"]/text()').extract().strip()
                #fans_num = info.xpath('span[@class = "ProfileHeader-name"]/text()').extract().strip()  # 专栏
                item['name'] = name
                item['place'] = place
                item['work'] = work
                item['brief_introduction'] = brief_introduction
                yield item
            except IndexError:
                pass
        url = ['https://www.zhihu.com/people/xia-si-gou/activities']
        yield  Request(url,callback=self.parse)

