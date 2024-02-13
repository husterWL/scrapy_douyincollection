# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
import time
from selenium import webdriver
import json
import re
from selenium.webdriver.common.by import By

class DouyinSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class DouyinDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        with open ('cookies.txt', 'r') as f:
            self.cookies_list = json.load(f)
        if re.search(r'(?<=/)[^/]+(?=/[^/]*$)', request.url)[0] == 'user':
            # browser = webdriver.Edge()
            # browser.get(request.url)
            # time.sleep(20)
            # with open('cookies.txt','w') as f:
            #     f.write(json.dumps(browser.get_cookies()))
            # browser.close()
            
            spider.browser.get(request.url)
            spider.browser.delete_all_cookies()
            for cookie in self.cookies_list:
                spider.browser.add_cookie(cookie)
            spider.browser.refresh()
            time.sleep(10)
            # print(f"当前访问{request.url}")

            return HtmlResponse(url = spider.browser.current_url, body = spider.browser.page_source , encoding='utf-8')
        
        elif re.search(r'(?<=/)[^/]+(?=/[^/]*$)', request.url)[0] == 'video':
            options = webdriver.EdgeOptions()
            # options.add_argument('--headless')
            driver = webdriver.Edge(options = options)
            driver.get(request.url)
            driver.delete_all_cookies()
            for cookie in self.cookies_list:
                driver.add_cookie(cookie)
            driver.refresh()
            time.sleep(5)
            return HtmlResponse(url = spider.browser.current_url, body = spider.browser.page_source , encoding='utf-8')

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
