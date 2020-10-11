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
gift_sg = []    # 上古馈赠
gift_yg = []    # 远古馈赠
other   = []

zhiye_des = ["武士","战士","骑士","法师","萨满","牧师","枪手","猎人","刺客"]

wushi,zhanshi,qishi,fashi,saman,mushi,qiang,lieren,cike   = [],[],[],[],[],[],[],[],[]
zhiye_book = [wushi,zhanshi,qishi,fashi,saman,mushi,qiang,lieren,cike]

# 减速光环=聚焦 镇定光环=洁净
wushi_book_l      = ["影遁","静默之刃","连续打击","追踪","敏锐","闪现刺杀"]
zhanshi_book_l    = ["野蛮掠夺","野蛮反击","跃击","愤怒","投掷","振奋"]
qishi_book_l      = ["减速光环","冷静","信仰守护","圣光治愈","盾击","圣光之盾"]
fashi_book_l      = ["火球","火焰枷锁","变形","霜爆","焦土","连锁闪电"]
saman_book_l      = ["枯萎","三头","水元素","生命汲取","致命连接","伤害加深"]
mushi_book_l      = ["天使","生命暖流","鼓舞","辉光守卫","镇定光环","庇护"]
qiang_book_l      = ["连射","导弹","燃油弹","火炮","麻醉弹","冲击弹"]
cike_book_l       = ["毒液","毒镖","暗影波动","分身术","雾隐","隐身术"]
lieren_book_l     = ["撒网","猎犬","石化","变狼","自然囚笼","火焰标枪"]

# 石化术?坚守=震慑 防守光环?恢复光环?滚石
wushi_book_m      = ["折射","穿刺","压迫打击","追击","巨力打击","放逐"]
zhanshi_book_m    = ["疾风乱舞","士气","恐惧","嘲讽","滚石","坚守"]
qishi_book_m      = ["圣光审判","免疫","骑士冲击","无敌","圣光净化","防守光环"]
fashi_book_m      = ["时间结界","电力冲击","火焰喷吐","磁暴","极寒冰封","石化术"]
saman_book_m      = ["诅咒","恶魔之手","龙卷风","土元素","吞噬","沉默"]
mushi_book_m      = ["治愈术","复活术","喷泉","燃烧意志","群体治疗","恢复光环"]
qiang_book_m      = ["弹幕","狙击","激光","破甲弹","地雷","灼热弹"]
cike_book_m       = ["暗器散射","雾霾","暗影之舞","潜行术","交换","影子猎手"]
lieren_book_m     = ["变熊","野性激发","剧毒标枪","绝望之囚","自然视野","箭猪"]

# 嗜血？割喉？突袭(闪击) 窒息之刃(虚脱) 
# 铁钩(弹跳) 真空=反向 进攻光环(涤荡光环) 地震
wushi_book_h      = ["闪电护盾","窒息之刃","割裂","穿刺风暴","幻影斩击","遁地突刺"]
zhanshi_book_h    = ["挥击","岩石皮肤","神的力量","烧灼","毁灭","地震"]
qishi_book_h      = ["惩戒","刚铁意志","神盾","圣光驱散","圣光守护","进攻光环"]
fashi_book_h      = ["雷神之力","流星火雨","暴风雪","寒冰咆哮","寒冬","真空"]
saman_book_h      = ["炎魔","死亡生长","陨石","虚弱","崩溃","嗜血"]
mushi_book_h      = ["治疗光波","烈炎重生","守护天使","寂静守卫","自然守护","净化术"]
qiang_book_h      = ["黑洞弹","爆裂弹","火舌","核弹","轰炸","防弹衣"]
lieren_book_h     = ["白熊","狮吼","变豹","寒冰标枪","铁钩","掩护"]
cike_book_h       = ["暗器风暴","毒瘴","割喉","突袭","多重影袭","致残"]
wushi_s           = ["打击系","打击系","打击系","狂暴系","狂暴系","狂暴系"]
zhanshi_s         = ["战斗系","战斗系","战斗系","野蛮系","野蛮系","野蛮系"]
qishi_s           = ["信仰系","信仰系","信仰系","圣光系","圣光系","圣光系"]
fashi_s           = ["元素系","元素系","元素系","法术系","法术系","法术系"]
saman_s           = ["召唤系","召唤系","召唤系","黑暗系","黑暗系","黑暗系"]
mushi_s           = ["庇护系","庇护系","庇护系","虔诚系","虔诚系","虔诚系"]
qiang_s           = ["射击系","射击系","射击系","科技系","科技系","科技系"]
lieren_s          = ["自然系","自然系","自然系","捕猎系","捕猎系","捕猎系"]
cike_s            = ["刺击系","刺击系","刺击系","暗影系","暗影系","暗影系"]

zhiye_def_l = [wushi_book_l, zhanshi_book_l, qishi_book_l, fashi_book_l, saman_book_l, mushi_book_l, qiang_book_l, lieren_book_l, cike_book_l]
zhiye_def_m = [wushi_book_m, zhanshi_book_m, qishi_book_m, fashi_book_m, saman_book_m, mushi_book_m, qiang_book_m, lieren_book_m, cike_book_m]
zhiye_def_h = [wushi_book_h, zhanshi_book_h, qishi_book_h, fashi_book_h, saman_book_h, mushi_book_h, qiang_book_h, lieren_book_h, cike_book_h]
zhiye_s     = [wushi_s, zhanshi_s, qishi_s, fashi_s, saman_s, mushi_s, qiang_s, lieren_s, cike_s]

jianshi_tt      = ["推进盔", "推进铠", "推进盾", "推进手套", "推进护靴", "勇士剑"]
mofa_tt         = ["灵动帽", "灵动法袍", "灵动之书", "灵动护手", "灵动鞋", "灵动杖"]
sheshou_tt      = ["防卫皮帽", "复合甲", "防卫剑", "防卫手套", "防卫鞋", "复合弓"]
tt_za           = ["金项链", "白银腰带", "精皮水袋"]

tt_zhuang_def   = [jianshi_tt, mofa_tt, sheshou_tt]

wushi_tz        = ["嵌甲盔", "镶嵌甲", "覆铁盾", "嵌甲护胫", "嵌甲护手", "冷刃矛"]
zhanshi_tz      = ["重型盔", "巨型甲", "重型盾", "重型护胫", "重型手套", "巨型斧"]
qishi_tz        = ["符纹盔", "符纹甲", "符纹盾", "符纹靴", "符纹护手", "符纹权杖"]
fashi_tz        = ["魔法帽", "魔法服", "魔法大典", "魔法鞋", "魔法手套", "魔法棍"]
saman_tz        = ["黑暗面具", "黑暗之衣", "黑暗之书", "黑暗鞋", "黑暗护腕", "羊头杖"]
mushi_tz        = ["祈祷帽", "祈祷服", "祈祷经文", "祈祷鞋", "祈祷手套", "祈祷杖"]
qiang_tz        = ["毡帽", "层压甲", "花剑", "军用靴", "军用护手", "膛线枪"]
lieren_tz       = ["重皮帽", "重皮甲", "锐利猎刀", "重皮靴", "重皮手套", "重标枪"]
cike_tz         = ["硬皮面罩", "硬皮甲", "锋利匕首", "硬皮护胫", "硬皮束手", "三角镖"]
tz_za           = ["秘银水壶", "秘银束带", "魔金项链"]

tz_zhuang_def = [wushi_tz, zhanshi_tz, qishi_tz, fashi_tz, saman_tz, mushi_tz, qiang_tz, lieren_tz, cike_tz]

jianshi_ft      = ["坚固盔", "坚固铠", "坚固盾", "坚固护腕", "坚固护靴", "斩铁剑"]
mofa_ft         = ["诡秘之帽", "诡秘法袍", "诡秘之书", "诡秘手套", "诡秘之鞋", "诡秘杖"]
sheshou_ft      = ["圆月之帽", "圆月甲", "寒铁剑", "圆月手套", "圆月鞋", "弯月弓"]
ft_za           = ["水晶吊坠", "镶金腰带", "密纹水袋"]

ft_zhuang_def   = [jianshi_ft, mofa_ft, sheshou_ft]