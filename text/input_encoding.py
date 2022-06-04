
# All input symbols are defined here.
SYMBOLS = []

_pad = '_'
_eos = '~'

# Punctuations which maps to sp
sp_set = [".", "…", "--", "——", "~"] + ["...", "……"]
SYMBOLS += sp_set

# Punctuations which maps to pause
pau_set = [r"\/", "—", "&", "%", "$", "%", "·", "|", "-", "#", "@", "\\"]
SYMBOLS += sp_set

# Punctuations which is filtered
filter_set = [
    "『", "』", "《", "》", "<", ">", "「", "」", "(", ")", "[", "]", "{", "}", "\'",
    "\"", "‘", "’", "”", "“", "（", "）", "【", "】", "`"
]
SYMBOLS += filter_set

# Punctuations which maps to "，"
trans_set = [";", "；", "、"]
SYMBOLS += trans_set

# Punctuations-in-sentence which maps to "，"
in_sent_trans_set = ["！", "？", "。", "!", "?"]
SYMBOLS += trans_set

# convert english symbols to chinese symbols
symbol_set = [(i, 'sp') for i in sp_set] + \
    [(i, 'pau') for i in pau_set] + \
    [(i, '，') for i in trans_set] + \
    [(":", "："), (",", "，"), ("?", "？"), ("!", "！")]
symbol_dict = dict(symbol_set)
SYMBOLS += list(symbol_dict.keys())

# Short level pause
short_pauset = ["pau", "："]
SYMBOLS += short_pauset

# Middle level pause
middle_pauset = ["sp", "，"]
SYMBOLS += middle_pauset

# Long level pause
long_pauset = ["sil", "？", "！", "。"]
SYMBOLS += long_pauset

# alphabet for English.
alphabet_set = [
    "E0aa", "E0ae", "E0ah", "E0ao", "E0aw", "E0ax", "E0ay", "E0b", "E0ch",
    "E0d", "E0dh", "E0eh", "E0er", "E0ey", "E0f", "E0g", "E0h", "E0hh", "E0ih",
    "E0iy", "E0jh", "E0k", "E0l", "E0m", "E0n", "E0ng", "E0ow", "E0oy", "E0p",
    "E0r", "E0s", "E0sh", "E0t", "E0th", "E0uh", "E0uw", "E0v", "E0w", "E0y",
    "E0z", "E0zh"
]
# Code-switch phoneme set
phone_set = [_pad, _eos] + short_pauset + middle_pauset + long_pauset + \
    ["C0a", "C0ai", "C0air", "C0an", "C0ang", "C0angr", "C0anr", "C0ao",
     "C0aor", "C0ar", "C0b", "C0c", "C0ch", "C0d", "C0e", "C0ei",
     "C0eir", "C0en", "C0eng", "C0engr", "C0enr", "C0er", "C0f", "C0g",
     "C0h", "C0i", "C0ia", "C0ian", "C0iang", "C0iangr", "C0ianr",
     "C0iao", "C0iaor", "C0iar", "C0ie", "C0ier", "C0ii", "C0iii",
     "C0in", "C0ing", "C0ingr", "C0inr", "C0io", "C0iong", "C0iongr",
     "C0iou", "C0iour", "C0ir", "C0j", "C0k", "C0l", "C0m", "C0n",
     "C0ng", "C0o", "C0or", "C0ong", "C0ongr", "C0ou", "C0our", "C0p",
     "C0q", "C0r", "C0s", "C0sh", "C0t", "C0u", "C0ua", "C0uai",
     "C0uair", "C0uan", "C0uang", "C0uangr", "C0uanr", "C0uar", "C0uei",
     "C0ueir", "C0uen", "C0ueng", "C0uengr", "C0uenr", "C0uer", "C0uo",
     "C0uor", "C0ur", "C0v", "C0van", "C0vanr", "C0ve", "C0ver",
     "C0vn", "C0vnr", "C0vr", "C0x", "C0z", "C0zh", "C0iir", "C0iiir"] + alphabet_set
SYMBOLS += phone_set

# Code-switch tone set
tone_set = [_pad, _eos
            ] + ['0', '1', '2', '3', '4', '5', '6', '7', '10', '11', '12']

# Word category set
wordcateg_set = [_pad, _eos] + ['B', 'M', 'E', 'S']

# Prosody set for phoneme and punctuation
prosody_set = [_pad, _eos] + ['0', '1', '2', '3', '4']

# speaker
speaker_set = ['qiezi','tuo','hmbb', 'hfnn', 'xll','labixx','miaomiao','junhong','biaobei','SSB0009',
'SSB0011','SSB0012','SSB0016','SSB0018','SSB0033','SSB0038','SSB0043','SSB0057','SSB0073','SSB0080',
'SSB0112','SSB0122','SSB0133','SSB0139','SSB0145','SSB0149','SSB0193','SSB0197','SSB0200','SSB0241',
'SSB0246','SSB0261','SSB0267','SSB0273','SSB0287','SSB0288','SSB0299','SSB0307','SSB0309','SSB0315',
'SSB0316','SSB0323','SSB0338','SSB0339','SSB0341','SSB0342','SSB0354','SSB0366','SSB0375','SSB0379',
'SSB0380','SSB0382','SSB0385','SSB0393','SSB0394','SSB0395','SSB0407','SSB0415','SSB0426','SSB0427',
'SSB0434','SSB0435','SSB0470','SSB0482','SSB0502','SSB0534','SSB0535','SSB0539','SSB0544','SSB0565',
'SSB0570','SSB0578','SSB0588','SSB0590','SSB0594','SSB0599','SSB0601','SSB0603','SSB0606','SSB0607',
'SSB0609','SSB0614','SSB0623','SSB0629','SSB0631','SSB0632','SSB0666','SSB0668','SSB0671','SSB0686',
'SSB0693','SSB0700','SSB0702','SSB0710','SSB0711','SSB0716','SSB0717','SSB0720','SSB0723','SSB0736',
'SSB0737','SSB0746','SSB0748','SSB0749','SSB0751','SSB0758','SSB0760','SSB0762','SSB0778','SSB0780',
'SSB0784','SSB0786','SSB0794','SSB0809','SSB0817','SSB0822','SSB0851','SSB0863','SSB0871','SSB0887',
'SSB0913','SSB0915','SSB0919','SSB0935','SSB0966','SSB0987','SSB0993','SSB0997','SSB1000','SSB1001',
'SSB1002','SSB1008','SSB1020','SSB1024','SSB1050','SSB1055','SSB1056','SSB1064','SSB1072','SSB1091',
'SSB1096','SSB1100','SSB1108','SSB1110','SSB1115','SSB1125','SSB1126','SSB1131','SSB1135','SSB1136',
'SSB1138','SSB1161','SSB1176','SSB1187','SSB1197','SSB1203','SSB1204','SSB1215','SSB1216','SSB1218',
'SSB1219','SSB1221','SSB1239','SSB1253','SSB1274','SSB1302','SSB1320','SSB1322','SSB1328','SSB1340',
'SSB1341','SSB1365','SSB1366','SSB1377','SSB1382','SSB1383','SSB1385','SSB1392','SSB1393','SSB1399',
'SSB1402','SSB1408','SSB1431','SSB1437','SSB1448','SSB1452','SSB1457','SSB1555','SSB1563','SSB1567',
'SSB1575','SSB1585','SSB1593','SSB1607','SSB1624','SSB1625','SSB1630','SSB1650','SSB1670','SSB1684',
'SSB1686','SSB1699','SSB1711','SSB1728','SSB1739','SSB1745','SSB1759','SSB1781','SSB1782','SSB1806',
'SSB1809','SSB1810','SSB1828','SSB1831','SSB1832','SSB1837','SSB1846','SSB1863','SSB1872','SSB1878',
'SSB1891','SSB1902','SSB1918','SSB1935','SSB1939','SSB1956','baiye','bajiaosang','bijiasuodisgust','bijiasuohappiness',
'bijiasuosadness','dabai','dijing','dipianger','dongbeihua','ezhappiness','hjt','jingwen','jingwenandroid','jingwenios',
'meishaonv','mmt','nana','neikujun','nvhuangdi','nvwangdaren','nvzhubo','qiezianger','qieziexclam','qiezimoodsurprise',
'qiezinormal','qieziquest','qiezisadness','qiezixinwen','tai','tuozi','tuozibasemood','tuoziexclam','tuozihappiness',
'tuozimoodsurprise','tuoziomit','tuoziquest','xiaolang','xiaoli','xionghaizi','yingguo','yixuantai','yizhiqiang',
'yuanqishaonv1','yumengsichuan','yuxiang','zhang','zhubajie'
]
#speaker_set = ['qiezi','hmbb', 'hfnn', 'xll','labixx','junhong']

speaker_to_int = {}
int_to_speaker = {}
for idx, item in enumerate(speaker_set):
    speaker_to_int[item] = idx
    int_to_speaker[idx] = item

phone_to_int = {}
int_to_phone = {}
for idx, item in enumerate(phone_set):
    phone_to_int[item] = idx
    int_to_phone[idx] = item

tone_to_int = {}
int_to_tone = {}
for idx, item in enumerate(tone_set):
    tone_to_int[item] = idx
    int_to_tone[idx] = item

wordcateg_to_int = {}
int_to_wordcateg = {}
for idx, item in enumerate(wordcateg_set):
    wordcateg_to_int[item] = idx
    int_to_wordcateg[idx] = item

prosody_to_int = {}
prosodicword_to_int = {}
int_to_prosody = {}
for idx, item in enumerate(prosody_set):
    prosody_to_int[item] = idx
    if (item == '2' or item == '3' or item == '4'):
        prosodicword_to_int[item] = prosodicword_to_int['1']
    else:
        prosodicword_to_int[item] = idx
    int_to_prosody[idx] = item

pwpps_for_punc = {
    "pau": 2,
    "sp": 3,
    "sil": 4,
    "：": 2,
    "，": 3,
    "？": 4,
    "！": 4,
    "。": 4,
    "<unk>": 1
}

SYMBOLS = set(SYMBOLS)
