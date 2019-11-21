# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Item,Field
import scrapy
class zhihuItem(Item):

    zhihu_id = Field()
    dongtai = Field()
    answer = Field()
    question = Field()
    article = Field()
    column = Field()#专栏
    idea = Field()#想法
    zhihu_more = Field()



class InformationItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    zhihu_id = Field()
    name = scrapy.Field()
    place = scrapy.Field()#居住地
    work = scrapy.Field()#所在行业
    brief_introduction = scrapy.Field()  #个人介绍
    brief_success = Field()

class RelationshipsItem(Item):
    """ 用户关系 """
    zhihu_id = Field()
    fan_id = Field()
    followed_id = Field()
    follow_topic = Field()
    follow_column = Field()
    follow_question = Field()
    follow_favorites = Field()

    pass
