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

模板中的过虑器  
1,因为在DTL中，不支函数的调用形式'()',所以不能给函数传递参数,这将有很大的局限性  
而过虑器其它就是函数，可以对需要处理的参数进行处理，并且还可以额外接收一个参数'(也就是说最多只能有2个参数)'  
模板的继承  
1,extends标签必须放在模板的开始位置  
2,子模板的代码必须放在block中，否则将不会被渲染  
静态文件的加载
1,

###爬虫程序原理
1,模拟浏览器行为,通过网络请求将目标抓取到本地   
2,使用一定的匹配规则，将目标网页中需要的数据提交出来，把不需要的过虑掉  
3,根据需求，把提取出来的数据存储到磁盘中(json,csv,exec,数据库)

###需要安装的库  
1,request用来做网站请求的，就跟浏览器是一样的
```
pip install requests
```
2，bs4 用来将请求下载下来的数据进行解析，安装方式
```
pip install bs 4
```
###ORM模型介绍   
1,易用性:使用ORM做数据库的开发可以有效减少重复SQL语句的概率，写出来的模型也更加直观，清析。  
2，性能损耗小:ORM转换成底层的数据库操作指令确实会有些开销，但从实际情况来看，这种性能损耗很少。  
3，设计灵活：可以轻松的写出复杂的查询  
4，可移植性：Django封装了底层的数据库实现，支持多个关系数据库引擎。  













































































































