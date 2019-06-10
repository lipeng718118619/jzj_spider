# -*- coding: utf-8 -*-

# Scrapy settings for jzj_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jzj_spider'

SPIDER_MODULES = ['jzj_spider.spiders']
NEWSPIDER_MODULE = 'jzj_spider.spiders'


# # LOG CONFIG
# LOG_LEVEL = 'INFO'
# LOG_FILE = "/Users/honddy/PycharmProjects/log/jzj_spider.log"
#
# # picture download path
# # /www/wwwroot/default/uploads/allimg
# DOWNLOAD_PATH = "/Users/honddy/Pictures/jzj_spider"
# DOMAIN_NAME = 'http://demo.txjmw.com.cn'
#
# # DataBase Config
# DB_USER = 'root'
# DB_PASSWORD = 'root'
# DB_HOST = '127.0.0.1'
# DB_PORT = 3306
# DB_NAME = 'cyjm'
#
# # Redis 增量爬取
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379

# LOG CONFIG
LOG_LEVEL = 'INFO'
LOG_FILE = "/data/wwwlogs/jzj_spider.log"

# picture download path
# /www/wwwroot/default/uploads/allimg
DOWNLOAD_PATH = "/www/wwwroot/soucanyin.com/uploads/allimg"
DOMAIN_NAME = 'http://demo.txjmw.com.cn'

# DataBase Config
DB_USER = 'root'
DB_PASSWORD = 'kevinygn@163.com'
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_NAME = 'cyjm'

# Redis 增量爬取
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 9379
# 代理服务器
# PROXY_SERVER = ""
# 代理隧道验证信息
# PROXY_USER = ""
# PROXY_PASS = ""

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'jzj_spider (+http://www.yourdomain.com)'
# 爬取1000条关闭
CLOSESPIDER_ITEMCOUNT = 10000

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 5

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 5
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

SCHEDULER_PERSIST = True
# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'jzj_spider.middlewares.QjSpiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'jzj_spider.middlewares.SeleniumMiddleware': 1
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 200,
    'jzj_spider.pipelines.DBDataIsExist': 250,
    'jzj_spider.pipelines.RegularProcessingPipeline': 300,
    'jzj_spider.pipelines.IndustryTransferPipeline': 400,
    'jzj_spider.pipelines.InvestmentAmountPipeline': 500,
    # 'jzj_spider.pipelines.CityTransferPipeline': 600,
    'jzj_spider.pipelines.ProjectTypeTransfer': 650,
    'jzj_spider.pipelines.DownloadPicturePipeline': 700,
    'jzj_spider.pipelines.QjSpiderPipeline': 1000,
    'jzj_spider.pipelines.TagTransferPipeline': 1680
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USER_AGENT = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
]

INDUSTRY = {
    "东北麻辣烫": "125",
    "中式甜品": "82",
    "中餐": "4",
    "串串": "14",
    "串串香火锅": "135",
    "主题餐厅": "95",
    "乌龙茶": "140",
    "乳饮料": "79",
    "休闲咖啡厅": "144",
    "休闲食品": "170",
    "煎饼": "96",
    "饼": "96",
    "烧饼": "96",
    "馅饼": "96",
    "传统小吃": "96",
    "凉皮": "96",
    "混沌": "96",
    "羊肉汤": "96",
    "豆花": "96",
    "传统烘焙": "132",
    "保健酒": "182",
    "八大菜系": "86",
    "冒菜": "167",
    "冰淇淋": "10",
    "功能饮料": "78",
    "汤包": "88",
    "包子": "88",
    "北派火锅": "66",
    "南派火锅": "65",
    "卤味": "20",
    "卤肉饭": "20",
    "台式奶茶": "109",
    "咖啡": "16",
    "咖啡餐厅": "146",
    "商务咖啡厅": "145",
    "啤酒": "176",
    "啵啵鱼": "134",
    "回转火锅": "68",
    "地方特色": "169",
    "外卖": "18",
    "外卖便当": "107",
    "便当": "154",
    "大众麻辣烫": "126",
    "奶茶": "7",
    "寿司": "151",
    "寿司店": "151",
    "小吃": "5",
    "小吃技术培训": "99",
    "小吃车": "157",
    "香辣虾": "98",
    "麻辣小龙虾": "98",
    "小龙虾": "98",
    "龙虾": "98",
    "快餐": "6",
    "意式冰淇淋（硬）": "120",
    "成都麻辣烫": "123",
    "披萨": "155",
    "料理": "17",
    "新式奶茶": "110",
    "日式奶茶": "111",
    "日式甜品": "85",
    "日本料理": "149",
    "早餐": "93",
    "果汁冻糕": "121",
    "果茶": "74",
    "果酒": "179",
    "水吧": "75",
    "水果店": "75",
    "饺子": "89",
    "水饺": "89",
    "汉堡": "100",
    "海鲜": "166",
    "港式奶茶": "108",
    "港式甜品": "84",
    "火锅": "1",
    "火锅设备": "72",
    "炸鸡": "101",
    "烘焙": "12",
    "烤肉": "159",
    "烤鸭": "159",
    "烤猪蹄": "159",
    "烤鱼": "160",
    "烧烤": "21",
    "驴肉火烧": "21",
    "焖锅": "163",
    "香锅": "163",
    "干锅": "163",
    "麻辣香锅": "163",
    "煲仔饭": "103",
    "熟食": "162",
    "饭团": "162",
    "牛排": "104",
    "牛排杯": "104",
    "特色串串香": "136",
    "特色冰淇淋": "122",
    "特色卤味": "158",
    "咖啡店": "148",
    "特色咖啡店": "148",
    "特色奶茶": "113",
    "特色小吃": "97",
    "牛肉汤": "97",
    "牛杂": "97",
    "特色料理": "152",
    "年糕火锅": "71",
    "特色火锅": "71",
    "羊蝎子火锅": "71",
    "小火锅": "71",
    "特色菜系": "87",
    "砂锅": "87",
    "泰国菜": "87",
    "特色餐饮": "22",
    "特色饮品": "80",
    "特色麻辣烫": "127",
    "甜品": "82",
    "生煎": "90",
    "白茶": "138",
    "酒": "174",
    "白酒": "174",
    "盖饭": "102",
    "简餐": "154",
    "螺蛳粉": "115",
    "米粉": "115",
    "酸辣粉": "115",
    "粉": "115",
    "过桥米线": "116",
    "米线": "116",
    "鸭血粉丝": "116",
    "米酒": "178",
    "粉面": "9",
    "红茶": "141",
    "红酒": "175",
    "绿茶": "137",
    "美式冰淇淋（软）": "119",
    "肉蟹煲": "105",
    "自助火锅": "70",
    "火锅自助": "70",
    "自助餐": "168",
    "臭豆腐": "164",
    "花甲": "165",
    "花茶": "143",
    "茶叶": "15",
    "茶餐厅": "94",
    "葡萄酒": "180",
    "面包蛋糕": "129",
    "蛋糕": "129",
    "糕点": "129",
    "西式奶茶": "112",
    "西式烘焙": "133",
    "西式甜品": "83",
    "西餐": "19",
    "西餐厅": "153",
    "西饼": "130",
    "贡茶": "73",
    "酒吧": "147",
    "酒水": "173",
    "酸奶": "76",
    "酸菜鱼": "13",
    "重庆小面": "118",
    "重庆老火锅": "67",
    "重庆麻辣烫": "124",
    "铁板烧": "161",
    "锅贴": "91",
    "零食店": "171",
    "面包": "128",
    "面馆": "114",
    "热干面": "114",
    "面食": "114",
    "拉面": "114",
    "牛肉面": "114",
    "刀削面": "114",
    "韩国料理": "150",
    "食品": "172",
    "豆浆": "2",
    "饮品": "2",
    "粥": "2",
    "饮品设备": "81",
    "饼干": "131",
    "馄饨": "117",
    "馒头": "92",
    "肉夹馍": "92",
    "鱼火锅": "69",
    "石锅鱼": "69",
    "鲜榨果汁": "77",
    "鸡尾酒": "181",
    "鸡排": "8",
    "鸡排店": "8",
    "鸭脖": "156",
    "麻辣烫": "126",
    "黄焖鸡": "106",
    "黄焖鸡米粉": "106",
    "黄茶": "139",
    "黄酒": "177",
    "黑茶": "142"
}

CITY_CODE = {
    "118": {
        "aid": "118",
        "title": "北京",
        "parentid": "0",
        "pinyin": "beijing",
        "sort": "0"
    },
    "119": {
        "aid": "119",
        "title": "天津",
        "parentid": "0",
        "pinyin": "tianjin",
        "sort": "0"
    },
    "120": {
        "aid": "120",
        "title": "河北",
        "parentid": "0",
        "pinyin": "hebei",
        "sort": "0"
    },
    "121": {
        "aid": "121",
        "title": "山西",
        "parentid": "0",
        "pinyin": "shanxi",
        "sort": "0"
    },
    "122": {
        "aid": "122",
        "title": "内蒙古",
        "parentid": "0",
        "pinyin": "neimenggu",
        "sort": "0"
    },
    "123": {
        "aid": "123",
        "title": "辽宁",
        "parentid": "0",
        "pinyin": "liaoning",
        "sort": "0"
    },
    "124": {
        "aid": "124",
        "title": "吉林",
        "parentid": "0",
        "pinyin": "jilin",
        "sort": "0"
    },
    "125": {
        "aid": "125",
        "title": "黑龙江",
        "parentid": "0",
        "pinyin": "heilongjiang",
        "sort": "0"
    },
    "126": {
        "aid": "126",
        "title": "上海",
        "parentid": "0",
        "pinyin": "shanghai",
        "sort": "0"
    },
    "127": {
        "aid": "127",
        "title": "江苏",
        "parentid": "0",
        "pinyin": "jiangsu",
        "sort": "0"
    },
    "128": {
        "aid": "128",
        "title": "浙江",
        "parentid": "0",
        "pinyin": "zhejiang",
        "sort": "0"
    },
    "129": {
        "aid": "129",
        "title": "安徽",
        "parentid": "0",
        "pinyin": "anhui",
        "sort": "0"
    },
    "130": {
        "aid": "130",
        "title": "福建",
        "parentid": "0",
        "pinyin": "fujian",
        "sort": "0"
    },
    "131": {
        "aid": "131",
        "title": "江西",
        "parentid": "0",
        "pinyin": "jiangxi",
        "sort": "0"
    },
    "132": {
        "aid": "132",
        "title": "山东",
        "parentid": "0",
        "pinyin": "shandong",
        "sort": "0"
    },
    "133": {
        "aid": "133",
        "title": "河南",
        "parentid": "0",
        "pinyin": "hebei",
        "sort": "0"
    },
    "134": {
        "aid": "134",
        "title": "湖北",
        "parentid": "0",
        "pinyin": "hubei",
        "sort": "0"
    },
    "135": {
        "aid": "135",
        "title": "湖南",
        "parentid": "0",
        "pinyin": "hunan",
        "sort": "0"
    },
    "136": {
        "aid": "136",
        "title": "广东",
        "parentid": "0",
        "pinyin": "guangdong",
        "sort": "0"
    },
    "137": {
        "aid": "137",
        "title": "广西",
        "parentid": "0",
        "pinyin": "jiangxi",
        "sort": "0"
    },
    "138": {
        "aid": "138",
        "title": "海南",
        "parentid": "0",
        "pinyin": "hainan",
        "sort": "0"
    },
    "139": {
        "aid": "139",
        "title": "重庆",
        "parentid": "0",
        "pinyin": "chongqing",
        "sort": "0"
    },
    "140": {
        "aid": "140",
        "title": "四川",
        "parentid": "0",
        "pinyin": "sichuan",
        "sort": "0"
    },
    "141": {
        "aid": "141",
        "title": "贵州",
        "parentid": "0",
        "pinyin": "guizhong",
        "sort": "0"
    },
    "142": {
        "aid": "142",
        "title": "云南",
        "parentid": "0",
        "pinyin": "yunnan",
        "sort": "0"
    },
    "143": {
        "aid": "143",
        "title": "西藏",
        "parentid": "0",
        "pinyin": "xizhang",
        "sort": "0"
    },
    "144": {
        "aid": "144",
        "title": "陕西",
        "parentid": "0",
        "pinyin": "shaanxi",
        "sort": "0"
    },
    "145": {
        "aid": "145",
        "title": "甘肃",
        "parentid": "0",
        "pinyin": "gansu",
        "sort": "0"
    },
    "146": {
        "aid": "146",
        "title": "青海",
        "parentid": "0",
        "pinyin": "qinghai",
        "sort": "0"
    },
    "147": {
        "aid": "147",
        "title": "宁夏",
        "parentid": "0",
        "pinyin": "ningxia",
        "sort": "0"
    },
    "148": {
        "aid": "148",
        "title": "新疆",
        "parentid": "0",
        "pinyin": "xinjiang",
        "sort": "0"
    },
    "149": {
        "aid": "149",
        "title": "香港",
        "parentid": "0",
        "pinyin": "xianggang",
        "sort": "0"
    },
    "150": {
        "aid": "150",
        "title": "澳门",
        "parentid": "0",
        "pinyin": "aomen",
        "sort": "0"
    },
    "151": {
        "aid": "151",
        "title": "台湾",
        "parentid": "0",
        "pinyin": "taiwan",
        "sort": "0"
    },
    "152": {
        "aid": "152",
        "title": "美国",
        "parentid": "0",
        "pinyin": "meiguo",
        "sort": "0"
    },
    "153": {
        "aid": "153",
        "title": "英国",
        "parentid": "0",
        "pinyin": "yingguo",
        "sort": "0"
    },
    "154": {
        "aid": "154",
        "title": "欧洲",
        "parentid": "0",
        "pinyin": "ouzhou",
        "sort": "0"
    }
}

PROJECT_TYPES = {19: "火锅加盟项目",
                 23: "冰淇淋加盟项目",
                 28: "中餐加盟项目",
                 31: "甜品加盟项目",
                 35: "小吃加盟项目",
                 39: "快餐加盟项目",
                 42: "饮品加盟项目",
                 46: "咖啡加盟项目",
                 50: "西餐加盟项目",
                 54: "烘焙加盟项目",
                 57: "茶叶加盟项目",
                 61: "熟食加盟项目",
                 64: "料理加盟项目",
                 68: "面食加盟项目",
                 73: "鸡排店加盟项目",
                 76: "酒店加盟项目",
                 79: "快捷酒店加盟项目",
                 94: "早教加盟项目",
                 97: "英语加盟项目",
                 100: "潜能开发加盟项目",
                 103: "1对1辅导加盟项目",
                 106: "培训加盟项目",
                 109: "作文加盟项目",
                 112: "公务员培训加盟项目",
                 115: "留学加盟项目",
                 118: "IT教育加盟项目",
                 121: "机器人教育加盟项目",
                 124: "在线教育加盟项目",
                 134: "母婴用品加盟项目",
                 137: "婴儿游泳加盟项目",
                 141: "儿童乐园加盟项目",
                 145: "儿童玩具加盟项目",
                 149: "月子中心加盟项目",
                 153: "幼儿园加盟项目",
                 158: "床上用品加盟项目",
                 162: "家居布艺加盟项目",
                 166: "窗帘加盟项目",
                 170: "毛浴巾加盟项目",
                 174: "地毯加盟项目",
                 178: "竹纤维加盟项目",
                 183: "美体瘦身加盟项目",
                 187: "化妆品加盟项目",
                 191: "美容院加盟项目",
                 197: "产后恢复加盟项目",
                 201: "足疗汗蒸加盟项目",
                 205: "美发美甲加盟项目",
                 210: "香水加盟项目",
                 216: "橱柜加盟项目",
                 221: "地板加盟项目",
                 226: "门窗加盟项目",
                 232: "衣柜加盟品牌",
                 237: "卫浴加盟品牌",
                 241: "五金加盟项目",
                 246: "吊顶加盟项目",
                 251: "硅藻泥加盟项目",
                 255: "瓷砖加盟品牌",
                 259: "厨卫电器加盟项目",
                 263: "集成灶加盟品牌",
                 267: "灯饰加盟项目",
                 273: "新能源汽车加盟品牌",
                 277: "充电桩加盟品牌",
                 281: "汽车美容加盟项目",
                 285: "智能洗车设备加盟项目",
                 289: "车饰加盟项目",
                 293: "润滑油加盟品牌",
                 301: "空气净化加盟项目",
                 305: "污水处理加盟项目",
                 309: "固废处理加盟项目",
                 314: "洗衣干洗加盟项目",
                 320: "皮革护理加盟项目",
                 324: "干洗设备加盟项目",
                 328: "自助洗衣店加盟项目",
                 333: "珠宝加盟项目",
                 337: "饰品加盟项目",
                 341: "礼品加盟项目",
                 346: "服装加盟品牌",
                 353: "视健保健加盟项目",
                 357: "成人用品加盟项目",
                 361: "保健食品加盟项目",
                 365: "连锁药店加盟项目",
                 369: "保健用品加盟项目",
                 373: "大健康加盟项目",
                 377: "家政服务加盟项目",
                 381: "养老院加盟项目",
                 385: "月嫂加盟项目",
                 390: "白酒加盟项目",
                 394: "红酒加盟项目",
                 398: "便利店加盟项目",
                 402: "进口食品加盟项目",
                 407: "互联网金融加盟项目",
                 411: "互联网医疗加盟项目",
                 415: "智能制造加盟项目",
                 419: "无人机加盟项目",
                 423: "区块链加盟项目",
                 427: "SaaS软件加盟项目",
                 432: "生鲜超市加盟项目",
                 436: "无人超市加盟项目",
                 498: "素质教育加盟项目",
                 503: "ktv加盟项目",
                 507: "潮流加盟项目",
                 511: "基因检测加盟项目",
                 515: "数码加盟项目",
                 519: "宠物店加盟项目",
                 523: "微商加盟项目",
                 527: "影像加盟项目",
                 531: "外卖加盟项目",
                 536: "新零售加盟项目",
                 540: "物流加盟项目",
                 661: "餐饮加盟项目",
                 601: "内衣加盟品牌",
                 604: "童装加盟品牌",
                 608: "男装加盟品牌",
                 611: "户外加盟品牌",
                 614: "运动加盟品牌",
                 617: "休闲加盟品牌",
                 620: "孕妇装加盟品牌",
                 623: "鞋帽加盟品牌",
                 629: "皮具加盟品牌",
                 632: "配饰其他加盟品牌",
                 635: "箱包加盟品牌",
                 662: "教育加盟项目",
                 663: "母婴加盟项目",
                 664: "家纺加盟项目",
                 665: "美容加盟项目",
                 666: "建材加盟项目",
                 667: "家居加盟项目",
                 668: "汽车加盟项目",
                 669: "环保加盟项目",
                 670: "干洗加盟项目",
                 671: "珠宝饰品加盟项目",
                 673: "服装配饰加盟项目",
                 674: "医药保健加盟项目",
                 675: "零食酒水加盟项目",
                 676: "移动互联网加盟项目",
                 677: "零售服务加盟项目",
                 678: "特色行业加盟项目"
                 }
