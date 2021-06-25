# Python爬虫之urllib库

### 1.编码url

```python
import urllib.parse
# 模块 urllib.parse()对url进行编码

wd = {
    'id': 1,
    'name': '管理员'
}
data = urllib.parse.urlencode(wd)
print(data)
```

### 2.解码url

```python
import urllib.parse
wd = {
    'id': 1,
    'name': '管理员'
}
# 首先进行编码
data = urllib.parse.urlencode(wd)
print(data)

# 解码  使用urllib.parse.unquote()
resp = urllib.parse.unquote(data)
print(resp)
```

### 3.发送POST请求

```python
import urllib.request
import urllib.parse

url = 'https://www.xslou.com/login.php'
data = {
    'username': 'fdsfsaf',
    'password': 'fsfsfsfsf',
    'action': 'login'
}

# 对data数据进行处理
# 方法一
data = urllib.parse.urlencode(data).encode('utf-8')
# 发送POSTT请求
resp = urllib.request.urlopen(url=url, data=data)
html = resp.read().decode('gbk')
print(html)

# 方法二
# 发送POST请求
resp = urllib.request.urlopen(url=url, data=bytes(urllib.parse.urlencode(data), encoding='utf-8'))
html = resp.read().decode('gbk')
print(html)
```

### 4.发送request请求

```python
import urllib.request

url = 'https://www.douban.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

# 构建请求对象
resp = urllib.request.Request(url=url, headers=headers)

# 发送请求
rep = urllib.request.urlopen(resp)
print(rep.read().decode('utf-8'))
```

### 5.使用urllopen()源码

```python
import urllib.request

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

# 构建请求对象
resp = urllib.request.Request(url=url, headers=headers)
# 构建opener对象
opener = urllib.request.build_opener()

# 发送请求
rep = opener.open(resp)
print(rep.read().decode('utf-8'))
```

### 6.发送http请求

```python
import urllib.request

url = 'https://www.baidu.com/'

# 发送请求
resp = urllib.request.urlopen(url=url)
print(resp.read().decode('utf-8'))
```

### 7.设置ip代理

```python
from urllib.request import build_opener
from urllib.request import ProxyHandler

url = 'https://www.xslou.com/'

# 设置用户代理
pro = ProxyHandler({'https': '116.25.245.228:4216'})

# 构建一个opener对象
opener = build_opener(pro)
# 发送http请求
resp = opener.open(url)
print(resp.read().decode('gbk'))
```

### 8.存储Cookie

```python
import urllib.request
from http import cookiejar

# 设置保存cookie的文件名
filename='cookie.txt'

# 定义获取cookie的函数
def get_cookie():
    """
	获取cookie
	"""
    # 实例化一个MozillaCookieJar(), 用于保存cookie
    cookie = cookiejar.MozillaCookieJar(filename)
    # 创建hander对象
    handler = urllib.request.HTTPCookieProcessor(cookie)
    # 创建opener对象
	opener = urllib.request.build_opener(handler)
    
    url = 'https://tieba.baidu.com/?page=like'
    # 发送请求
    opener.open(url)
    
    # 保存cookie
    cookie.save()

def use_cookie():
    """
    加载cookie
    """
    cookie = cookiejar.MozillaCookieJar()
    
    # 加载cookie文件
    cookie.load(filename)
    print(cookie)

if __name__ == "__main__":
    get_cookie()
    use_cookie()
```

### 9.错误解析，异常处理

```python
import urllib.request
import urllib.error

"""
两大类:
	① URLError
	② HTTPError
"""
url = 'http://www.google.com'
try:
    resp = urllib.request.Urlopen(url)
except urllib.error.URLError as e:
    print(e.reason)
    
url = 'https://www.douban.com'
try:
    resp = urllib.request.Urlopen(url)
except urrlib.error.HTTPError as e:
    print('错误原因:', e.reason)
    print('响应状态码:', e.code)
    print('响应数据：', e.headers)
```

# Python爬虫之requests库