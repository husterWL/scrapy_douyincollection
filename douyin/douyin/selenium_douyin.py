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
        # options = webdriver.EdgeOptions()
        # driver = webdriver.Edge(options = options)
        url = line.strip()
        filename = re.findall(r'/([^/]*$)', url)[0] + '.mp4'
        save_path = 'E:/Vedios/dy2/' + filename
        if os.path.exists(save_path) == False:
            options = webdriver.EdgeOptions()
            # options.add_argument('--headless')
            driver = webdriver.Edge(options = options)
            driver.get(url)
            # driver.delete_all_cookies()
            # for cookie in self.cookies_list:
            #     driver.add_cookie(cookie)
                # driver.refresh()
            time.sleep(1)
            # print('原始地址为-------------------------:', driver.find_element(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[2]/div/xg-video-container/video/source[2]').get_attribute('src'))
            
            try:
                link = driver.find_element(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[2]/div/xg-video-container/video/source[2]').get_attribute('src')
            
            except:
                
                driver.close()
                continue

            '''
            可以加个判断，如果文件存在，则不保存，如果文件不存在，则保存。
            '''
            

            while os.path.exists(save_path) == False:
                    # filename = re.findall(r'/([^/]*$)', url)[0] + str(time.time()) + '.mp4'
                    # save_path = 'E:/Vedios/dy2/' + filename
                res = requests.get(link, stream = True)
                with open(save_path, 'wb') as f:
                    for chunk in res.iter_content(chunk_size = 10240):
                        f.write(chunk)
        
        else:
            continue