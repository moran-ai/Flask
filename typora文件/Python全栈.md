## Python全栈

### HTML知识

```
1.html标签
	① head标签 -----> 里面放置页面的配置信息
	head部分可以放如下标签：
		<title>, <meta>, <link>, <style>, <script>，<base>
    ② body标签 -----> 放置页面展示出来的内容		
```

#### head中可用标签

```html
<!DOCTYPE html>
<html>
	<!-- 
	 head标签中，放置页面的配置信息
	 -->
	<head>
		<!-- 设置页面编码，防止乱码 -->
		<meta charset="utf-8" />
		<!-- 页面标题 -->
		<title>hello，你好</title>  
		<!-- 页面刷新效果  3秒刷新到百度首页--> 
		<!-- <meta http-equiv="refresh" content="3;https://www.baidu.com" /> -->
		<!-- 页面作者 -->
		<meta name="author" content="msb;23456465e@qq.com" />
		<!-- 设置页面搜索的关键字 -->
		<meta name="keywords" content="hello; 线上; 书籍" />
		<!-- 页面描述 -->
		<meta name="description" content="详情页" />
		<!-- 加上图标，百度图标 -->
		<link rel="shortcut icon" href="https://www.baidu.com/favicon.ico" type="image/x-icon" />
	</head>
	<!-- 
	 body标签中放置页面展示的内容
	 -->
	<body>
		this is a html, 你好
	</body>
</html>
```

#### body中可用标签

##### ① 文本标签

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>文本标签</title>
	</head>
	<body>
		<!-- 文本标签 -->
		补短板 强功
		补短板 强功
		补短板 强功
		补短板 强功
		<!-- 标题标签 
		h1-h6  字号逐渐变小,自带换行  h7后属于无效标签
		-->
		<h1>补短板 强功</h1>
		<h2>补短板 强功</h2>
		<h3>补短板 强功</h3>
		<h4>补短板 强功</h4>
		<h5>补短板 强功</h5>
		<h6>补短板 强功</h6>
		<!-- 横线标签 
		width:设置宽度
			300px: 固定宽度
			30%:  页面宽度的百分比，随着页面宽度变化而变化
		align: 设置位置  默认不写居中
		-->
		<hr width="300px" align="left"/>
		<hr width="30%" align="left"/>
		
		<!-- 段落标签 
		段落效果：自动换行，段落与段落之间有空行
		&emsp;:换行  比&nbsp换行大
		&lt;:< 
		&gt;:>
		&nbsp; ©
		-->	
		<p>&nbsp;&nbsp;&nbsp;&nbsp;拍摄屏幕快照。边界框内的像素在&copy;Windows上以“RGB”图像或在macOS上以“RGBA”形式返回。如果省略了边界框，则会复制整个屏幕。</p>
		<p>拍摄屏幕快照。边界框内的像素在&lt;Windows&gt;上以“RGB”图像或在macOS上以“RGBA”形式返回。如果省略了边界框，则会复制整个屏幕。</p>
		<p>拍摄屏幕快照。边界框内的像素在Windows上以“RGB”图像或在macOS上以“RGBA”形式返回。如果省略了边界框，则会复制整个屏幕。</p>
		<!-- 加粗，倾斜,下划线 -->
		<b>加粗</b>
		<i>倾斜</i>
		<u>下划线</u>
		<u><i><b>加粗倾斜下划线</b></i></u>
		
		<!-- 预编译标签:在页面上显示原样效果 -->
		<pre>
			public static void main(String[] args){
				System.out.println("Hello Word")；
			}
		</pre>
		
		<!-- 换行 -->
		拍摄屏幕快照。边界框内的像素在&lt;Windows&gt;<br />上以“RGB”图像或在macOS上以“RGBA”形式返回。如果省略了边界框，则会复制整个屏幕。
		<br>
		<!-- 一箭穿心 -->
		<del>你好，哈哈</del>
		
		<!-- 字体标签 -->
		<font color="antiquewhite" size="7">边界框内的像素</font>
	</body>
</html>
```

##### ② 多媒体标签

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<!-- 图片 
		src:引入图片的位置
			引入本地资源
		width:设置高度
			注意：一般高度和宽度只设置一个即可，另一个会按照比例自动设置
		title：鼠标悬浮在图片上的提示语，默认情况下（没有设置alt属性）图片加载失败那么提示语是title的内容
		-->
		<img src="img/壁纸.jpg" width="300px" title="这是一个图片" alt="图片加载失败">	
		<img src="https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=900725287,2889491409&fm=26&gp=0.jpg" alt="">
		<img src="https://img14.360buyimg.com/n7/jfs/t1/157622/2/5868/103794/6017cb04E79a5d0e1/6a00ca4ca483df1e.jpg" alt="">
		<!-- 音频 -->
		<embed src="music/鹿先森乐队%20-%20春风十里.mp3" type="">
		<!-- 视频 -->
		<!-- <embed src="" width="200px" height="300px" type=""> -->
		<embed src="//player.video.iqiyi.com/4ca1496a17b3c9486ad541503f1e52df/0/0/v_19rqsgc8to.swf-albumId=1654878400-tvId=1654878400-isPurchase=0-cnId=undefined" allowFullScreen="true" quality="high" width="480" height="350" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>
	 </body>
</html>

```

##### ③ 超链接标签

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<!-- 超链接标签 
		href:跳转的位置
		target:_self 自身页面打开 （默认）  _blank 空白页面打开
		-->
		<a href="文本标签.html" target="_blank">这是一个超链接</a>
	</body>
</html>
```

#### ④ 超链接设置锚点

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>商城</title>
	</head>
	<body>
		<!-- 设置锚点 锚点：同一个页面不同位置的跳转 -->
		<a name="F1"></a>
		<h1>手机</h1>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<p>华为</p>
		<a name="F2"></a>
		<h1>书籍</h1>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<p>三国演义</p>
		<a name="F3"></a>
		<h1>服装</h1>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<p>裤子</p>
		<a name="F4"></a>
		<h1>电器</h1>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<p>电器产品</p>
		<a href="#F1">手机</a>
		<a href="#F2">书籍</a>
		<a href="#F3">服装</a>
		<a href="#F4">电器</a>
	</body>
</html>
```

⑤ 其他页面使用锚点

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>其他页面使用锚点</title>
	</head>
	<body>
		<a href="超链接设置锚点.html#F2">超链接</a>
	</body>
</html>
```

#### 列表标签

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>列表标签</title>
	</head>
	<body>
		<!-- 无序列表 
			type：设置列表前图标的样式 有三种样式
			想要更换图标样式，需要借助css，style="list-style:url(图片地址);"
		-->
		<h1>书籍</h1>
		<ul type="square">
			<li>三国演义</li>
			<li>呐喊</li>
			<li>彷徨</li>
			<li>雪</li>
		</ul>
		<!-- 有序列表 
		type:设置列表的标号：1,I,A
		start:设置起始位置
		-->
		<h1>学习的顺序</h1>
		<ol>
			<li>高等数学</li>
			<li>英语</li>
			<li>计算机基础知识</li>
			<li>数据结构与算法</li>
		</ol>
	</body>
</html>

```

