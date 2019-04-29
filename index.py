
from urllib import request

if __name__ == '__main__':
    urls = 'http://www.mca.gov.cn/article/sj/xzqh/2019/201901-06/201902031029.html'
    res = request.urlopen(urls)
    html = res.read()
    html = html.decode()

print(html)


