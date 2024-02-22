import time
from selenium import webdriver
import json
import re
from selenium.webdriver.common.by import By
import requests
import os

with open('E:/Git_Repository/scrapy_douyincollection/douyin/douyin/spiders/link.txt', 'r') as f:
    for line in f:
        # print(line.strip())
        options = webdriver.EdgeOptions()
        # options.add_argument('--headless')
        driver = webdriver.Edge(options = options)
        url = line.strip()
        driver.get(url)
                    # driver.delete_all_cookies()
                    # for cookie in self.cookies_list:
                    #     driver.add_cookie(cookie)
                    # driver.refresh()
        # time.sleep(2)
                    # print('原始地址为-------------------------:', driver.find_element(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[2]/div/xg-video-container/video/source[2]').get_attribute('src'))
        try:
            link = driver.find_element(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[2]/div/xg-video-container/video/source[2]').get_attribute('src')
            filename = re.findall(r'/([^/]*$)', url)[0] + '.mp4'
            save_path = 'E:/Vedios/dy2/' + filename
            res = requests.get(link, stream = True)
            with open(save_path, 'wb') as f:
                for chunk in res.iter_content(chunk_size = 10240):
                    f.write(chunk)
        finally:
            pass
            # print(url)
            driver.close()