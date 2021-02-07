import sys
import getopt
import time
import sqlite3
import tia_data

class G:
    common = True           # 普通查询(技能书)
    should_print = False
    query_all = False
    query_everything = False
    query_all_zhiye = False
    count = 0               # 一轮计数
    za = False              # 杂项(项链腰带水壶)
    tz = False              # 三专
    tt = False              # 三通
    fz = False              # 四专
    ft = False              # 四通

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
    zhiye_keywords, output_data, zhiye_name = [], [], []
    str_filter = ""

    # 确定查看职业
    if zhiye_flag == 0:
        output_data = tia_data.zhiye_book
        zhiye_name = tia_data.zhiye_des
    else:
        output_data.append(tia_data.zhiye_book[zhiye_flag - 1])
        zhiye_name.append(tia_data.zhiye_des[zhiye_flag - 1])

    # 确定职业书籍关键词
    if G.common:
        if book_prefix == 0:
            if zhiye_flag == 0:
                zhiye_keywords = tia_data.zhiye_def_l
            else:
                zhiye_keywords.append(tia_data.zhiye_def_l[zhiye_flag - 1])
        elif book_prefix == 1:
            if zhiye_flag == 0:
                zhiye_keywords = tia_data.zhiye_def_m
            else:
                zhiye_keywords.append(tia_data.zhiye_def_m[zhiye_flag - 1])
        elif book_prefix == 2:
            if zhiye_flag == 0:
                zhiye_keywords = tia_data.zhiye_def_h
            else:
                zhiye_keywords.append(tia_data.zhiye_def_h[zhiye_flag - 1])
    # print(zhiye_keywords)
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
        elif book_prefix == 1 and book_suffix == 2:
            str_filter = "中阶高级"
        elif book_prefix == 2 and book_suffix == 0:
            str_filter = "高阶初级"
        elif book_prefix == 2 and book_suffix == 1:
            str_filter = "高阶中级"
        elif book_prefix == 2 and book_suffix == 2:
            str_filter = "高阶高级"

    # 确定装备关键词
    if G.tz:
        if zhiye_flag == 0:
            zhiye_keywords = tia_data.tz_zhuang_def
        else:
            zhiye_keywords.append(tia_data.tz_zhuang_def[zhiye_flag - 1])
        if G.za:
            zhiye_keywords = tia_data.tz_za
        str_filter = "三阶专属"

    if G.tt:
        if zhiye_flag == 0:
            zhiye_keywords = tia_data.tz_zhuang_def
        else:
            zhiye_keywords.append(tia_data.tt_zhuang_def[zhiye_flag - 1])
        if G.za:
            zhiye_keywords = tia_data.tt_za
        str_filter = "三阶通用"

    if G.ft:
        if zhiye_flag == 0:
            zhiye_keywords = tia_data.tz_zhuang_def
        else:
            zhiye_keywords.append(tia_data.ft_zhuang_def[zhiye_flag - 1])
        if G.za:
            zhiye_keywords = tia_data.ft_za
        str_filter = "四阶通用"

    if G.fz:
        str_filter = "四阶专属"

    begin_parse_data(zhiye_keywords, output_data, zhiye_name, str_filter)
    pass

def begin_parse_data(zhiye_keywords, output_data, zhiye_name, str_filter):
    count, total = 0, 0
    all_data = get_data_from_db()
    print(str_filter)
    # print(zhiye_keywords)
    # print(zhiye_name)
    for data in sorted(all_data, key=lambda books: books[0]):
        # 单条数据
        single_data = data[1]
        # print(single_data)
        # continue
        # 服务器过滤
        if not "107" in single_data:
            continue
        # 自定义
        # if not "三阶专属" in single_data:
            # continue
        # if not "天" in single_data:
            # continue
        # print(single_data)
        # continue
        # if not "上古" in single_data:
            # continue
        # print(single_data)
        # if not "远古" in single_data:
        #     continue
        # print(single_data)
        # if not "古神" in single_data:
        #     continue
        # print(single_data)
        # 查询所有物品
        if G.query_everything:
            print(single_data)
            continue               
        # 根据过滤字段过滤
        if not str_filter in single_data:
            continue
        # 中中时间过滤
        if str_filter == "中阶中级" and data[0] <= 1605112398:
            continue 
        # 低中时间过滤
        if str_filter == "低阶中级" and data[0] <= 1605801600:
            continue 
        # 显示过滤后所有开出物品
        if G.query_all:
            count = count + 1
            if not G.za:
                # 为数据贴上职业标签
                name = "---- ----"
                for keywords in zhiye_keywords:
                    for keyword in keywords:
                        if keyword in single_data[-15:]:
                            name = zhiye_name[zhiye_keywords.index(keywords)]
                            if G.common:
                                book_s = tia_data.zhiye_s[zhiye_keywords.index(keywords)][keywords.index(keyword)]
                                name = name + " " + book_s
                            if zhiye_keywords.index(keywords) in range(0, 3):
                                name = "近战 " + name
                            elif zhiye_keywords.index(keywords) in range(3, 6):
                                name = "法系 " + name
                            else:
                                name = "射手 " + name
                            break
                
                print(name, single_data)
                if count % 54 == 0:
                    total = total + 1
                    # print("第 {} 轮--------------------------------------------------------------------------".format(total + 1))
            else:
                for keyword in zhiye_keywords:
                    if keyword in single_data:
                        print(single_data)
                        break
            continue
        
        # 筛选职业关键词
        for i in range(0, len(zhiye_keywords)):
            for keyword in zhiye_keywords[i]:
                if keyword in single_data[-15:]:
                    output_data[i].append(single_data)
                    break
    
    # 显示指定职业剩余未开出物品
    if not G.query_all:
        for i in range(0, len(output_data)):
            query_left_book(output_data[i], zhiye_keywords[i], zhiye_name[i])

def query_left_book(data_selected, zhiye_keywords, zhiye_name):
    idx, total = 0, 0
    for book in data_selected:
        if G.should_print:
            idx = idx + 1
            print(book)
            if idx % 6 == 0:
                total = total + 1
                print("第 {} 轮--------------------------------------------------------------------------".format(total + 1))

    left = len(data_selected) % 6
    if left > 0:
        book_opened = []
        for i in range(0, left):
            book_opened.append(data_selected[len(data_selected) - 1 - i])

        book_left = []
        for book in book_opened:
            for zb in zhiye_keywords:
                if zb in book:
                    book_left.append(zb)
                    break
        
        Left = ""
        for keyword in zhiye_keywords:
            if not keyword in book_left:
                for n in range(0, 5-len(keyword)):
                    keyword += '  '
                Left = Left + keyword
        print("{}：{}".format(zhiye_name, Left))
    else:
        print("{}：请等待下一轮".format(zhiye_name))

def query_all():
    all_books = get_data_from_db()
    for book in sorted(all_books, key=lambda books: books[0]):
        book_des = book[1]
        print(book_des)

def print_single_data(single_data):
    if G.common:
        return


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

    opts,args = getopt.getopt(sys.argv[1:],'-a-w-z-q-f-s-m-Q-l-c-L-M-H-P-I-S-h-p',["all","allbook","jianshi","mofa","sheshou","tz","tt","ft","fz", "za"])
    for opt_name,opt_value in opts:
        if opt_name in ('-h'):
            help_info()
            exit()
        elif opt_name in ('-a'):
            zhiye_flag = 0
        elif opt_name in ('-w') or opt_name == ("--jianshi"):
            zhiye_flag = 1
        elif opt_name in ('-z') or opt_name == ("--mofa"):
            zhiye_flag = 2
        elif opt_name in ('-q') or opt_name == ("--sheshou"):
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
        elif opt_name in ('--tz'):
            G.tz = True
            G.common = False
        elif opt_name in ('--tt'):
            G.tt = True
            G.common = False
        elif opt_name in ('--fz'):
            G.fz = True
            G.common = False
        elif opt_name in ('--ft'):
            G.ft = True
            G.common = False
        elif opt_name == ('--za'):
            G.za = True

    pre_parse_data(zhiye_flag, book_prefix, book_suffix)