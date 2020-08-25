import scrapy
from scrapy.crawler import CrawlerProcess
from first_spider import tia

process = CrawlerProcess()
process.crawl(tia.TiaSpider)
process.start()