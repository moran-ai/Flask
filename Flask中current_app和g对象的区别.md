

# Flask中current_app和g对象的区别

##### **Flask中有两种上下文，一种是请求上下文，一种是应用上下文**

**request和session属于请求上下文**

**current_app和g对象属于应用上下文**

request:封装了HTTP请求的内容，针对的是http请求，获取的是get或者post请求的参数。

session:用来记录请求会话中的信息，针对的是用户信息。

**current_app:表示当前运行程序文件的程序实例**

g:处理请求时，用于临时存储的对象,每次请求都会重设这个对象，比如：在用户执行某个操作，可以使用g判断当前用户是否是登录状态

```
当调用app = Flask(_name_)的时候，创建了程序应用对象app；
request 在每次http请求发生时，WSGI server调用Flask.call()；然后在Flask内部创建的request对象；
app的生命周期大于request和g，一个app存活期间，可能发生多次http请求，所以就会有多个request和g。
最终传入视图函数，通过return、redirect或render_template生成response对象，返回给客户端。
```

**请求上下文和应用上下文的区别**

请求上下文：保存客户端和服务器的数据

应用上下文：在flask程序运行过程中，保存的一些配置信息，比如程序文件名，数据库的连接，用户信息等
**上下文的作用域**

```
在flask项目中某一个功能中会有多个视图，那么from flask import request,current_app,session,g，怎么保证某次请求的上下文不会被别的视图拿走呢？
```

从pycharm中进入globals.py：

```
_request_ctx_stack = LocalStack()
_app_ctx_stack = LocalStack()
current_app = LocalProxy(_find_app)
request = LocalProxy(partial(_lookup_req_object, 'request'))
session = LocalProxy(partial(_lookup_req_object, 'session'))
g = LocalProxy(partial(_lookup_app_object, 'g'))
```

```
线程有个叫做ThreadLocal的类，也就是通常实现线程隔离的类。而werkzeug自己实现了它的线程隔离类：werkzeug.local.Local。LocalStack就是用Local实现的。
LocalStack是flask定义的线程隔离的栈存储对象，分别用来保存应用和请求上下文。
它是线程隔离的意思就是说，对于不同的线程，它们访问这两个对象看到的结果是不一样的、完全隔离的。这是根据pid的不同实现的，类似于门牌号。而每个传给flask对象的请求，都是在不同的线程中处理，而且同一时刻每个线程只处理一个请求。所以对于每个请求来说，它们完全不用担心自己上下文中的数据被别的请求所修改。
而这个LocalProxy 的作用就是可以根据线程/协程返回对应当前协程/线程的对象，也就是说
线程 A 往 LocalProxy 中塞入 A
线程 B 往 LocalProxy 中塞入 B
无论在是什么地方，
线程 A 永远取到得是 A，线程 B 取到得永远是 B
```

