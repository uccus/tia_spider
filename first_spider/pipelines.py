# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import time
import sqlite3
from itemadapter import ItemAdapter


class FirstSpiderPipeline:
    conn = None
    c = None
    latest_time = (0, "")

    def open_spider(self, spider):
        self.conn = sqlite3.connect("tia.db")
        self.c = conn.cursor()
        pass

    def close_spider(self, spider):
        self.conn.close()
        pass

    def process_item(self, item, spider):
        # print(item["award_info"])
        parse_json(item['award_info'])
        return item

    def parse_json(self, data):
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

            str_from = js_data_list[i]['prop_info']['from']
            if "一阶通用装备" in str_from:
                continue
            if "一阶专属装备" in str_from:
                continue
            if "二阶通用装备" in str_from:
                continue

            get_info = js_data_list[i]['prop_info']['from']
            tia_info = get_time + ' ' + server + ' ' + server_name + ' ' + get_info

            self.save_data(get_time, tia_info)

        self.c.execute("COMMIT")
        print("最后更新时间: " + self.latest_time[1])

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