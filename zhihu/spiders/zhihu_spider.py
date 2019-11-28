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

    def parse(self, response):
        # 他关注的人数
        tnum = response.xpath("//strong[@class='NumberBoard-itemValue']/text()").extract()[0]
        # 粉丝数
        fnum = response.xpath("//strong[@class='NumberBoard-itemValue']/text()").extract()[1]
        print("他关注的人数为：%s" % tnum)
        print("他粉丝的人数为：%s" % fnum)


