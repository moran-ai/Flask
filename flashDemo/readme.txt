1.闪现
    1.在一个请求结束时添加flash
    2.在当前请求中渲染获取或者仅仅下一个请求中可以获取

添加闪现 （后面的类型可选）
flash('信息1', 'info')
flash('信息2', 'error')
flash('信息3', 'warning')

获取flash的值
with_categories=True 返回元组
with_categories=False 返回一个message
get_flashed_messages(with_categories=True)

get_flashed_messages(category_filter=['error']) 可选的
有针对性的获取对应类型的闪现消息

2.日志
    uwsgi ----> uwsgi.log

    1.使用app自带
        app.logger.info('')
        logger.debug("Do something")
        logger.warning("Something maybe fail.")
        logger.error("Finish")

    2.通过logging创建
       import logging

       logger = logging.getLogger('name') # 默认flask的名字是app
       logger = logging.getLogger('app')

       保存到文件：
       方式一：
            filename：保存的文件名  filemode:保存的模式 a:追加
       logging.basicConfig(filename='log.txt', filemode='a', level=logging.WARNING,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
       logger = logging.getLogger(__name__)

    方式二：
        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.INFO)
        handler = logging.FileHandler("log1.txt")
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    3.使用logger.info('message')
