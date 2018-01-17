import requests

headers ={'Connection' : 'keep-alive'
          'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.0.2; Redmi Note 2 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060134) NetType/WIFI Language/zh_CN'
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/sharpp,*/*;q=0.8'
'Accept-Encoding' : 'gzip, deflate'
'Accept-Language' : 'zh-CN,en-US;q=0.8'}

cookie = 'ASP.NET_SessionId=erlftaxnvvghr5n4gfsimrb3'
url = 'http://www.baidu.com'
r = requests.get(url=url)


print(r.text)

