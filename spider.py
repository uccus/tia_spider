import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from first_spider import *

process = CrawlerProcess(get_project_settings())
# process.crawl(tia.TiaSpider)
process.crawl(test.TestSpider)
process.start()