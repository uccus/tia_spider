import sqlite3
import time

def get_timestamp(get_time):
    time_array = time.strptime(get_time, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(time_array))
    return timestamp

conn = sqlite3.connect("tia.db")
c = conn.cursor()

timestamp = get_timestamp("2020-08-02 06:00:00")
print(timestamp)
# str_sql = "INSERT INTO Tia VALUES (1609947900, '2021-01-06 23:45:00 107 107 test 打开 三阶专属装备 获得:硬皮护胫');"
str_sql = "INSERT INTO Tia VALUES (1596319200, '2020-08-02 22:00:00 107 107 test 打开 低阶高级技能 获得:高级导弹技能书');"
# str_sql = "INSERT INTO Tia VALUES (1611266400, '2021-01-22 06:00:00 107 107 test 打开 四阶通用装备 获得:弯月弓');"
# c.execute(str_sql)
# conn.commit()
# conn.close()