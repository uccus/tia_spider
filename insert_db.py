import sqlite3
import time

def get_timestamp(get_time):
    time_array = time.strptime(get_time, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(time_array))
    return timestamp

conn = sqlite3.connect("tia.db")
c = conn.cursor()

# timestamp = get_timestamp("2020-08-10 00:00:00")
# print(timestamp)
str_sql = "INSERT INTO Tia VALUES (1596988800, '2020-08-10 00:00:00 111 111 test 打开 低阶中级技能 获得:中级信仰守护技能书');"
c.execute(str_sql)
conn.commit()