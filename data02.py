import urllib.request

urls = ('http://www.baidu.com','http://www.taobao.com','http://www.hao123.com')
for url in urls:
    try:
        response = urllib.request.urlopen(url,timeout=0.1)
        print('%s 请求成功'%url)
    except:
        print('%s 失败'%url)

 