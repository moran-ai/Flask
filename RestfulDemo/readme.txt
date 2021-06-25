安装：
    pip install flask-restful

restful:前后端分离API
前端：app, 小程序, pc页面
后端: 没有页面，Mtv: 模型，模板， 视图 去掉了t模板
       mv: 模型， 视图
       模型的使用mtv开发一样
       视图：api构建视图
       1.安装
       pip install flask-restful

        2.创建API对象
        api = Api(app=app)
        api = Api(app=蓝图对象)

        from flask_restful import Api
        api = Api()
        api.init_app(app=app)

        3.定义类视图
            from flask_restful import Resource

            class xxxApi(Resource):
                def get(self):
                    pass

                def post(self):
                    pass

                def put(self):
                    pass

                def delete(self):
                    pass
        4. 绑定API
        api.add_resource(xxxApi, '/')

文档地址：https://flask-restful.readthedocs.io/en/latest/quickstart.html#data-formatting
         http://www.pythondoc.com/Flask-RESTful/quickstart.html

进：
需要定义字典，字典的格式是给客户端看的格式
user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'phone': fields.String,
    'icon': fields.String,
    'udatetime': fields.DateTime(dt_format='rfc822')
}
客户端能看到的是：id, username, password, phone, icon, udatetime
默认名字和model中的模型属性一致，如果不想让前端看见命名，可以修改
但是必须结合attribute='模型的字段名'使用


自定义fields
1.必须继承Raw
2.重写其中的一个方法：
    def format(self):
        return result

    例如：
    class Isdelete(fields.Raw):
        def format(self, value):
            print('--------->', value)
            return '删除' if value else '未删除'

URI的使用
    user_fields_1 = {
    'id': fields.Integer,
    'username': fields.String,
    'uri': fields.Url('single_user', absolute=True)
    # 'password': fields.String,
    # 'phone': fields.String,
    # 'icon': fields.String,
    # 'isDelete': fields.Boolean(attribute='isdelete'),
    # 'isDelete1': Isdelete(attribute='isdelete'),
    # 'udatetime': fields.DateTime(dt_format='rfc822')
    }




出：
    return data
    data必须符合json格式
        json格式:
            {
                'aa': 10,
                'bb': [
                    {
                        'id': '',
                        'xxx': [
                            {}, {}, {}
                        ]
                    }
                ]
            }

如果直接返回，不能有自定义的对象,例如：数据库中的表,数据库....
如果有这种对象：
    方法一：  使用marchal() 方法
    marchal(对象, 对象的fields格式) # 对象的fields格式是指字典的输出格式
    marchal([对象， 对象, 对象], 对象的fields格式)

    方法二：使用marchal_with()装饰器 修饰请求方法
    @marshal_with(user_friends_fields)
    def get(self, id):
        ...
        return data
    需要一个参数，参数是最终数据的输出格式 dict
    参数: user_friends_fields 类型为：dict
    例如：
    user_friends_fields = {
    'username': fields.String,
    'nums': fields.Integer,
    'friends': fields.List(fields.Nested(user_fields))
            }
fields.Nested(fields.String) -------> ['aaa', 'bbb', 'ccc']
fields.Nested(user_fields)  ---> user_fields是一个自定义的字典结构，将里面的每一个对象转为字典结构

什么是RESTful架构：

（1）每一个URI代表一种资源；

（2）客户端和服务器之间，传递这种资源的某种表现层；

（3）客户端通过四个HTTP动词（GET, POST, PUT(全部修改), DELETE, [PATCH](部分修改)），对服务器端资源进行操作，实现"表现层状态转化"。
链接：https://www.jianshu.com/p/75389ea9a90b

Postman
模拟前端的工具
