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
    login_url = 'https://www.zhihu.com/api/v3/oauth/sign_in'
    captcha_url = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=en'

    def start_requests(self):
        yield scrapy.Request(url=self.captcha_url,callback=self.parse_get_captcha)

    def parse_get_captcha(self, response):
        '''
        解析验证码的get请求，获取show_captcha的值。
        :param response:
        :return:
        '''
        print(response.text)
        # response.text获取的是字符串，为了方便取值，使用json的loads()方法反序列化成字典。
        is_captcha = json.loads(response.text).get("show_captcha")
        if is_captcha:
            print('有验证码')
            # 继续向captcha_url发送put请求，获取验证码图片的加密地址。
            yield scrapy.Request(url=self.captcha_url, method='PUT', callback=self.parse_image_url)

    def parse_image_url(self, response):
        '''
        解析验证码的put请求，获取图片的加密地址。
        :param response:
        :return:
        '''
        img_url = json.loads(response.text).get("img_base64")
        # 对加密图片进行解密，获取原始地址
        img_data = base64.b64decode(img_url)
        # 根据得到的Bytes-like对象，创建一个字节码对象(bytes对象)
        img_real_url = BytesIO(img_data)
        # 利用Image去请求这个图片，获得图片对象
        img = Image.open(img_real_url)
        img.save('captcha.png')

        # 调用云打码平台接口进行识别英文字母
        result = yan_zheng('captcha.png')[1]
        # 继续发起一个post请求，获取验证码识别的是否正确
        yield scrapy.FormRequest(
            url=self.captcha_url,
            callback=self.parse_post_captcha,
            formdata={
                'input_text': str(result)
            }
        )

    def parse_post_captcha(self, response):
        '''
        解析验证码的post请求，获取验证码的识别结果，输入的验证码是错误还是正确。
        :param response:
        :return:
        '''
        result = json.loads(response.text).get("success", '')
        if result:
            print('验证码输入正确')
            # 访问这个sign_in这个url进行登录
            post_data = {
                'username': '你的账号',
                'password': '你的密码'
            }
            # 此时，需要现在settings.py文件中添加scrapy允许处理的状态码(即添加HTTPERROR_ALLOWED_CODES=[400,600])，因为scrapy默认只处理[200,300]之间的状态码。
            yield scrapy.FormRequest(
                url=self.login_url,
                formdata=post_data,
                callback=self.parse_login
            )




