import sys
import time
import sqlite3

list_book = []

def get_timestamp(get_time):
    time_array = time.strptime(get_time, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(time_array))
    return timestamp

with open("file.txt", "r", encoding='utf-8') as f:
    line = f.readline()
    while line:
        get_time = line[:19]
        timestamp = get_timestamp(get_time)

        if not (timestamp, line) in list_book:
            list_book.append((timestamp, line))

        line = f.readline()

for book in sorted(list_book, key=lambda info: info[0]):
    print(book[1])


conn = sqlite3.connect("tia.db")
try:
    cursor = conn.execute("SELECT timestamp from Tia")
except BaseException as e:
    if "no such table" in str(e):
        conn.execute('''CREATE TABLE Tia (id INT PRIMARY KEY NOT NULL,
                                          timestamp INT,
                                          tia_info  TEXT);''')
# print(type(cursor))