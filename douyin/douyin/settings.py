# Scrapy settings for douyin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "douyin"

SPIDER_MODULES = ["douyin.spiders"]
NEWSPIDER_MODULE = "douyin.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'Cookie': 'ttwid=1%7CZAY4sBJZ9XMM9pWoPGdIfeIC_wK-E54--NByW5m7ZbA%7C1701222597%7C25dca317841c31fef0767f2c992bd107aaecea394f129efdee386b00668110b0; dy_swidth=1707; dy_sheight=1067; bd_ticket_guard_client_web_domain=2; n_mh=MwAHPg-ldy5vjDZa2m-0Uz32UYqHWuYijCFkNHJW2Oo; sso_uid_tt=33c77a2b51d3e31c7156851bbaf08fa1; sso_uid_tt_ss=33c77a2b51d3e31c7156851bbaf08fa1; toutiao_sso_user=626e24e0bbb55c2e4cd38b8c1e5c079f; toutiao_sso_user_ss=626e24e0bbb55c2e4cd38b8c1e5c079f; LOGIN_STATUS=1; my_rd=2; store-region=cn-hb; store-region-src=uid; uid_tt=33c77a2b51d3e31c7156851bbaf08fa1; uid_tt_ss=33c77a2b51d3e31c7156851bbaf08fa1; sid_tt=626e24e0bbb55c2e4cd38b8c1e5c079f; sessionid=626e24e0bbb55c2e4cd38b8c1e5c079f; sessionid_ss=626e24e0bbb55c2e4cd38b8c1e5c079f; live_use_vvc=%22false%22; xgplayer_device_id=20755753164; xgplayer_user_id=350070612275; passport_assist_user=CkEsw0LCaUNlvk0pwNkiGYukN1BwPMliojklzHWc1FZ3tUy20H-_8ED-rIwRE7Fv-Co3eLySR2naYBvT8sMZyb6I0hpKCjy2SePi_yU8dZRO4ownb-qfGZbmUhy31Bmm0VDO5bslO9j_EVRrTmsua3-rIcm3bhTYsnj_VntvxopaH6IQprrJDRiJr9ZUIAEiAQNBb4-F; sid_ucp_v1=1.0.0-KDIwZDI0MzgyYWM3OGQwZDFiY2NhYzBiY2EwZGRmNjMxMTZlZjY4MGIKIQj3jPDJhvSzAxDBiLiuBhjvMSAMMIanmvgFOAZA9AdIBBoCaGwiIDYyNmUyNGUwYmJiNTVjMmU0Y2QzOGI4YzFlNWMwNzlm; ssid_ucp_v1=1.0.0-KDIwZDI0MzgyYWM3OGQwZDFiY2NhYzBiY2EwZGRmNjMxMTZlZjY4MGIKIQj3jPDJhvSzAxDBiLiuBhjvMSAMMIanmvgFOAZA9AdIBBoCaGwiIDYyNmUyNGUwYmJiNTVjMmU0Y2QzOGI4YzFlNWMwNzlm; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=d037ba08722d1a38c41cfde8cbe4a0cf; __security_server_data_status=1; __live_version__=%221.1.1.9068%22; passport_csrf_token=c918ae1640552ec0bae9ea05458700ce; passport_csrf_token_default=c918ae1640552ec0bae9ea05458700ce; sid_ucp_sso_v1=1.0.0-KGM5ZGM1NjI5MDM5OGE4ZWM4ZjA0ODQ2MzM4ZTMxMzc4YTMwZDlhYWYKIQj3jPDJhvSzAxCfvLSwBhjvMSAMMIanmvgFOAZA9AdIBBoCaGwiIDYyNmUyNGUwYmJiNTVjMmU0Y2QzOGI4YzFlNWMwNzlm; ssid_ucp_sso_v1=1.0.0-KGM5ZGM1NjI5MDM5OGE4ZWM4ZjA0ODQ2MzM4ZTMxMzc4YTMwZDlhYWYKIQj3jPDJhvSzAxCfvLSwBhjvMSAMMIanmvgFOAZA9AdIBBoCaGwiIDYyNmUyNGUwYmJiNTVjMmU0Y2QzOGI4YzFlNWMwNzlm; sid_guard=626e24e0bbb55c2e4cd38b8c1e5c079f%7C1712135712%7C5184000%7CSun%2C+02-Jun-2024+09%3A15%3A12+GMT; pwa2=%220%7C0%7C3%7C0%22; publish_badge_show_info=%221%2C0%2C0%2C1712482900682%22; download_guide=%223%2F20240407%2F0%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.075%7D; GlobalGuideTimes=%221712647980%7C0%22; tt_scid=jJQ9hLjH3eiLr0IWU65A8Fn1qZUSQbH0ZgwVJqyy1K3go.YsG3RwKuFQuPn2DkYua9d3; msToken=ntzQ64vXHqL19erQ19TECcV7s531ME0zrctsuSfNBT9cGmoSaMAvbFPlCKK02Tic6pORhN2OltTF4wrQo-PfFWBF3y3WWC2-OsSvgTidhaQmuZUFrfuwUZgqHjukxQ==; strategyABtestKey=%221712843764.072%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A1%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAztmNcl6IuIaPLfdjJX73RKTy2X--P8GKi0z87YlP9hnpjlLrZrO3ZmRkpW74AdR2%2F1712851200000%2F0%2F0%2F0%22; __ac_nonce=06617f7e5008238c46f91; __ac_signature=_02B4Z6wo00f01hV1aAgAAIDC4xxhLCLVJ1YVVWyAAONYB6C4Qn3UWj6qSADhONGXhvLOnMUGSy.ZI3lXHQGZr10KPHuj4E-eRPSbu662t21XaCZACgFCJ3vQ-pZkzvbefuq3XRV1f05j7lA143; douyin.com; xg_device_score=7.60271738116804; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; csrf_session_id=cc74e68db4041c8bdf47de4d59a82d12; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAztmNcl6IuIaPLfdjJX73RKTy2X--P8GKi0z87YlP9hnpjlLrZrO3ZmRkpW74AdR2%2F1712851200000%2F0%2F1712846812384%2F0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCS0tQQXpldEVkZGdGZXRwUzhkRUtONlVRb2JHelh5Q0xpdElTSUcvNkNsYmpwdTRDaGM1bUxUdEU2SkZtSERoZ1IzSkpGQmp3TGo4QUhScEVoa0V5dTQ9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; odin_tt=6f247f1d0050fb3a1a844c7ab090acd2f26fae2c7aba5be2b0fa34e644493d8dac93d282bd4a98845c0725303fca48ffde4c03e81a62c87ad066b4aa80f72132; msToken=j9t9u7TTbKsBNxomKoqsripQQ0YxURWGD_AC3WrJuMQ9qp5WPKxzFzAaWK7IXPjRpZHuZHjo0BDJToUmMje0shWzU7vZY9JErefY3jj3_B8iGlyuEAH3sf_YJ-5Ebg==; IsDouyinActive=false; passport_fe_beating_status=false'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "douyin.middlewares.DouyinSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "douyin.middlewares.DouyinDownloaderMiddleware": 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "douyin.pipelines.videodownloadpipeline": 300,
}
FILES_STORE = 'E:/Vedios/dy2'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
