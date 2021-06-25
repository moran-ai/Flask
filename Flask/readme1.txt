1.路由
192.168.0.1:8080
@app.route('/index')
def index():
    return 'Hello Wolrd'
url:192.168.0.1:8000/index

route:
        def route(self, rule, **options):
            def decorator(f):
                endpoint = options.pop("endpoint", None)
                self.add_url_rule(rule, endpoint, f, **options)
                return f
            return decorator
这个装饰器将rule字符串和视图函数进行绑定，通过add_url_rule()函数实现绑定

def index1():
    return 'Welcome to Flask'
app.add_url_rule('/', view_func=index1)

@app.route('/index')
def index():
    return 'Hello Wolrd'

app.add_url_rule('/', view_func=index1)  等效于 app.route('/index')

路由的变量规则：
    1.string: (缺省值) 接收任何不包含斜杠的文本  *
    2.int: 接受正整数 *
    3.float:接收正浮点数
    4.path:类似string，但可以包含斜杠
    5.uuid:接收uuid字符串

@app.route('/add/<int:num>')
def add(num):
    """
    加法
    :param num:
    :return:
    """
    result = num + 10
    return str(result)   # 返回值只能是string，dict,tuple,response对象,WSGI，不能是int

2.视图
    1.返回值 返回值都是一个响应对象
    response响应对象 from flask import Response
        response.content_type
        response.headers
        response.status_code  # 状态码
        response.status

    视图函数返回值:
        response响应：
            1.返回值
                a.str 自动转成response对象
                b.dict  json
                c.response对象 from flask import Response
                d.make_response() 返回一个response对象 from flask import make_response
                e.redirect() 重定向 from flask import redirect 302状态码
                f.render_template() 模板渲染 from flask import render_template
                g.url_for 路径反向解析 from flask import url_for

    requests请求对象  from flask import request
        request.full_path
        request.path
        # 只能取出get请求数据
        request.args
        # get请求获取usernama和address
            request.args.get('username')
            request.args.get('address')

        # post请求数据获取
            request.form
            request.form.get('username')
            request.form.get('address')
    2.参数

3.模板
模板的语法：
            1.在模板中获取view(视图)中传递的变量值: {{变量名key}}
                render_template('模板名字', key=value, key=value)
                如果没有找到变量名,则以空白字符串填充

            2.传递的数据类型
                1.str
                2.dict
                3.元组
                5.8种基本数据类型(int,float,double,long,short,chart,boolean,byte)
                4.自定义的类对象
                6.列表
                取值：{{list.0}} 同{{list[0}}
                       {{dict.key}} 同{{dict.get(key)}}
                       {{类对象.name}} 同{{对象.属性}}

            3.控制块
                {% if  条件 %}
                    条件为true
                {% else%}
                    条件为false
                {% endif%}

                {% for 变量 in 可迭代的对象%}
                    for循环要执行的任务
                {%endfor%}

2.使用loop
loop.index 索引从1开始
loop.index0 索引从0开始
loop.revindex 将索引反转
loop.revindex0 索引反转
loop.first 判断是否是第一个值 返回值为boolean
loop.last 判断是否是最后一个值 返回值为boolean

3.过滤器
过滤器的本质就是函数
过滤器语法：
    {{变量名 | 过滤器(*args)}}
    {{变量名 | 过滤器}}

    常见的过滤器：
        1.safe:禁用转译
        2.capitalize :首字母大写
        3.lower: 全部小写
        4.upper: 全部大写
        5.title:一句话中每个单词的首字母大写
        6.reverse:反转
        7.format:格式化输出
        8.truncate:字符串截断

列表过滤器的使用
    1.length:获取列表长度
    2.first:取出第一个元素
    3.last:取出最后一个元素
    4.sum:求和 整型计算
    5.sort:排序 整型

字典过滤器的使用
    1.
        {% for v in users.0.values() %}  ---> 获取值
           <p>值:{{ v }}</p>
        {% endfor %}


        {% for k in users.0.keys() %} --->获取键
            <p>键：{{ k }}</p>
        {% endfor %}


        {% for k,v in users.0.items() %} --->获取值和键
            <p>键： {{ k }}--->值：{{ v }}</p>
        {% endfor %}

自定义过滤器：
    1.通过flask模块中的add_template_filter方法
        a.定义函数，带有参数和返回值
        b.添加过滤器:app.add_template_filter(function, name='自定义过滤器名字')
        c.在模板中使用:{{变量 | 自定义过滤器}}

    2.使用装饰器实现
        a.定义函数，带有参数和返回值
        b.通过装饰器完成 @app.template_filter(name='自定义过滤器名字')
        c.在模板中使用:{{变量 | 自定义过滤器}}


模板的复用
模板继承
include
宏

模板继承:
    需要模板继承的情况
        1. 多个模板具有完全相同的顶部和底部
        2. 多个模板具有相同的模板内容，但是部分内容不同
        3. 多个模板具有完全相同的模板内容

    标签：
        {% block 名字 %}
            需要重写的内容
        {% endblock %}

    1.定义父模板
    2.子模版继承父模板 extends {% extends '父模板名称' %}
步骤：
    1.父模板
        a.定义一个base.html的模板
        b.分析模板中那些是变化的
            对变化的部分使用block进行位置的预留
        c.样式和脚本需要提前预留

    2.子模版使用父模板
        a.{% extends '父模板名称'%} 将父模板继承过来
        b.找到对应的block填充,每个block都是有名字的

include:包含
在A, B ,C 页面包含共同的部分，但是其他页面没有这部分
使用include
步骤：
    1.定义一个公共的模板部分,xx.html
    2.谁使用，则使用include导入过来 {%include '文件夹/xxx.html'%}

宏:macro
1.是jinja2的一个函数，返回一个HTML字符串
2.目的：实现代码复用，避免代码冗余

定义有两种方式：
    1.在模板中直接定义：
        macro1.html中的定义方式

    2.将所有的宏放在一个固定的模板中，例如：macro.html
        若要使用：使用{% import '宏模板的名字 as 别名' %}进行导入
                    调用：{{ xxx.宏名字(**args)}}

{#声明变量的两种方式#}
    {#第一种方式：使用set#}
        {% set username='zhang' %}
        {{ username }}

    {#第二种方式：使用with#}
        {% with num=100 %}
            {{ num }}
        {% endwith %}

{# link导入外部样式文件 #}
    <link rel="stylesheet" href="{{ url_for('static',filename='css/style.css') }}">

{# 导入图片 #}
    <img src="{{url_for('static', filename='images/图片名称.jpg/png')}}">

总结：
    1.变量 ：{{变量}}
    2.代码块：
            a.
                 {% if 条件 %}...{% endif %}
                 {% for 变量名 in 可迭代对象 %}
                     {{变量名}}
                 {% endfor %}

            b.继承：
                {% block %}...{% endblock %}
                {% extends '父模板名' %}

            c.包含一个模板：
                {% include '模板名字' %}

            d.导入宏文件：
                {% import '宏文件名' as 别名 %}
                调用宏：{{别名.定义的宏(参数)}}

            f.宏：
                {% macro 条件(参数) %}...{% endmacro %}
                调用宏：{{条件(参数)}}
