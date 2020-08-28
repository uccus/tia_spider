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

zhiye_des = ["武士","战士","骑士","法师","萨满","牧师","枪手","猎人","刺客"]

wushi,zhanshi,qishi,fashi,saman,mushi,qiang,lieren,cike   = [],[],[],[],[],[],[],[],[]
zhiye_book = [wushi,zhanshi,qishi,fashi,saman,mushi,qiang,lieren,cike]

wushi_book_l      = ["影遁","静默之刃","连续打击","追踪","敏锐","闪现刺杀"]
zhanshi_book_l    = ["野蛮掠夺","野蛮反击","跃击","愤怒","投掷","振奋"]
qishi_book_l      = ["减速光环","冷静","信仰守护","圣光治愈","盾击","圣光之盾"]
fashi_book_l      = ["火球","火焰枷锁","变形","霜爆","焦土","连锁闪电"]
saman_book_l      = ["枯萎","三头","水元素","生命汲取","致命连接","伤害加深"]
mushi_book_l      = ["天使","生命暖流","鼓舞","辉光守卫","镇定光环","庇护"]
qiang_book_l      = ["连射","导弹","燃油弹","火炮","麻醉弹","冲击弹"]
cike_book_l       = ["毒液","毒镖","暗影波动","分身术","雾隐","隐身术"]
lieren_book_l     = ["撒网","猎犬","石化","变狼","自然囚笼","火焰标枪"]

# 石化术?坚守?防守光环?恢复光环?滚石
wushi_book_m      = ["折射","穿刺","压迫打击","追击","巨力打击","放逐"]
zhanshi_book_m    = ["疾风乱舞","士气","恐惧","嘲讽","滚石","坚守"]
qishi_book_m      = ["圣光审判","免疫","骑士冲击","无敌","圣光净化","防守光环"]
fashi_book_m      = ["时间结界","电力冲击","火焰喷吐","磁暴","极寒冰封","石化术"]
saman_book_m      = ["诅咒","恶魔之手","龙卷风","土元素","吞噬","沉默"]
mushi_book_m      = ["治愈术","复活术","喷泉","燃烧意志","群体治疗","恢复光环"]
qiang_book_m      = ["弹幕","狙击","激光","破甲弹","地雷","灼热弹"]
cike_book_m       = ["暗器散射","雾霾","暗影之舞","潜行术","交换","影子猎手"]
lieren_book_m     = ["变熊","野性激发","剧毒标枪","绝望之囚","自然视野","箭猪"]

# 嗜血？割喉？突袭？窒息之刃？铁钩？真空？进攻光环?地震
wushi_book_h      = ["闪电护盾","穿刺风暴","割裂","幻影斩击","遁地突刺"]
zhanshi_book_h    = ["挥击","神的力量","烧灼","毁灭","岩石皮肤"]
qishi_book_h      = ["圣光守护","惩戒","钢铁意志","圣光驱散","神盾"]
fashi_book_h      = ["暴风雪","寒冰咆哮","寒冬","流星火雨"]
saman_book_h      = ["崩溃","炎魔","虚弱","死亡生长"]
mushi_book_h      = ["守护天使","寂静守卫","烈炎重生","自然守护"]
qiang_book_h      = ["黑洞弹","核弹","轰炸","爆裂弹","火舌","防弹衣"]
cike_book_h       = ["突袭","多重影袭","割喉","窒息之刃","毒瘴","致残"]
lieren_book_h     = ["寒冰标枪","白熊","狮吼","铁钩","掩护","变豹"]

zhiye_def_l = [wushi_book_l, zhanshi_book_l, qishi_book_l, fashi_book_l, saman_book_l, mushi_book_l, qiang_book_l, lieren_book_l, cike_book_l]
zhiye_def_m = [wushi_book_m, zhanshi_book_m, qishi_book_m, fashi_book_m, saman_book_m, mushi_book_m, qiang_book_m, lieren_book_m, cike_book_m]
zhiye_def_h = [wushi_book_h, zhanshi_book_h, qishi_book_h, fashi_book_h, saman_book_h, mushi_book_h, qiang_book_h, lieren_book_h, cike_book_h]