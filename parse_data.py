import sys
import getopt
import time
import sqlite3

ll_book = []    # 低阶初级
ml_book = []    # 中阶初级
hl_book = []    # 高阶初级
lm_book = []    # 低阶中级
mm_book = []    # 中阶中级
lh_book = []    # 低阶高级
se_dedi = []    # 二阶专属
th_comm = []    # 三阶通用
th_dedi = []    # 三阶专属
pet     = []    # 宠物
gift    = []    # 馈赠
other   = []

wushi,zhanshi,qishi,fashi,saman,mushi,qiang,lieren,cike   = [],[],[],[],[],[],[],[],[]

wushi_book      = ["影遁","静默之刃","连续打击","追踪","敏锐","闪现刺杀"]
zhanshi_book    = ["野蛮掠夺","野蛮反击","跃击","愤怒","投掷","振奋"]
qishi_book      = ["减速光环","冷静","信仰守护","圣光治愈","盾击","圣光之盾"]
fashi_book      = ["火球","火焰枷锁","变形","霜爆","焦土","连锁闪电"]
saman_book      = ["枯萎","三头","水元素","生命汲取","致命连接","伤害加深"]
mushi_book      = ["天使","生命暖流","鼓舞","辉光守卫","镇定光环","庇护"]
qiang_book      = ["连射","导弹","燃油弹","火炮","麻醉弹","冲击弹"]
cike_book       = ["毒液","毒镖","暗影波动","分身术","雾隐","隐身术"]
lieren_book     = ["撒网","猎犬","石化","变狼","自然囚笼","火焰标枪"]

def get_timestamp(get_time):
    time_array = time.strptime(get_time, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(time_array))
    return timestamp

conn = sqlite3.connect("tia.db")
c = conn.cursor()
c.execute("SELECT * from Tia")
all_data = c.fetchall()

# 111所有数据
list_data = []

for data in all_data:
    if "111" in data[1]:
        list_data.append((data[0], data[1]))

# 排序归类
for data in sorted(list_data, key=lambda book: book[0]):
# for data in list_data:
    line = data[1]
    if "低阶初级" in line:
        ll_book.append(line)
    elif "中阶初级" in line:
        ml_book.append(line)
    elif "高阶初级" in line:
        hl_book.append(line)
    elif "低阶中级" in line:
        lm_book.append(line)
    elif "中阶中级" in line:
        mm_book.append(line)
    elif "低阶高级" in line:
        lh_book.append(line)
    elif "二阶专属" in line:
        se_dedi.append(line)
    elif "三阶通用" in line:
        th_comm.append(line)
    elif "三阶专属" in line:
        th_dedi.append(line)
    elif "灵石" in line:
        pet.append(line)
    elif "馈赠" in line:
        gift.append(line)
    else:
        other.append(line)

# tmp = []
# with open("data.txt", "r", encoding='utf-8') as f:
#     line = f.readline()
#     while line:
#         if "低阶中级" in line:
#             tmp.append(line)
#         line = f.readline()

tgt_book = lm_book
list_book = []

for book in tgt_book:
    if not "111" in book:
        continue
    get_time = book[:19]
    timestamp = get_timestamp(get_time)
    list_book.append((timestamp, book))

    if "技能" in book:
        for idx in wushi_book:
            if idx in book and not (timestamp, book) in wushi:
                wushi.append((timestamp,book))
                continue
        for idx in zhanshi_book:
            if idx in book and not (timestamp, book) in zhanshi:
                zhanshi.append((timestamp,book))
                continue
        for idx in qishi_book:
            if idx in book and not (timestamp, book) in qishi:
                qishi.append((timestamp,book))
                continue
        for idx in fashi_book:
            if idx in book and not (timestamp, book) in fashi:
                fashi.append((timestamp,book))
                continue
        for idx in mushi_book:
            if idx in book and not (timestamp, book) in mushi:
                mushi.append((timestamp,book))
                continue
        for idx in saman_book:
            if idx in book and not (timestamp, book) in saman:
                saman.append((timestamp,book))
                continue
        for idx in qiang_book:
            if idx in book and not (timestamp, book) in qiang:
                qiang.append((timestamp,book))
                continue
        for idx in lieren_book:
            if idx in book and not (timestamp, book) in lieren:
                lieren.append((timestamp,book))
                continue
        for idx in cike_book:
            if idx in book and not (timestamp, book) in cike:
                cike.append((timestamp,book))
                continue
    # print(book)

if __name__ == "__main__":
    zhiye = []
    zhiye_book = []
    is_all = False
    opts,args = getopt.getopt(sys.argv[1:],'-a-h-w-z-q-f-s-m-Q-l-c-v',['help','version'])
    for opt_name,opt_value in opts:
        if opt_name in ('-h','--help'):
            print("Help info")
            exit()
        if opt_name in ('-v','--version'):
            print("The current Version is v1.0 ")
            exit()
        if opt_name in ('-a'):
            zhiye = [wushi, zhanshi, qishi, fashi, saman, mushi, qiang, lieren, cike]
            is_all = True
        elif opt_name in ('-w'):
            zhiye = wushi
            zhiye_book = wushi_book
        elif opt_name in ('-z'):
            zhiye = zhanshi
            zhiye_book = zhanshi_book
        elif opt_name in ('-q'):
            zhiye = qishi
            zhiye_book = qishi_book
        elif opt_name in ('-f'):
            zhiye = fashi
            zhiye_book = fashi_book
        elif opt_name in ('-s'):
            zhiye = saman
            zhiye_book = saman_book
        elif opt_name in ('-m'):
            zhiye = mushi
            zhiye_book = mushi_book
        elif opt_name in ('-Q'):
            zhiye = qiang
            zhiye_book = qiang_book
        elif opt_name in ('-l'):
            zhiye = lieren
            zhiye_book = lieren_book
        elif opt_name in ('-c'):
            zhiye = cike
            zhiye_book = cike_book
        else:
            print("help info")

    if is_all:
        zhiye_des = ["武士","战士","骑士","法师","萨满","牧师","枪手","猎人","刺客"]
        zhiye_books = [wushi_book, zhanshi_book, qishi_book, fashi_book, saman_book, mushi_book, qiang_book, lieren_book, cike_book]
        for idx in range(0, 9):
            books = zhiye[idx]
            data_sorted = sorted(books, key=lambda book_info: book_info[0])    
            left = len(data_sorted) % 6

            if left > 0:
                book_opened = []
                for i in range(0, left):
                    book_opened.append(data_sorted[len(data_sorted) - 1 - i][1])

                book_left = []
                for book in book_opened:
                    for zb in zhiye_books[idx]:
                        if zb in book:
                            book_left.append(zb)
                            break
                
                Left = ""
                for book in zhiye_books[idx]:
                    if not book in book_left:
                        for n in range(0, 5-len(book)):
                            book += '  '
                        Left = Left + book
                print("{}：{}".format(zhiye_des[idx], Left))

            else:
                print("请等待下一轮")
    else:
        data_sorted = sorted(zhiye, key=lambda book_info: book_info[0])
        for book in data_sorted:
            print(book[1])

        left = len(data_sorted) % 6

        if left > 0:
            book_opened = []
            for i in range(0, left):
                book_opened.append(data_sorted[len(data_sorted) - 1 - i][1])

            book_left = []
            for book in book_opened:
                for zb in zhiye_book:
                    if zb in book:
                        book_left.append(zb)
                        break
            
            Left = ""
            for book in zhiye_book:
                if not book in book_left:
                    Left = Left + book + "   "
            print("当前书库剩余：" + Left)

        else:
            print("请等待下一轮")

    pass