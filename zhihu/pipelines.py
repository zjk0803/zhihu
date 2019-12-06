# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
class ZhihuPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost',27017)
        test = client['test']
        zhihu = test['zhihu']
        self.post = zhihu


    def process_item(self, item, spider):
        #content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #self.file.write(content)
        info = dict(item)
        self.post.insert(info)

        return item

    '''  class CnblogJsonPipeline(object):
        def __init__(self):
            self.file = open("cnblogs.json", 'w')

        def process_item(self, item, spider):
            print('cnblog json')
            content = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(content)
            return item

        def close_spider(self, spider):
            self.file.close()

    class CnblogspiderPipeline(object):

        def process_item(self, item, spider):
            print("CnblogspiderPipeline")
            return item

    def close_spider(self, spider):
    self.file.close()
        '''