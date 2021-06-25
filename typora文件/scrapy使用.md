# scrapy使用

### 1.安装Scrapy框架

```
pip install scrapy
```

### 2.创建scrapy项目

```
① 创建项目名
	scrapy startproject 项目名
② 创建爬虫
	scrapy genspider 爬虫名 域名
③ 运行爬虫
	scrapy crawl 爬虫名
④ 保存爬虫
	scrapy crawl 爬虫名 -o xxx.json/csv/xml
	如果输出json文件中需要显示中文,需要在setting.py文件中设置
	FEED_EXPORT_ENCODING = 'utf-8'
```

### 3.创建crawl scrapy爬虫项目

```
① 创建项目名
	scrapy startproject 项目名
② 创建爬虫
	scrapy genspider -t crawl 爬虫名 域名
```

### 4.在pycharm中运行爬虫

```python
from scrapy import cmdline

cmdline.execute('scrapy crawl 爬虫名'.split(' '))
```

### 5.scrapy保存文件为csv  在pipelines文件中编写内容

```python
import csv
class DoubanspiderPipeline:
    def __init__(self):
        """
        自定义的初始化方法，用来构建csv对象
        """
        # 创建一个csv文件
        self.file=open('xxx.csv', 'w', encoding='utf-8', newline='')
        # 创建一个csv对象
        self.writer=csv.writer(self.file)
        self.writer.writerrow(['字段名1', '字段名2', '字段名3','...'])
    
    def process_item(self, item, spider):
        """
        插入数据到csv文件中
        """
        data = [item['字段名1'], item['字段名2'], item['字段名3']]
        self.writer.writerrow(data)
        return item
    
    def close_spider(self, spider):
        """
        关闭爬虫
        """
        self.file.close() 
```

### 6.保存文件为xlsx,在pipelines文件中编写内容

```python
import openpyxl
class DoubanspiderPipeline:
    def __init__(self):
        self.wb=openpyxl.Workbook()
        self.wk=self.wb.active  # 获取活动表
        sefl.wk.append(['字段名'])
    
    def process_item(self, item, spider):
        data = [item['字段名']]
        self.wk.append(data)
        return item
    def close_spider(self, spider):
        self.wb.save('xxx.xlsx')
        self.wb.close()
```

### 7.保存文件为json格式，在pipelines文件中编写内容

```python
import json

class DoubanspiderPipeline:
	def __init__(self):
        self.file=open('xx.json', 'wb')
    
    def process_item(self, item, spider):
        data=json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.file.writer(data.encode('utf-8'))
        return item
    def close_spider(self, spider):
        self.file.close()
```

### 8.保存文件为txt格式，在pipelines文件中编写内容

```python
class DoubanspiderPipeline:
    def __init__(self):
        self.file=open('xx.txt', 'w', encoding='utf-8')
    
    def process_item(self, item, spider):
        self.file.writer(str(item))
        return item
    
    def close_spider(self, spider):
        self.close()
```

### 9.爬取图片  pipelines文件修改

```python
使用crawlspider进行图片爬取   
需要对settings文件进行修改
	① 设置文件存放的目录
    	IMAGES_STORE='路径'
    ② 开启管道
    ③ 设置请求头
默认的pipelines文件  图片文件会放到full文件目录
	class DoubanspiderPipeline:
		  def process_item(self, item, spider):
			return item
自定义pipelines文件  需要继承ImagesPipeline
	class DoubanspiderPipeline(ImagesPipeline):
        """
        重写ImagesPipeline其中的方法
        """
        def get_media_requests(self, item, info):
            image_requests = super().get_media_requests(item, info)
            for image in image_requests:
                image.item = item
            return image_requests
        
        # 方法一
        def file_path(self, request, response=None, info=None, *, item=None):
            title = request.item['title']  # 获取文件名
       	 	title1 = ''.join(title).replace('[', '').replace(']', '')   
        	image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()  # 设定图片的id
            # image_guid可以进行更改
        	return f'{IMAGES_STORE}/{title1}/{image_guid}.jpg'
        # 方法二
        def file_path(self, request, response=None, info=None, *, item=None):
            path=super().file_path(request)
            title=request.item['title']
            save_path=os.path.join(IMAGES_STROE, title)
            filename=path.replace('full/', '')
            return os.path.join(save_path, filename)
```

### 10.scrapy存入数据到数据库

```

```

