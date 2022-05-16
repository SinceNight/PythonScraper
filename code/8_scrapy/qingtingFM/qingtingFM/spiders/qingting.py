import scrapy


class QingtingSpider(scrapy.Spider):
    name = 'qingting'
    allowed_domains = ['qingting.fm']
    start_urls = ['http://qingting.fm/']

    def parse(self, response): #对爬虫进行爬取后，回调的函数,在函数中执行爬虫
        # print("---->",response) #网址和状态
        print("---->",response.text) #源码
        pass
