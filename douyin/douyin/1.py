import requests

headers = {
    'authority': 'www.douyin.com',
    'method': 'GET',
    'scheme': 'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Cookie': 'douyin.com; xg_device_score=7.983585126412278; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; dy_swidth=1707; dy_sheight=1067; bd_ticket_guard_client_web_domain=2; n_mh=MwAHPg-ldy5vjDZa2m-0Uz32UYqHWuYijCFkNHJW2Oo; LOGIN_STATUS=1; my_rd=2; store-region=cn-hb; store-region-src=uid; live_use_vvc=%22false%22; xgplayer_device_id=20755753164; xgplayer_user_id=350070612275; SEARCH_RESULT_LIST_TYPE=%22single%22; passport_csrf_token=2a8211efdedcc6e1bd87ddfeea67baf4; passport_csrf_token_default=2a8211efdedcc6e1bd87ddfeea67baf4; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; UIFID_TEMP=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4f32f18448adb07d6570627193de18b3dbab0666da8e59d0ae53bf588959cf689877c0432f38e5dfd759da3e1d99e65752692a4d99cf94ceb989eb933c03885d7; fpk1=U2FsdGVkX1+wlKLuPUiMBkL65O5LwgVZZgxsYKUZIeXPwhz7xbUXJev0uUAX7Zk063XoG7anX2y085fmemtoUA==; fpk2=d94a27a56e6a143d4c900b9014d6ba5d; UIFID=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4f32f18448adb07d6570627193de18b3dbab0666da8e59d0ae53bf588959cf689e1b73b8c259468029552d61687d4e82fd87171fbd9ff98bfa25a689317f915258f41d457127d176d963cd95ef36b88dde672122faf6230b6ca6b8305976f374c8fd8cbb54a9fb4439cc5980f241ff6e0cc6d247e09751e0b74dde9116e95a46a90c5b1467d2ffe5a38ef7d3ed25e0eeaaa59d90e2b4127f82f736fd8bd6c6959; passport_assist_user=CkHYe-YS20cRs45KcfDnqzePeLeUAiIuHUEw-Ugmg4ovykD_plqA6g_ls102Jan-ewflJ8-5Qy9Ip-qfzjnyZntgZRpKCjyd_xkuMHm_BGUiVFE9PwtF49DC4QBOWHTW9EPZ7iO0ni1itJfThAmbCPKUPZq5UbrmdQc8Okg1f-SAiTEQo7HWDRiJr9ZUIAEiAQOLbz8P; sso_uid_tt=ff07d64ca054d604523982f9bc2d6fdd; sso_uid_tt_ss=ff07d64ca054d604523982f9bc2d6fdd; toutiao_sso_user=1a819a1a56c2e8f8f04fe2405a1778b5; toutiao_sso_user_ss=1a819a1a56c2e8f8f04fe2405a1778b5; sid_ucp_sso_v1=1.0.0-KDFkZTQ5YmU1NWNkOTg4NGM5ZDgyNDViMWZmZTkwN2M2ZDI3NWJjODcKIQj3jPDJhvSzAxDa6r-0BhjvMSAMMIanmvgFOAVA-wdIBhoCbGYiIDFhODE5YTFhNTZjMmU4ZjhmMDRmZTI0MDVhMTc3OGI1; ssid_ucp_sso_v1=1.0.0-KDFkZTQ5YmU1NWNkOTg4NGM5ZDgyNDViMWZmZTkwN2M2ZDI3NWJjODcKIQj3jPDJhvSzAxDa6r-0BhjvMSAMMIanmvgFOAVA-wdIBhoCbGYiIDFhODE5YTFhNTZjMmU4ZjhmMDRmZTI0MDVhMTc3OGI1; uid_tt=63444a8f498b43e94f7c6ec4ddaddb58; uid_tt_ss=63444a8f498b43e94f7c6ec4ddaddb58; sid_tt=5fed473170e2468d2ab3e4a6dac417b3; sessionid=5fed473170e2468d2ab3e4a6dac417b3; sessionid_ss=5fed473170e2468d2ab3e4a6dac417b3; _bd_ticket_crypt_cookie=1f366ce5f757f4726da1e57eae835f46; sid_guard=5fed473170e2468d2ab3e4a6dac417b3%7C1720710495%7C5183997%7CMon%2C+09-Sep-2024+15%3A08%3A12+GMT; sid_ucp_v1=1.0.0-KGZiZDJiZjMwNjBhNTY4YTE2ZGRhMzg1NzkxMzhhYmU3ODQ5MzIyZjYKGwj3jPDJhvSzAxDf6r-0BhjvMSAMOAVA-wdIBBoCaGwiIDVmZWQ0NzMxNzBlMjQ2OGQyYWIzZTRhNmRhYzQxN2Iz; ssid_ucp_v1=1.0.0-KGZiZDJiZjMwNjBhNTY4YTE2ZGRhMzg1NzkxMzhhYmU3ODQ5MzIyZjYKGwj3jPDJhvSzAxDf6r-0BhjvMSAMOAVA-wdIBBoCaGwiIDVmZWQ0NzMxNzBlMjQ2OGQyYWIzZTRhNmRhYzQxN2Iz; s_v_web_id=verify_lyn0hwon_8ZNIjG1n_ajtY_47rv_8phB_BaSnHFJsm1MA; publish_badge_show_info=%220%2C0%2C0%2C1721377376586%22; EnhanceDownloadGuide=%220_0_1_1721377404_0_0%22; pwa2=%220%7C0%7C3%7C0%22; __live_version__=%221.1.2.2148%22; download_guide=%223%2F20240721%2F0%22; live_can_add_dy_2_desktop=%221%22; ttwid=1%7CZAY4sBJZ9XMM9pWoPGdIfeIC_wK-E54--NByW5m7ZbA%7C1721573286%7C33fa271f7324bca9ef2141ddf52b8edcfe4b289092dffa8c7efb84cec766040e; strategyABtestKey=%221721618715.904%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.087%7D; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; WallpaperGuide=%7B%22showTime%22%3A1721619113339%2C%22closeTime%22%3A0%2C%22showCount%22%3A5%2C%22cursor1%22%3A51%2C%22cursor2%22%3A0%7D; csrf_session_id=1b53f71143957c1dfe8791bca57a2745; douyin.com; xg_device_score=7.983585126412278; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAztmNcl6IuIaPLfdjJX73RKTy2X--P8GKi0z87YlP9hnpjlLrZrO3ZmRkpW74AdR2%2F1721664000000%2F0%2F1721635150978%2F0%22; odin_tt=dec3baf5caf89bb5719c808b46628f1a287e2d2db1e1c930219b3b9045130002bdd551fe8110b6edacbb1a9b6350027a; __ac_nonce=0669e205100625d0f37d7; __ac_signature=_02B4Z6wo00f01X4qHyQAAIDBiEMWAocd06l-ChuAADkYIZX6uIcAR37yvx4rwctHd9mFGK9Rj6uTfdoWAk.F9AzY7hpkq0Ik0OUbfNi38oslDIl7lVVlgjI5ZR3fislOTgYkS-8X.TRSvG5j01; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAztmNcl6IuIaPLfdjJX73RKTy2X--P8GKi0z87YlP9hnpjlLrZrO3ZmRkpW74AdR2%2F1721664000000%2F0%2F1721638994531%2F0%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCS0tQQXpldEVkZGdGZXRwUzhkRUtONlVRb2JHelh5Q0xpdElTSUcvNkNsYmpwdTRDaGM1bUxUdEU2SkZtSERoZ1IzSkpGQmp3TGo4QUhScEVoa0V5dTQ9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; IsDouyinActive=false; passport_fe_beating_status=false',
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

res = requests.get('https://v3-web-prime.douyinvod.com/video/tos/cn/tos-cn-ve-15/oABhApCYFi3pcAaQIziBydfkEiGXgIpzADDPXe/?a=6383&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=561&bt=561&cs=0&ds=3&ft=4SNWjAIMppftTzL8Esq.C_fauVq0InyeSctc6B3qlVS6zQdHDDLb~M7nU6GqtusZ.&mime_type=video_mp4&qs=1&rc=PGc0NWczaDZmMzM8ODo4OUBpMzU4Zmw5cjpudTMzNGkzM0AyXl9jYmJfX2IxMl9iYzIxYSNmYnFiMmRzNS5gLS1kLTBzcw%3D%3D&btag=80000e00038000&cquery=100b&dy_q=1724388386&expire=1724392592&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20240823124626F1F3AD700097360B2972&ply_type=4&policy=4&signature=92a333f6a18ded5eef539f85eb1e5a3d&tk=webid&webid=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4f32f18448adb07d6570627193de18b3dbab0666da8e59d0ae53bf588959cf689e1b73b8c259468029552d61687d4e82fd87171fbd9ff98bfa25a689317f915258f41d457127d176d963cd95ef36b88dde672122faf6230b6ca6b8305976f374c8fd8cbb54a9fb4439cc5980f241ff6e0cc6d247e09751e0b74dde9116e95a46a90c5b1467d2ffe5a38ef7d3ed25e0eeaaa59d90e2b4127f82f736fd8bd6c6959-277ce8cd01e1d72737c4afed269fe269', headers = headers, stream = True)
print(res)
with open('e:/Vedios/dy4/7404838297203199266.mp4', 'wb') as f:
    f.write(res.content)

# for head in headers:
#     print(headers[head])