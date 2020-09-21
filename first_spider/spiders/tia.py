import scrapy
import json
import time
import sqlite3
from first_spider.items import FirstSpiderItem

class TiaSpider(scrapy.Spider):
    name = 'tia'
    allowed_domains = ['tia.163.com']
    cur_page = 1
    # page_count = 19800 / 200
    page_count = 10
    url = "http://comp-sync.webapp.163.com/x11/sync_paged_list?game=x11&page={}&per_page=200".format(cur_page)
    start_urls = [url]
    conn = sqlite3.connect("tia.db")
    c = conn.cursor()
    latest_time = (0, "")

    def get_nexturl(self):
        self.cur_page += 1
        if self.cur_page > self.page_count:
            return None
        url = "http://comp-sync.webapp.163.com/x11/sync_paged_list?game=x11&page={}&per_page=200".format(self.cur_page)
        return url
 
    def parse(self, response):
        # item = FirstSpiderItem()
        data = response.xpath("//*/body/p//text()").extract()
        # item['award_info'] = data[0]
        # yield item
        need_next = self.parse_json(data[0])
        if True:
            url = self.get_nexturl()
            if url == None:
                print("over")
                return
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)
        pass

    def parse_json(self, data):
        need_next = False
        js_data = json.loads(data)
        js_data_list = js_data['data']

        self.c.execute("BEGIN TRANSACTION")
        for i in range(0, len(js_data_list)):
            get_time = js_data_list[i]['get_time']
            server = js_data_list[i]['user_info']['server']
            server_name = js_data_list[i]['user_info']['server_name']

            # 记录最新更新时间
            time_array = time.strptime(get_time, "%Y-%m-%d %H:%M:%S")
            timestamp = int(time.mktime(time_array))
            if timestamp > self.latest_time[0]:
                self.latest_time = (timestamp, get_time)
                need_next = True

            str_from = js_data_list[i]['prop_info']['from']
            if "一阶通用装备" in str_from:
                continue
            if "一阶专属装备" in str_from:
                continue
            if "二阶通用装备" in str_from:
                continue

            get_info = js_data_list[i]['prop_info']['from']
            tia_info = get_time + ' ' + server + ' ' + server_name + ' ' + get_info

            # print(tia_info)
            self.save_data(get_time, tia_info)

        self.c.execute("COMMIT")
        print("cur_page: {}, 最后更新时间: {}".format(self.cur_page, self.latest_time[1]))
        return need_next

    def save_data(self, get_time, data):
        time_array = time.strptime(get_time, "%Y-%m-%d %H:%M:%S")
        timestamp = int(time.mktime(time_array))

        try:
            cursor = self.conn.execute("SELECT timestamp from Tia")
        except BaseException as e:
            if "no such table" in str(e):
                self.conn.execute('''CREATE TABLE Tia (timestamp INT, tia_info  TEXT);''')

        str_sql = "SELECT * from Tia where tia_info LIKE '{}';".format(data)
        self.c.execute(str_sql)
        list_data = self.c.fetchall()
        if len(list_data) > 0:
            return

        self.conn.execute("INSERT INTO Tia (timestamp, tia_info) VALUES (?,?);", (timestamp, data))

    def get_latest_time(self):
        return self.latest_time[1]