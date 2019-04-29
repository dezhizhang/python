
# from urllib import request

# if __name__ == '__main__':
#     urls = 'http://www.mca.gov.cn/article/sj/xzqh/2019/201901-06/201902031029.html'
#     res = request.urlopen(urls)
#     html = res.read()
#     html = html.decode()

# print(html)

# from urllib import request
# if __name__ == '__main__':
#     urls = 'http://dag.mca.gov.cn/'
#     res = request.urlopen(urls)
#     html = res.read()
#     html = html.decode()
# print(html)

# from urllib import request
# if __name__ == '__main__':
#     urls = 'http://dag.mca.gov.cn/'
#     res = request.urlopen(urls)
#     print(type(res))
#     html = res.read()
#     html = html.decode()

# print(html)

# from urllib import request
# if __name__ == '__main__':
#     urls = 'http://dag.mca.gov.cn/'
#     res = request.urlopen(urls)
#     print('url:{0}'.format(res.geturl()))
#     print('info:{0}'.format(res.info()))
#     print('code:{0}'.format(res.getcode()))

from urllib import request
from urllib import parse
if __name__ == '__main__':
    urls = 'http://www.baidu.com/s?'
    wd = input('请输入关键字')
    qs = {
        'wd':wd
    }
    qs = parse.urlencode(qs)
    fullurl = urls + qs
    res = request.urlopen(fullurl)
    html = res.read()
    html = html.decode()
    print(html)
    









