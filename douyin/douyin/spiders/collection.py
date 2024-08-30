import scrapy
from selenium import webdriver
# from selenium.webdriver.edge.options import Options
import time
from scrapy import signals
from pydispatch import dispatcher
from douyin.items import DouyinItem
import re
import copy

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
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # self.options.add_experimental_option("prefs", prefs)
        self.browser = webdriver.Edge(options = self.options)
        time.sleep(3)
        dispatcher.connect(self.close_browser, signals.spider_closed)
        # self.browser.execute_script()
        
    def close_browser(self, spider):
        self.browser.quit()

    def start_requests(self):
        
        yield scrapy.Request(self.start_urls[0], callback = self.parse_list)

    def parse_list(self, response):
        num = 0

        # beautylist = response.xpath('//*[@id="douyin-right-container"]/div[2]/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/ul//li')
        beautylist = response.xpath('//*[@id="douyin-right-container"]/div[2]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/ul//li')
        
        # //*[@id="douyin-right-container"]/div[2]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/ul/li[276]
        # //*[@id="douyin-right-container"]/div[2]/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/ul/li[240]/div/a
        # //*[@id="douyin-right-container"]/div[2]/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/ul/li[240]/div/a
        for beauty in beautylist:
            items = DouyinItem()
            num = num + 1
            if num == 355:
                break
            if beauty.xpath('./div/a/@href').get()[1:6] == 'video':
                items['beautylink'] = 'https://www.douyin.com' + beauty.xpath('./div/a/@href').get()
                
                # print(items['beautylink'])
                
                with open('E:/Git_Repository/scrapy_douyincollection/douyin/douyin/spiders/link.txt', 'a') as f:
                    f.write(items['beautylink'] + '\n')
            else:
                items['beautylink'] = 'https:' + beauty.xpath('./div/a/@href').get()
            # print('视频地址为：', items['beautylink'])
            #暂时只有前10个爬到,可以手动滚动，划到相应的位置
            # yield scrapy.Request(items['beautylink'], meta = {'video_note': copy.deepcopy(items)}, callback = self.parse_video)

        # print(len(beautylist))

    # def parse_video(self, response):
    #     items = response.meta['video_note']
    #     items['name'] = re.findall(r'/([^/]*$)', response.url)[0]
        # if re.search(r'(?<=/)[^/]+(?=/[^/]*$)', response.url)[0] == 'video':
            # items['videolink'] = response.xpath('//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[2]/div/xg-video-container/video/source[2]/@src').get()
            # print('视频原始地址是：', items['videolink'])     
            # yield items
        