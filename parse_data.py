import sys
import time

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

wushi   = {}
zhanshi = {}
qishi   = {}
fashi   = {}
saman   = {}
mushi   = {}
qiang   = {}
cike    = {}
lieren  = {}

wushi_book = ["追踪","静默之刃","连续打击","影遁","敏锐","闪现刺杀"]
zhanshi_book = ["野蛮","跃击","愤怒","投掷","振奋"]
qishi_book = ["减速光环","冷静","信仰守护","圣光治愈","盾击","圣光之盾"]
fashi_book = ["火球","火焰枷锁","变形","霜爆","焦土","连锁闪电"]
saman_book = ["枯萎","三头","水元素","生命汲取","致命连接","伤害加深"]
mushi_book = ["天使","生命暖流","鼓舞","辉光守卫","镇定光环","庇护"]
qiang_book = ["连射","导弹","燃油弹","火炮","麻醉弹","冲击弹"]
cike_book = ["毒液","毒镖","暗影波动","分身术","雾隐","隐身术"]
lieren_book = ["撒网","猎犬","石化","变狼","自然囚笼","火焰标枪"]

def get_timestamp(get_time):
    time_array = time.strptime(get_time, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(time_array))
    return timestamp

def parse_book(book):
    if "技能" in book:
        for idx in wushi_book:
            if idx in book:
                wushi.append(book)
                return

with open("data.txt", "r", encoding='utf-8') as f:
    line = f.readline()
    while line:
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
        line = f.readline()

tgt_book = lm_book
dict_book = {}

for book in tgt_book:
    if not "111" in book:
        continue
    get_time = book[:19]
    timestamp = get_timestamp(get_time)
    dict_book[timestamp] = book

    if "技能" in book:
        for idx in wushi_book:
            if idx in book:
                wushi[timestamp] = book
                continue
        for idx in zhanshi_book:
            if idx in book:
                zhanshi[timestamp] = book
                continue
        for idx in qishi_book:
            if idx in book:
                qishi[timestamp] = book
                continue
        for idx in fashi_book:
            if idx in book:
                fashi[timestamp] = book
                continue
        for idx in mushi_book:
            if idx in book:
                mushi[timestamp] = book
                continue
        for idx in saman_book:
            if idx in book:
                saman[timestamp] = book
                continue
        for idx in qiang_book:
            if idx in book:
                qiang[timestamp] = book
                continue
        for idx in lieren_book:
            if idx in book:
                lieren[timestamp] = book
                continue
        for idx in cike_book:
            if idx in book:
                cike[timestamp] = book
                continue
    # print(book)

for i in sorted(cike):
    print(cike[i])

# for i in sorted(dict_book):
#     print(dict_book[i])

# print(tgt_book[1])
# print(len(tgt_book))
# print(len(dict_book))