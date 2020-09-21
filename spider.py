import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from first_spider import *

process = CrawlerProcess(get_project_settings())
process.crawl(tia.TiaSpider)
process.start()
