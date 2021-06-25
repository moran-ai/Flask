from flask import Blueprint
from flask_restful import Api, Resource, fields, marshal_with, reqparse, marshal

from apps.models.news_model import NewsType, News
from exts import db

news_bp = Blueprint('news', __name__)
api = Api(news_bp)

# 新闻类型的输出格式
types_fields = {
    'id': fields.Integer,
    'name': fields.String(attribute='type_name')
}

type_parser = reqparse.RequestParser()
type_parser.add_argument('typeName', type=str, required=True, help='请选择新闻分类')

# 新闻类别
class NewsTypeApi(Resource):
    @marshal_with(types_fields)
    def get(self):
        types = NewsType.query.all()
        return types

    # post添加新闻类型
    def post(self):
        args = type_parser.parse_args()
        typename = args.get('typeName')

        # 添加到数据库
        newsType = NewsType()
        newsType.type_name = typename
        db.session.add(newsType)
        db.session.commit()
        return marshal(newsType, types_fields)

news_parser = reqparse.RequestParser()
# required=True 必填项
news_parser.add_argument('typeid', type=int, help='请选择新闻分类id', required=True)
news_parser.add_argument('page', type=int)

# 自定义fields类型
class AuthorName(fields.Raw):
    def format(self, value):
        return value.username

# 定义每条新闻的输出格式
news_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'desc': fields.String,
    'datatime': fields.DateTime(attribute='date_time'),
    'author': AuthorName(attribute='author'),
    # absolute=True 看见完整url
    'url': fields.Url('news.newsdetail', absolute=True)
}

# 新闻api
class NewsListApi(Resource):
    # 获取某个新闻分类下的新闻
    def get(self):
        args = news_parser.parse_args()
        # newstype = NewsType.query.get(typeid)
        typeid = args.get('typeid')
        page = args.get('page', 1)
        pagination = News.query.filter(News.new_type_id == typeid).paginate(page=page, per_page=8)
        data = {
            'has_more': pagination.has_next,
            'data': marshal(pagination.items, news_fields),
            'return_count': len(pagination.items),
            'html': 'null'
        }
        return data

# 评论回复格式
replay_fields = {
    'user': AuthorName(attribute='user'),
    'content': fields.String,
    'datetime': fields.DateTime(attribute='date_time'),
    'lovenum': fields.Integer(attribute='love_num')
}

# 评论格式
comment_fields = {
    'user': AuthorName(attribute='user'),
    'content': fields.String,
    'datetime': fields.DateTime(attribute='date_time'),
    'lovenum': fields.Integer(attribute='love_num'),
    'replays': fields.List(fields.Nested(replay_fields))
}

# 新闻详情输出
new_detail_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'datetime': fields.DateTime(attribute='date_time'),
    'author': AuthorName(attribute='author'),
    # fields.Nested 嵌套
    'comments': fields.List(fields.Nested(comment_fields))
}

# 新闻详情
class NewsDetailApi(Resource):
    @marshal_with(new_detail_fields)
    def get(self, id):
        news = News.query.get(id)
        return news

api.add_resource(NewsTypeApi, '/types')
api.add_resource(NewsListApi, '/newslist')
api.add_resource(NewsDetailApi, '/newsdetail/<int:id>', endpoint='newsdetail')
