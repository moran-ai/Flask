from flask import Blueprint, request, render_template, redirect, url_for

from apps.goods.model import Goods, User_Goods
from apps.user.model import User
from ext import db

goods_bp = Blueprint('goods', __name__)

@goods_bp.route('/findgoods')
def find_goods():
    """
    根据用户找商品
    :return:
    """
    # 获取用户id
    id = request.args.get('uid')
    users = User.query.get(id)
    return render_template('goods/find_goods.html', users=users)

@goods_bp.route('/finduser')
def find_user():
    """
    根据商品找用户
    :return:
    """
    goods_id = request.args.get('gid')
    goods = Goods.query.get(goods_id)
    return render_template('goods/find_user.html', goods=goods)

@goods_bp.route('/show')
def show():
    users = User.query.filter(User.isdelete==False).all()
    goods_list = Goods.query.all()
    return render_template('goods/show.html', users=users, goods_list=goods_list)

@goods_bp.route('/buy')
def buy():
    uid = request.args.get('uid')
    gid = request.args.get('gid')
    ug = User_Goods()
    ug.user_id = uid
    ug.goods_id = gid
    db.session.add(ug)
    db.session.commit()
    return '购买成功'
