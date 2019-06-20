import urllib.request

# def Search(word):

# """

# Search word in www.baidu.com

# Parameter:

# ----------

# word: search word.

# Return:

# ------

# None

# """

# # 进行url 编码

# param = urllib.parse.urlencode({'wd':word},encoding='utf8')

# # 请求 url

# url = 'http://www.baidu.com/s?'+param

# # 开始请求 目标url

# response=urllib.request.urlopen(url)

# # 查看网页源代码HTML

# HTML = response.read().decode('utf8')

# print(HTML)
def post(word1,word2):
    url = 'http://httpbin.org/post'
    data = urllib.parse.urlencode({word1:word2},encoding='utf8')
    data = bytes(data,encoding='utf8')
    response = urllib.request.urlopen(url,data=data)
    print(response.read().decode('utf8'))
if __name__ == "__main__":
    post('name','你真是一个小天才')

