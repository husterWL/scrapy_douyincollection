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
    'Cookie': 'douyin.com; xg_device_score=7.796995563243618; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; ttwid=1%7CZAY4sBJZ9XMM9pWoPGdIfeIC_wK-E54--NByW5m7ZbA%7C1701222597%7C25dca317841c31fef0767f2c992bd107aaecea394f129efdee386b00668110b0; dy_swidth=1707; dy_sheight=1067; bd_ticket_guard_client_web_domain=2; passport_assist_user=CkGpoosZ5ElotqtyO7W-uXIFL2eEOsL7yPtsjfkBliLQXp4Eb4iTiDjn6b9H0vjXIvsnu3GkmGGJSNSdqNNdKo73gRpKCjwnKJn8ATpZVT6DVW0inpSYM__oGEtDVQRmYQZTVhUWMfP2vQELJ0YBDj-Sl3eY3eizY-6yPRGqET_Cc8YQrMfCDRiJr9ZUIAEiAQMel1qy; n_mh=MwAHPg-ldy5vjDZa2m-0Uz32UYqHWuYijCFkNHJW2Oo; sso_uid_tt=33c77a2b51d3e31c7156851bbaf08fa1; sso_uid_tt_ss=33c77a2b51d3e31c7156851bbaf08fa1; toutiao_sso_user=626e24e0bbb55c2e4cd38b8c1e5c079f; toutiao_sso_user_ss=626e24e0bbb55c2e4cd38b8c1e5c079f; LOGIN_STATUS=1; _bd_ticket_crypt_cookie=6a89f51413907b597b09f8fabb3f04b9; my_rd=2; store-region=cn-hb; store-region-src=uid; sid_ucp_v1=1.0.0-KDdlYzgwYTRhZmUxOTAxMGE2NjQ0YTBjMmNjYjYxZGU0NjFkY2U2MzcKGwj3jPDJhvSzAxCR15-sBhjvMSAMOAZA9AdIBBoCbGYiIDI2NWQ5ZGNmNDY3MzYwNTE5NWJhZjhjMWVkN2Q5MTVh; ssid_ucp_v1=1.0.0-KDdlYzgwYTRhZmUxOTAxMGE2NjQ0YTBjMmNjYjYxZGU0NjFkY2U2MzcKGwj3jPDJhvSzAxCR15-sBhjvMSAMOAZA9AdIBBoCbGYiIDI2NWQ5ZGNmNDY3MzYwNTE5NWJhZjhjMWVkN2Q5MTVh; uid_tt=33c77a2b51d3e31c7156851bbaf08fa1; uid_tt_ss=33c77a2b51d3e31c7156851bbaf08fa1; sid_tt=626e24e0bbb55c2e4cd38b8c1e5c079f; sessionid=626e24e0bbb55c2e4cd38b8c1e5c079f; sessionid_ss=626e24e0bbb55c2e4cd38b8c1e5c079f; live_use_vvc=%22false%22; __live_version__=%221.1.1.7489%22; passport_csrf_token=4b982dcd5155b7504ba2f2628520fe9d; passport_csrf_token_default=4b982dcd5155b7504ba2f2628520fe9d; vdg_r=%2219757_1%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAztmNcl6IuIaPLfdjJX73RKTy2X--P8GKi0z87YlP9hnpjlLrZrO3ZmRkpW74AdR2%2F1707062400000%2F0%2F1707016037700%2F0%22; publish_badge_show_info=%220%2C0%2C0%2C1707571211404%22; strategyABtestKey=%221707571211.767%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.088%7D; sid_ucp_sso_v1=1.0.0-KGZkZWE0MjZiNTJjODRkODIwNTY1YmJjNWM1MDJiOWU4Y2UyZDE2YTEKHwj3jPDJhvSzAxCd8J2uBhjvMSAMMIanmvgFOAZA9AcaAmxxIiA2MjZlMjRlMGJiYjU1YzJlNGNkMzhiOGMxZTVjMDc5Zg; ssid_ucp_sso_v1=1.0.0-KGZkZWE0MjZiNTJjODRkODIwNTY1YmJjNWM1MDJiOWU4Y2UyZDE2YTEKHwj3jPDJhvSzAxCd8J2uBhjvMSAMMIanmvgFOAZA9AcaAmxxIiA2MjZlMjRlMGJiYjU1YzJlNGNkMzhiOGMxZTVjMDc5Zg; sid_guard=626e24e0bbb55c2e4cd38b8c1e5c079f%7C1707571229%7C5184001%7CWed%2C+10-Apr-2024+13%3A20%3A30+GMT; pwa2=%220%7C0%7C2%7C0%22; __ac_nonce=065c798c100448dfab505; __ac_signature=_02B4Z6wo00f01cmUF3QAAIDCdGoLMjouGD3JtBPAABekne59iG6idDbQVT0XKDhP37BgEURrm7oTe0UK5TfsRtVqeCfjoavSldyaeiQA5qrQyOmXEFnULAMYYcFTHeXrnFvp3FaDv5ryTyxH1c; csrf_session_id=b3fcd38c5419ddfbdba832433937ab58; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAztmNcl6IuIaPLfdjJX73RKTy2X--P8GKi0z87YlP9hnpjlLrZrO3ZmRkpW74AdR2%2F1707580800000%2F0%2F1707579580738%2F0%22; download_guide=%223%2F20240210%2F0%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCS0tQQXpldEVkZGdGZXRwUzhkRUtONlVRb2JHelh5Q0xpdElTSUcvNkNsYmpwdTRDaGM1bUxUdEU2SkZtSERoZ1IzSkpGQmp3TGo4QUhScEVoa0V5dTQ9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=1sCn268Op8XY4v0pBSSRfFHWG0CuUA_rAOqrs93Hgy5ayZtP9dB2FgFZEKLmv4Pc1-QYmMAqW0M3jIZR1P2Sw80CASqO6y4Kz4XZy5ZdN2Hp1-gYCRIVicCLCJFu; odin_tt=2f5b0aee7bf9cf0827626a3635f0782bb2532377e7c178602c035359569d012304998206df86a1f93378c71d0121a618a9eecc951af236ef30391978ec7f5a5fce94b740b6a34045f90c4018fa7d7ceb; tt_scid=6hU4FAbHR9wP-NkckB5xXWl457TGkQ4HyHGokJ.lGBF-3ZvKOJB6q3ROcuJ0WpFR3b50; msToken=ePI-kxnhCHpjbwvN0JLbf6-puKx6d8QtZW9TJ-eN3yugrlXIl7RGO0VQrCgcOUi6mPPFkbV2CvPb3TvoRoyI7Njvj0LcXBYUpR8goZwIlMo8CK6VGyyqjkgCyS_V; IsDouyinActive=false; passport_fe_beating_status=false'
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
