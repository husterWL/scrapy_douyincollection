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
    'Cookie': 'ttwid=1%7CZAY4sBJZ9XMM9pWoPGdIfeIC_wK-E54--NByW5m7ZbA%7C1701222597%7C25dca317841c31fef0767f2c992bd107aaecea394f129efdee386b00668110b0; dy_swidth=1707; dy_sheight=1067; bd_ticket_guard_client_web_domain=2; n_mh=MwAHPg-ldy5vjDZa2m-0Uz32UYqHWuYijCFkNHJW2Oo; LOGIN_STATUS=1; my_rd=2; store-region=cn-hb; store-region-src=uid; live_use_vvc=%22false%22; xgplayer_device_id=20755753164; xgplayer_user_id=350070612275; SEARCH_RESULT_LIST_TYPE=%22single%22; s_v_web_id=verify_lw4ytr4a_QsiMHKlA_83Ti_4IPA_ANLR_EXkPYxbhKbir; __live_version__=%221.1.2.250%22; passport_csrf_token=2a8211efdedcc6e1bd87ddfeea67baf4; passport_csrf_token_default=2a8211efdedcc6e1bd87ddfeea67baf4; passport_assist_user=CkE9dbkpw8g4ypvd1-GHKF2hg82KbBBUs64e72GW5PQ41YQPyKYjiAF4WLP-xRc1eaXbAxY9sXwZMDfZCLzIY3PDgxpKCjzxvkww1R4CUCHVxLQYG_CGETaErVHEjQjIXVeGEITjyNQprjggvy6LzloE9tU3wpE05IaWqsQbHQdAiKwQ7OLSDRiJr9ZUIAEiAQPxaCaK; sso_uid_tt=21c68bca312992adbb3c36ab3a48914d; sso_uid_tt_ss=21c68bca312992adbb3c36ab3a48914d; toutiao_sso_user=253f9bdd6ee7b34433e01cdde78ea32f; toutiao_sso_user_ss=253f9bdd6ee7b34433e01cdde78ea32f; sid_ucp_sso_v1=1.0.0-KGI0YzdhMmQwYTEwMmRlYzk4Mjk0MGVhMWRlMzU2YWQ1ZmRlZTc4ODUKHwj3jPDJhvSzAxCUzeayBhjvMSAMMIanmvgFOAZA9AcaAmhsIiAyNTNmOWJkZDZlZTdiMzQ0MzNlMDFjZGRlNzhlYTMyZg; ssid_ucp_sso_v1=1.0.0-KGI0YzdhMmQwYTEwMmRlYzk4Mjk0MGVhMWRlMzU2YWQ1ZmRlZTc4ODUKHwj3jPDJhvSzAxCUzeayBhjvMSAMMIanmvgFOAZA9AcaAmhsIiAyNTNmOWJkZDZlZTdiMzQ0MzNlMDFjZGRlNzhlYTMyZg; passport_auth_status=96034e0380a5de7c8e7ae4e71df04dff%2C; passport_auth_status_ss=96034e0380a5de7c8e7ae4e71df04dff%2C; uid_tt=184de6c4691a2722a89fb975ba7d8b30; uid_tt_ss=184de6c4691a2722a89fb975ba7d8b30; sid_tt=883738fda73570931db08c79259c6736; sessionid=883738fda73570931db08c79259c6736; sessionid_ss=883738fda73570931db08c79259c6736; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=c7ccc27b866beb8520f9ee1f4b9ce4ee; __security_server_data_status=1; sid_guard=883738fda73570931db08c79259c6736%7C1717151402%7C5183981%7CTue%2C+30-Jul-2024+10%3A29%3A43+GMT; sid_ucp_v1=1.0.0-KGQ5YWNlYjg2YzIyMGM1NzA0YTc3MDIzOTNiZTc2M2IyZjMyOGNiZDQKGwj3jPDJhvSzAxCqzeayBhjvMSAMOAZA9AdIBBoCbGYiIDg4MzczOGZkYTczNTcwOTMxZGIwOGM3OTI1OWM2NzM2; ssid_ucp_v1=1.0.0-KGQ5YWNlYjg2YzIyMGM1NzA0YTc3MDIzOTNiZTc2M2IyZjMyOGNiZDQKGwj3jPDJhvSzAxCqzeayBhjvMSAMOAZA9AdIBBoCbGYiIDg4MzczOGZkYTczNTcwOTMxZGIwOGM3OTI1OWM2NzM2; download_guide=%223%2F20240608%2F0%22; pwa2=%220%7C0%7C3%7C0%22; EnhanceDownloadGuide=%220_0_1_1718254078_1_1717838008%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAztmNcl6IuIaPLfdjJX73RKTy2X--P8GKi0z87YlP9hnpjlLrZrO3ZmRkpW74AdR2%2F1718294400000%2F0%2F0%2F1718256753239%22; __ac_nonce=0666d1909008dc6556c78; __ac_signature=_02B4Z6wo00f01BIcrCQAAIDA5HWlA.k27nQSPKiAAGLw0Fkd4jRttZYJOYWgNC2i6-10ygbytEDo5GQwEN.RoSfyXuGaU5m25f9WSfC44hlZJSM8em19Ezh0Okgv5N.8fCmqU-4v8YQk5Xf95e; douyin.com; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; csrf_session_id=c867ec8b94908cde46dfab4c866a53a8; strategyABtestKey=%221718425855.51%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.064%7D; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCS0tQQXpldEVkZGdGZXRwUzhkRUtONlVRb2JHelh5Q0xpdElTSUcvNkNsYmpwdTRDaGM1bUxUdEU2SkZtSERoZ1IzSkpGQmp3TGo4QUhScEVoa0V5dTQ9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; publish_badge_show_info=%220%2C0%2C0%2C1718425860566%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAztmNcl6IuIaPLfdjJX73RKTy2X--P8GKi0z87YlP9hnpjlLrZrO3ZmRkpW74AdR2%2F1718467200000%2F1718425868278%2F1718425855979%2F0%22; odin_tt=b0be0be0bdfcd1a5bde902c8aaf4c5399d5777a88f42ab9ac924cddda74ba27ddd69d998c1acf2919ee689176c1b2624d46e9a1427e5b28d29be832622331329; xg_device_score=7.676830700039698; msToken=OzkidAhtyf0bUo8iiT_esxboswEIY6vhmNODQ5OYrhJpiIIjEtyNCOzoGTQrf69pkzBa42S7Lhfq0DORKA7FD-SBqpH6FwtA1fVN3-BNzi4VbqQiC0OpTXlEs-G9Gw==; IsDouyinActive=false; passport_fe_beating_status=false'
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
