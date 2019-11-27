from scrapy import cmdline
cmdline.execute("scrapy crawl zhihu_spider -s LOG_ENABLED=False".split())
#