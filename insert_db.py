import sqlite3
import time

def get_timestamp(get_time):
    time_array = time.strptime(get_time, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(time_array))
    return timestamp

conn = sqlite3.connect("tia.db")
c = conn.cursor()

# timestamp = get_timestamp("2020-09-18 00:00:00")
# print(timestamp)
str_sql = "INSERT INTO Tia VALUES (1596988800, '2020-08-10 00:00:00 107 107 test 打开 中阶初级技能 获得:初级吞噬技能书');"
# str_sql = "INSERT INTO Tia VALUES (1600358400, '2020-09-18 00:00:00 107 107 test 打开 中阶初级技能 获得:初级暗影之舞技能书');"
c.execute(str_sql)
conn.commit()
conn.close()