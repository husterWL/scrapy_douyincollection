import scrapy
from selenium import webdriver
# from selenium.webdriver.edge.options import Options
import time
from scrapy import signals
from pydispatch import dispatcher
from douyin.items import DouyinItem

class CollectionSpider(scrapy.Spider):
    name = "collection"
    allowed_domains = ["douyin.com"]
    start_urls = ['https://www.douyin.com/user/MS4wLjABAAAAztmNcl6IuIaPLfdjJX73RKTy2X--P8GKi0z87YlP9hnpjlLrZrO3ZmRkpW74AdR2?showTab=favorite_collection']

    def __init__(self):
        
        self.options = webdriver.EdgeOptions()
        # edge_options.add_argument('--headless')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('useAutomationExtension', False)
        # 模拟请求，避免被反爬
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.options.add_experimental_option('detach', True)
        # 获取请求信息，避免被反爬
        prefs = {"profile.managed_default_content_settings.images": 2}
        self.options.add_experimental_option("prefs", prefs)
        self.browser = webdriver.Edge(options = self.options)
        time.sleep(3)
        dispatcher.connect(self.close_browser, signals.spider_closed)
        # self.browser.execute_script()
        
    def close_browser(self, spider):
        self.browser.quit()

    def start_requests(self):
        
        yield scrapy.Request(self.start_urls[0], callback = self.parse_list)

    def parse_list(self, response):
        pass
        beautylist = response.xpath('//*[@id="douyin-right-container"]/div[2]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/ul//li')
        for beauty in beautylist:
            items = DouyinItem()

            if beauty.xpath('./div/a/@href').get()[1:6] == 'video':
                items['beautylink'] = 'https://www.douyin.com' + beauty.xpath('./div/a/@href').get()
            else:
                items['beautylink'] = 'https:' + beauty.xpath('./div/a/@href').get()
            # print(items['beautylink'])
            #暂时只有前10个爬到