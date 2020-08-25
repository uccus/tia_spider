import scrapy


class WeoponSpider(scrapy.Spider):
    name = 'weopon'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
