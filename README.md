#基于Django的系统
url命名
1，因为url命名经常变化的，如查在代码中写死可能会经常改代码，给url取个名字
以后使用url的时候就使用它的名字进进行返转，就不用写死url了
2，在'path'函数中传递一个name参数就可以指定，示例代码如下
```
urlpatterns = [
    path('',views.index,name = 'index'),
    path('login/',views.login,name = 'login')
]

from django.http import HttpResponse
from django.shortcuts import redirect,reverse

def index(request):
    index_url = reverse('index')
    print(index_url)
    return HttpResponse('前台首页')

def login(request):
    return HttpResponse('前台登录页')

```
3,应用命名空间
在多个app之间，有可能产生同名的 url这时候为了避免反转url的时候产生混淆
可以应用命名空间来做区分，定义命名空间非常简单，只要在'app'的'urls.py'中定义一个叫做'app_name'的变量，来指定这个应用的命名空间即可
示例代码如下
```
app_name = 'index'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('login/',views.login,name = 'login')
]
```
以后在做反转的时候就可以使用'应用命名空间:url名称'的方式进行反转，示例代码如下 
```
index_url = reverse('index:index')
    print(index_url)
    return HttpResponse('前台首页')
```
























































































