# -*- coding: utf-8 -*-
import scrapy
import re
from lxml import etree
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.utils.project import get_project_settings
from zhihu.items import InformationItem, RelationshipsItem,zhihuItem



class ZhihuSpiderSpider(scrapy.Spider):
    name = "zhihu_spider"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['http://www.zhihu.com/']

    def start_requests(self):
        start_uids = [
            'xia-si-gou',  # 吓死狗

        ]
        for uid in start_uids:
            yield Request(url="https://www.zhihu.com/%s/activities" % uid, callback=self.parse_information)


    def parse_information(self, response):
        """ 抓取个人信息 """
        information_item = InformationItem()
        selector = Selector(response)
        information_item['zhihu_id'] = re.findall('(\d+)/info', response.url)[0]

        # 获取标签里的所有text()
        text1 = ";".join(selector.xpath('body/div[@class="Card"]//text()').extract())
        nick_name = re.findall(..//span, text1)