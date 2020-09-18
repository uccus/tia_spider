import sys
import getopt
import time
import sqlite3
import tia_data

class G:
    common = True
    should_print = False
    query_all = False
    query_all_just_book = False
    query_all_zhiye = False

def get_timestamp(get_time):
    time_array = time.strptime(get_time, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(time_array))
    return timestamp

def get_data_from_db():
    conn = sqlite3.connect("tia.db")
    c = conn.cursor()
    c.execute("SELECT * from Tia")
    all_data = c.fetchall()
    conn.close()
    return all_data

def pre_parse_data(zhiye_flag, book_prefix, book_suffix):
    zhiye_def, zhiye_book, zhiye_des = [], [], []
    str_filter = ""

    # 确定查看职业
    if zhiye_flag == 0:
        zhiye_book = tia_data.zhiye_book
        zhiye_des = tia_data.zhiye_des
    else:
        zhiye_book.append(tia_data.zhiye_book[zhiye_flag - 1])
        zhiye_des.append(tia_data.zhiye_des[zhiye_flag - 1])

    # 确定职业书籍
    if book_prefix == 0:
        if zhiye_flag == 0:
            zhiye_def = tia_data.zhiye_def_l
        else:
            zhiye_def.append(tia_data.zhiye_def_l[zhiye_flag - 1])
    elif book_prefix == 1:
        if zhiye_flag == 0:
            zhiye_def = tia_data.zhiye_def_m
        else:
            zhiye_def.append(tia_data.zhiye_def_m[zhiye_flag - 1])
    elif book_prefix == 2:
        if zhiye_flag == 0:
            zhiye_def = tia_data.zhiye_def_h
        else:
            zhiye_def.append(tia_data.zhiye_def_h[zhiye_flag - 1])
    # print(zhiye_def)

    # 确定过滤字段
    if book_prefix == 0 and book_suffix == 0:
        str_filter = "低阶初级"
    elif book_prefix == 0 and book_suffix == 1:
        str_filter = "低阶中级"
    elif book_prefix == 0 and book_suffix == 2:
        str_filter = "低阶高级"
    elif book_prefix == 1 and book_suffix == 0:
        str_filter = "中阶初级"
    elif book_prefix == 1 and book_suffix == 1:
        str_filter = "中阶中级"
    elif book_prefix == 2 and book_suffix == 0:
        str_filter = "高阶初级"

    begin_parse_data(zhiye_def, zhiye_book, zhiye_des, str_filter)
    pass

def begin_parse_data(zhiye_def, zhiye_book, zhiye_des, str_filter):
    all_books = get_data_from_db()
    print(str_filter)
    for book in sorted(all_books, key=lambda books: books[0]):
        book_des = book[1]
        # print(book_des)
        # continue
        if not "107" in book_des:
            continue
        # if "四阶通用" in book_des:
        #     print (book_des)
        if G.query_all:
            print(book_des)
            continue
        if not str_filter in book_des:
            continue
        if G.query_all_just_book:
            print(book_des)
            continue
        for i in range(0, len(zhiye_def)):
            for book_def in zhiye_def[i]:
                if book_def in book_des:
                    zhiye_book[i].append(book_des)
                    break
    
    if G.common:
        for i in range(0, len(zhiye_book)):
            query_left(zhiye_book[i], zhiye_def[i], zhiye_des[i])

def query_left(some_books, defs, des):
    for book in some_books:
        if G.should_print:
            print(book)

    left = len(some_books) % 6
    if left > 0:
        book_opened = []
        for i in range(0, left):
            book_opened.append(some_books[len(some_books) - 1 - i])

        book_left = []
        for book in book_opened:
            for zb in defs:
                if zb in book:
                    book_left.append(zb)
                    break
        
        Left = ""
        for book in defs:
            if not book in book_left:
                for n in range(0, 5-len(book)):
                    book += '  '
                Left = Left + book
        print("{}：{}".format(des, Left))
    else:
        print("{}：请等待下一轮".format(des))

def query_all():
    all_books = get_data_from_db()
    for book in sorted(all_books, key=lambda books: books[0]):
        book_des = book[1]
        print(book_des)


def help_info():
    print("====================help_info====================")
    print("          -a 查看当前轮所有职业剩余书籍")
    print("          -w 查看当前轮武士剩余书籍")
    print("          -z 查看当前轮战士剩余书籍")
    print("          -q 查看当前轮战士剩余书籍")
    print("          -f 查看当前轮武士剩余书籍")
    print("          -s 查看当前轮战士剩余书籍")
    print("          -m 查看当前轮战士剩余书籍")
    print("          -Q 查看当前轮武士剩余书籍")
    print("          -l 查看当前轮战士剩余书籍")
    print("          -c 查看当前轮战士剩余书籍")
    print("          -L 查看当前轮低阶书籍")
    print("          -M 查看当前轮中阶书籍")
    print("          -H 查看当前轮高阶书籍")
    print("          -P 查看当前轮低级书籍")
    print("          -I 查看当前轮中级书籍")
    print("          -S 查看当前轮高级书籍")
    print("          --all 查看当前所有物品")
    print("          --allbook 查看当前所有书籍")
    pass

if __name__ == "__main__":
    book_prefix, book_suffix, zhiye_flag = 0, 0, 0

    opts,args = getopt.getopt(sys.argv[1:],'-a-w-z-q-f-s-m-Q-l-c-L-M-H-P-I-S-h-p',["all","allbook"])
    for opt_name,opt_value in opts:
        if opt_name in ('-h'):
            help_info()
            exit()
        elif opt_name in ('-a'):
            zhiye_flag = 0
        elif opt_name in ('-w'):
            zhiye_flag = 1
        elif opt_name in ('-z'):
            zhiye_flag = 2
        elif opt_name in ('-q'):
            zhiye_flag = 3
        elif opt_name in ('-f'):
            zhiye_flag = 4
        elif opt_name in ('-s'):
            zhiye_flag = 5
        elif opt_name in ('-m'):
            zhiye_flag = 6
        elif opt_name in ('-Q'):
            zhiye_flag = 7
        elif opt_name in ('-l'):
            zhiye_flag = 8
        elif opt_name in ('-c'):
            zhiye_flag = 9
        elif opt_name in ('-L'):
            book_prefix = 0
        elif opt_name in ('-M'):
            book_prefix = 1
        elif opt_name in ('-H'):
            book_prefix = 2
        elif opt_name in ('-P'):
            book_suffix = 0
        elif opt_name in ('-I'):
            book_suffix = 1
        elif opt_name in ('-S'):
            book_suffix = 2
        elif opt_name in ('-p'):
            G.should_print = True
        elif opt_name in ('--all'):
            G.query_all = True
            G.common = False
        elif opt_name in ('--allbook'):
            G.query_all_just_book = True
            G.common = False

    pre_parse_data(zhiye_flag, book_prefix, book_suffix)