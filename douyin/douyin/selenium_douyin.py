import time
from selenium import webdriver
import json
import re
from selenium.webdriver.common.by import By
import requests
import os

with open('E:/Git_Repository/scrapy_douyincollection/cookie.txt', 'r') as cookie:
    cookielist = json.load(cookie)

headers = {
    'authority': 'www.douyin.com',
    'method': 'GET',
    'scheme': 'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Cookie': 'dy_swidth=1707; dy_sheight=1067; bd_ticket_guard_client_web_domain=2; n_mh=MwAHPg-ldy5vjDZa2m-0Uz32UYqHWuYijCFkNHJW2Oo; LOGIN_STATUS=1; my_rd=2; store-region=cn-hb; store-region-src=uid; live_use_vvc=%22false%22; xgplayer_device_id=20755753164; xgplayer_user_id=350070612275; SEARCH_RESULT_LIST_TYPE=%22single%22; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; UIFID_TEMP=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4f32f18448adb07d6570627193de18b3dbab0666da8e59d0ae53bf588959cf689877c0432f38e5dfd759da3e1d99e65752692a4d99cf94ceb989eb933c03885d7; fpk1=U2FsdGVkX1+wlKLuPUiMBkL65O5LwgVZZgxsYKUZIeXPwhz7xbUXJev0uUAX7Zk063XoG7anX2y085fmemtoUA==; fpk2=d94a27a56e6a143d4c900b9014d6ba5d; UIFID=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4f32f18448adb07d6570627193de18b3dbab0666da8e59d0ae53bf588959cf689e1b73b8c259468029552d61687d4e82fd87171fbd9ff98bfa25a689317f915258f41d457127d176d963cd95ef36b88dde672122faf6230b6ca6b8305976f374c8fd8cbb54a9fb4439cc5980f241ff6e0cc6d247e09751e0b74dde9116e95a46a90c5b1467d2ffe5a38ef7d3ed25e0eeaaa59d90e2b4127f82f736fd8bd6c6959; s_v_web_id=verify_lyn0hwon_8ZNIjG1n_ajtY_47rv_8phB_BaSnHFJsm1MA; __live_version__=%221.1.2.2148%22; ttwid=1%7CZAY4sBJZ9XMM9pWoPGdIfeIC_wK-E54--NByW5m7ZbA%7C1721573286%7C33fa271f7324bca9ef2141ddf52b8edcfe4b289092dffa8c7efb84cec766040e; passport_csrf_token=0964f3e85b6232bfcd02658d546b6e8c; passport_csrf_token_default=0964f3e85b6232bfcd02658d546b6e8c; is_staff_user=false; d_ticket=ab5c43ed0f45a0942481cf7d3dd9c426cb738; passport_assist_user=CkHz-_qkAeiZeKYqKFcMge1pTZUiMinlwQnytFOPkh5uRN-1WCksKu1b6yB65W2aeKvb4e_nykoOb_C2ZjIo3zIf5xpKCjxF6HeQcSKua_upReIu204rkulV-TgUHXrPKcwWssvvbga0-1rbw0e9BVP5cg9GEZ35vzmcpN41hr24dQ4QhJnYDRiJr9ZUIAEiAQM7xEmV; sso_uid_tt=2ab48d1c7628e67f846cba626e99677b; sso_uid_tt_ss=2ab48d1c7628e67f846cba626e99677b; toutiao_sso_user=9219f19c7295a22e51660bf58e57f727; toutiao_sso_user_ss=9219f19c7295a22e51660bf58e57f727; sid_ucp_sso_v1=1.0.0-KDNlYjBlMWY2Y2M1NjkwYzUxM2MxZWY1YjRmZjIyM2M5MTExMjIyNmIKIQj3jPDJhvSzAxDBoKy1BhjvMSAMMIanmvgFOAVA-wdIBhoCaGwiIDkyMTlmMTljNzI5NWEyMmU1MTY2MGJmNThlNTdmNzI3; ssid_ucp_sso_v1=1.0.0-KDNlYjBlMWY2Y2M1NjkwYzUxM2MxZWY1YjRmZjIyM2M5MTExMjIyNmIKIQj3jPDJhvSzAxDBoKy1BhjvMSAMMIanmvgFOAVA-wdIBhoCaGwiIDkyMTlmMTljNzI5NWEyMmU1MTY2MGJmNThlNTdmNzI3; uid_tt=6bd85bb6809fea52b53e96d3e5931157; uid_tt_ss=6bd85bb6809fea52b53e96d3e5931157; sid_tt=e8cba7bb35cff2b92e864f814fbc952b; sessionid=e8cba7bb35cff2b92e864f814fbc952b; sessionid_ss=e8cba7bb35cff2b92e864f814fbc952b; _bd_ticket_crypt_cookie=bb70c0d90d6426df2256e9beb5fe46ce; sid_guard=e8cba7bb35cff2b92e864f814fbc952b%7C1722486855%7C5183997%7CMon%2C+30-Sep-2024+04%3A34%3A12+GMT; sid_ucp_v1=1.0.0-KDZkNjdjMDk2ODM1NTM3NjZhNGUwY2Q3ZTA2YTlhYTgwM2YyYjFmYzkKGwj3jPDJhvSzAxDHoKy1BhjvMSAMOAVA-wdIBBoCbHEiIGU4Y2JhN2JiMzVjZmYyYjkyZTg2NGY4MTRmYmM5NTJi; ssid_ucp_v1=1.0.0-KDZkNjdjMDk2ODM1NTM3NjZhNGUwY2Q3ZTA2YTlhYTgwM2YyYjFmYzkKGwj3jPDJhvSzAxDHoKy1BhjvMSAMOAVA-wdIBBoCbHEiIGU4Y2JhN2JiMzVjZmYyYjkyZTg2NGY4MTRmYmM5NTJi; publish_badge_show_info=%220%2C0%2C0%2C1723296654074%22; EnhanceDownloadGuide=%220_0_5_1722921541_4_1723433000%22; pwa2=%220%7C0%7C3%7C0%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; strategyABtestKey=%221723797116.609%22; download_guide=%223%2F20240816%2F0%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAztmNcl6IuIaPLfdjJX73RKTy2X--P8GKi0z87YlP9hnpjlLrZrO3ZmRkpW74AdR2%2F1723824000000%2F0%2F0%2F1723816223134%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.16%7D; __ac_nonce=066bf659a009a4a3b23d8; __ac_signature=_02B4Z6wo00f01tDzMCAAAIDCJpo5Bq.lnJbQ0zSAANKQ1hfFBExQ.ZQWeq..t6bkZplge-8BDqsr9RPeXF5DzHPkO4gCt4449Loe-vtlwGGpW-3McYwqjywZ2LyLg3oCTLs.-uLLIfTLZptsbd; douyin.com; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; csrf_session_id=1829b4a95d52dbe9d463a5af1b12cb04; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCS0tQQXpldEVkZGdGZXRwUzhkRUtONlVRb2JHelh5Q0xpdElTSUcvNkNsYmpwdTRDaGM1bUxUdEU2SkZtSERoZ1IzSkpGQmp3TGo4QUhScEVoa0V5dTQ9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAztmNcl6IuIaPLfdjJX73RKTy2X--P8GKi0z87YlP9hnpjlLrZrO3ZmRkpW74AdR2%2F1723824000000%2F0%2F1723819427699%2F0%22; home_can_add_dy_2_desktop=%221%22; odin_tt=ee1c5a1dcf1d589b15711109142861d08643df1dcf6ff4e8fc1dca9c88e2a8d18e49730adfbe0bbb733cebba4ac08eaa; xg_device_score=7.983585126412278; IsDouyinActive=false; passport_fe_beating_status=false',
    'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'Referer': 'https://www.douyin.com/',
}

with open('E:/Git_Repository/scrapy_douyincollection/douyin/douyin/spiders/link.txt', 'r') as f:
    for line in f:
        # print(line.strip())
        # options = webdriver.EdgeOptions()
        # driver = webdriver.Edge(options = options)
        url = line.strip()
        filename = re.findall(r'/([^/]*$)', url)[0] + '.mp4'
        save_path = 'E:/Vedios/dy3/' + filename
        if os.path.exists(save_path) == False:
            
            # print(url)
            
            options = webdriver.EdgeOptions()

            options.add_argument('--headless')
            options.add_argument('--mute-audio')
            options.add_argument('--disable-blink-features')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option('useAutomationExtension', False)
            # options.add_experimental_option('excludeSwitches', ['enable-automation'])
            options.add_experimental_option('detach', True)


            driver = webdriver.Edge(options = options)

            driver.get(url)

            driver.delete_all_cookies()
            for cook in cookielist:
                driver.add_cookie(cook)

            driver.refresh()

            time.sleep(1)


            # print('原始地址为-------------------------:', driver.find_element(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[2]/div/xg-video-container/video/source[2]').get_attribute('src'))
            with open('E:/Git_Repository/scrapy_douyincollection/cookie.txt', 'w') as c:
                c.write(json.dumps(driver.get_cookies())) #大概率是因为无法转换为json序列
                # json.dump(json.dumps(driver.get_cookies), c)

            try:
                # link = driver.find_element(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div/div[1]/div[2]/div/xg-video-container/video/source[3]').get_attribute('src')
                link = driver.find_element(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[2]/div/xg-video-container/video/source[3]').get_attribute('src')
                # //*[@id="douyin-right-container"]/div[2]/div/div[1]/div[2]/div/xg-video-container/video/source[3]
                # //*[@id="douyin-right-container"]/div[2]/div/div[1]/div[2]/div/xg-video-container/video/source[3]
                # //*[@id="douyin-right-container"]/div[2]/div/div[1]/div[2]/div/xg-video-container/video/source[3]

            except:
                driver.close()
                continue
            # link = driver.find_element(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div/div[1]/div[2]/div/xg-video-container/video/source[2]').get_attribute('src')

            # //*[@id="douyin-right-container"]/div[2]/div/div/div[1]/div[2]/div/xg-video-container/video/source[2]
            '''
            可以加个判断，如果文件存在，则不保存，如果文件不存在，则保存。
            '''
            

            # while os.path.exists(save_path) == False:
            #         # filename = re.findall(r'/([^/]*$)', url)[0] + str(time.time()) + '.mp4'
            #         # save_path = 'E:/Vedios/dy2/' + filename
            #     res = requests.get(link, stream = True)
            #     with open(save_path, 'wb') as f:
            #         for chunk in res.iter_content(chunk_size = 10240):
            #             f.write(chunk)
            print("这是连接------------------------------------------------------------------------------", link)

            # res = requests.get(link, headers = headers, stream = True)
            # with open(save_path, 'wb') as f:
            #     f.write(res.content)
            # driver.close()

            res = requests.get(link, headers = headers, stream = True)
            if int(res.headers.get('Content-Length')) >= 10240:
                with open(save_path, 'wb') as f:
                    for chunk in res.iter_content(chunk_size = 10240):
                        f.write(res.content)
                driver.close()
            else:
                with open(save_path, 'wb') as f:
                    f.write(res.content)
                driver.close()
        
        else:
            continue