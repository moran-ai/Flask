from order import order


@order.route('/order')
def create_order():
    return 'ok'
