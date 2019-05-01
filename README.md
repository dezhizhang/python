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
模板变量
1,在模板中使用变量,需要将变量放在'{{变量}}'中  
2,如果想要访问对象的属性，那么可以通过'对象属性名'来进行访问  
3,如果想要访问一个字典的key对应的value，那么只能通过'字典.key'的方式进行访问，不能通过'中括号[]'的形式进行访问  
4,因为在访问字典的'key'时候也是使用点'.'来进行访问，因此不能在字典中定义本身就有属性名当作'key',否则字典的那个属性将变成字典的key了  
5,如果想要访问列表或元组，那么也是通过'.'的方式进访问，不能过过'[]'进行访问，这一点和在python是不一样的,示例代码如下  
```
context = {
    'username':'zhangshang'
}
{{username}}
```
```
context = {
        'pserson':['张三','李四','王五']
    }
    return render(request,'index.html',context = context)
{{person.1}}
```
模板if语句  
1,所有的标签都是在'{%%}'之间  
2,if标签有闭合标签，就是'{%endif%}'  
3,if标的判断运算符，就是跟python中的判断运算符一样的'==,!=,<=,>=,in mot is,is not'  
4,还可以使用elif或else语句,示例代码如下
```
{% if age > 19 %}
     <p>你还没有成年</19>
{% elif age == 18%}
    <p>你以成年了</p>
{% endif %}
```
模板for语句

模板url语句

































































































