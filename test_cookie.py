import json

with open('E:/Git_Repository/scrapy_douyincollection/cookie.txt', 'r') as cookie:
    # cookielist = json.load(cookie)
    data = cookie.readlines()[0]
    print('这是json--------------------------------', json.dumps(data))
    # print('这是文本---------------------------------', data)
    cookielist = json.load(json.dumps(data))