import requests
url = 'http://www.baidu.com/s?'
def baidu(wds):
    count=1
    for wd in wds:
        res = requests.get(url,params={'wd':wd})
        path = 'res%d.txt'%count
        with open(path,'w',encoding='utf8') as f:
            f.write(res.text)
        count +=1

if __name__=="__main__":
    wds = ("廉","晓","娇")
    baidu(wds)

str_ = ".bg{background-image:url(http://s1.bdstatic.com/r/www/cache/static/global/img/icons_5859e57.png);_background-image:url(http://s1.bdstatic.com/r/www/cache/static/global/img/icons_d5b04cc.gif);background-repeat:no-repeat}"
res = str_.split('(')
print(res)
for url in res:
    if 'http' in url or 'https' in url:
        res2 = url.split(');')
        print(res2)







import  requests
LXJ = requests.get('http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808')
with open('%s.jpg','wb') as f:
         f.write(LXJ.content)

for url in LXJ:
    response = requests.get(url)
    content = response.content
    name = url.split('/')[-1]
    with open(name,'wb') as f:
        f.write(content)