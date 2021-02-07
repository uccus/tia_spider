import os
import time
import datetime

while True:
    os.system("scrapy crawl tia")

    now = datetime.datetime.now()
    print ("当前系统时间是: ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

    time.sleep(3600)