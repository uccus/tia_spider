import sys
import time

dict_book = {}

def get_timestamp(get_time):
    time_array = time.strptime(get_time, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(time_array))
    return timestamp

with open("file.txt", "r", encoding='utf-8') as f:
    line = f.readline()
    while line:
        get_time = line[:19]
        timestamp = get_timestamp(get_time)
        dict_book[timestamp] = line
        line = f.readline()

for book in sorted(dict_book):
    print(dict_book[book])