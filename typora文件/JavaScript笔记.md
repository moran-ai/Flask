#  (JavaScript笔记	

## 一. JavaScript组成

```
① ECMAScript:欧洲计算机协会，大概每年六月份中旬定制语法规范
② DOM:全称Document Object Model  中文全称：文档对象模型
③ BOM：全称Browser Object Model  中文全称：浏览器对象模型
```

## 二. DOM:Document Object Model 文档对象模型

### 1.获取节点方法

```
getElementById：可以通过标签的ID选择器，在js中获取标签 可以获取到节点树上任意的节点，需要给节点添加id
document.getElementById();
getElementsByTagName 通过标签名获取节点，返回类数组
getElementsByClassName 通过标签的class属性获取节点，返回类数组
querySelector 通过任意的选择器获取节点
```

### 2.操作节点的属性

```
获取id属性
    var div = document.getElementById("box");
    console.log(div.className); 
设置节点的id属性	
	div.id = "xxx";
设置节点的class属性
	div.className = "xxx";
```

### 3.操作节点的文本

```
两种情况：
    ① 非表单元素获取文本 使用innerHTML
    ② 表单元素获取文本   使用value
	可以对节点的文本进行设置
		① 非表单元素
			selector.innerHTML = "xxxx";
		② 表单书元素
			selector.value ="xxx";
```

### 4.操作节点的样式

```
通过id获取节点：
	var span = document.getElementById("b");
获取节点的样式：
	console.log(span.style.width);
设置节点的样式：
	span.style.width = "20px";
```

### 5.节点绑定事件信号量

```html
<script type="text/javascript">
			var p = document.getElementById("box");
			// 创建一个信号量
			var sum = 12; // 字体大小默认是12
			p.onclick = function() {
				sum++;
				// 设置字体的最大大小为30
				if (sum >= 30) {
					sum = 30;
				}
				// 改变字体大小
				p.style.fontSize = sum + "px";
			}
		</script>
```

### 6.节点的事件

```
事件绑定：
语法格式：
    element onxxx = function(){

    }
onxxx:事件名称，都是小写
function：事件处理函数,用户触发事件时会执行一次
```

### 7.节点树

```
获取节点树的html标签：document.documentElement
获取节点数据的head标签：document.head
获取节点数的title文本：document.title
获取节点数的body: document.body
```

```html
<script>
    // DOM:document object model  文档对象
    console.log(document);
    console.log(typeof document);  // object
</script>
<script type="text/javascript">
    // DOM常用属性
    // documentElement:获取到节点树的html标签
    console.log(document.documentElement);

    // head:获取到节点树的head标签
    console.log(document.head);

    // title属性 获取title的文本
    console.log(document.title);

    // body 获取节点<body>
    console.log(document.body);
</script>
```



### 8.聚焦和失焦事件

```
一般和表单元素进行使用：
    onfocus:聚焦
    onblur: 失焦
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>聚焦和失焦事件</title>
</head>
<body>
<p>
    手机号：<input type="text" id="cur"><span id="sp"></span>
</p>
</body>
</html>
<script>
    /*
    *  一般和表单元素进行使用：
    *   onfocus:聚焦
    *   onblur: 失焦
    * */
    var input = document.getElementById("cur");
    var span = document.getElementById("sp");
    // 鼠标聚焦事件
    input.onfocus = function () {
        input.style.color = 'green';
    }

    // 鼠标失焦事件
    input.onblur = function () {
        // 获取输入框中的值
        var txt = input.value;
        // 使用正则判断手机格式是否正确
        if (/^1[3456789]\d{9}/.test(txt) && txt.length == 11) {
            span.style.color = "pink";
            span.innerHTML = "";
        } else {
            span.style.color = "red";
            span.innerHTML = "手机号必须为11位";
        }
    }
</script>
```

### 9.批量添加事件

```
在特定的场景下，有很多相同的标签或者节点，需要添加相同的事件，可以批量添加事件
方法一：使用IIFE：
    IIFE:在声明表达式函数的同时立刻马上执行一次
    每一个IIFE都有自己独立的作用域，相互不影响

方法二：使用this
```

```html
<script>
var liArr = document.getElementsByTagName("li");
		for (var i = 0; i < liArr.length; i++) {
		// console.log(liArr[i]);
		// 批量绑定事件
		liArr[i].onclick = function () {
			// 定义一个IIFE，用来独立每一个元素的值
		//     +function (index) {
		//         console.log(liArr[index]);
		//     }();
		// }
		// 使用IIFE，用来独立每一个元素的值
			+function (index) {
				liArr[index].onclick = function () {
					liArr[index].style.color = "red";
				}
			}(i);
		}
		console.log("循环语句结束" + i);  // 5
</script>
```

```html
<script>
			// 使用this
			var li = document.getElementsByTagName("li");
			for (var i = 0; i < li.length; i++) {
				li[i].onclick =function () {
					this.style.color = "red";
				}
			}
		</script>
```

### 10.事件处理函数event

```
事件函数执行时，系统自动注入实参，用形参接收【事件对象】
考虑浏览器的兼容性：
    高级浏览器：谷歌,IE8以上的浏览器--->事件对象返回event
    低级浏览器：IE8以下的浏览器--->事件对象作为BOM对象属性
短路操作解决浏览器兼容问题
	var e = event || window.event;
```

### 11.获取鼠标的位置

```
screenX和screenY：两者是事件对象属性，主要可以获取鼠标位置。获取鼠标位置零零点在【电脑屏幕左上角】
pageX和pageY:两者是事件对象属性，主要可以获取鼠标位置 获取鼠标位置零零点在网页主体部分左上角,零零点会随着滚动条滚动而移上去
clientX和clientY：两者是事件属性，主要获取鼠标位置，获取鼠标位置零零点在可视区域左上角
offsetX和offsetY:两者是事件属性，主要获取鼠标位置，类似于pageX和pageY，但是鼠标位置零零点会受到子元素坐标体系的影响，既鼠标放在那个位置上，零零点就是该位置的左上角
```

```html
<script>
var inn = document.querySelector(".inner");
		 // 鼠标在整个页面中进行移动
		 document.onmousemove = function (event) {
			 // console.log(event);
			 // 短路操作解决浏览器兼容问题
			 var e = event || window.event;
			 // 零零点电脑屏幕左上角
			 inn.innerHTML = "screenX=" + e.screenX + ", " + "screenY=" + e.screenY + "<br/>";
			 // 零零点网页主体左上角  零零点会随着滚动条滚动而移上去
			 inn.innerHTML += "pageX=" + e.pageX + ", " + "pageY=" + e.pageY + "<br/>";
			 // 零零点可视区域左上角
			 inn.innerHTML += "clientX=" + e.clientX + ", " + "clientY=" + e.clientY + "<br/>";
			 // 鼠标位于那个元素上，零零点就在该元素的左上角
			 inn.innerHTML += "offsetX=" + e.offsetX + ", " + "offsetY=" + e.offsetY + "<br/>";
</script>
```

### 12.鼠标常用事件

```
onmousedown()   鼠标按下事件
onmousemove()   鼠标移动事件
onmouseup()     鼠标抬起事件
onmouseenter：鼠标进入事件
onmouseleave: 鼠标移除事件
onmouseover   鼠标进入事件
onmouseout    鼠标移除事件
```

### 13.使用原生js实现拖拽效果

```html
/*
拖拽效果的三板斧：
① 鼠标按下
② 鼠标移动
③ 鼠标抬起
*/
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>原生js实现拖拽效果</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .cur {
            position: absolute; /*只有定位的元素才有left top 的概念*/
            width: 100px;
            height: 100px;
            background-image: url("img/4.jpg");
            background-size: 100px 100px; /* 设置背景图的大小*/
        }

    </style>
</head>
<body>
<div class="cur"></div>
</body>
</html>
<script>
    /*
    *  拖拽效果的三板斧：
    *       ① 鼠标按下
    *       ② 鼠标移动
    *       ③ 鼠标抬起
    * */
    // 获取div节点
    var cur = document.querySelector(".cur");
    // 添加鼠标按下事件
    cur.onmousedown = function (event) {
        // 短路解决兼容问题
        var e = event || window.event;
        // 使用offset获取图片上鼠标的位置
        var startX = e.offsetX;
        var startY = e.offsetY;

        // 鼠标全屏移动事件
        document.onmousemove = function (event1) {
            var e = event1 || window.event;
            // 使用client获取可视区域鼠标的位置
            cur.style.left = e.clientX - startX + "px";
            cur.style.top = e.clientY - startY + "px";
        }

        // 鼠标抬起事件
        document.onmouseup = function () {
            document.onmousemove = null;
        }
    }
</script>
```

### 14.淘宝二级菜单

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>淘宝二级菜单</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .container {
            width: 80%;
            height: 400px;
            /*color: #EFEFEF;*/
            margin: 30px auto;
            border: 1px solid black;
        }

        .container div {
            float: left;
        }


        #left {
            width: 20%;
            height: 100%;
            border-right: 1px solid black;
        }

        #right {
            width: 79%;
            height: 100%;
            /*border-left: 1px solid black;*/
            /*display: none; !*隐藏元素*!*/
        }

        #left ul {
            width: 100%;
            list-style: none;
        }

        #left ul li {
            text-align: center;
            height: 30px;
            margin: 10px 0;
        }

    </style>
</head>
<body>
<div class="container">
    <div id="left">
        <ul>
            <li>女装 / 内衣 / 家居</li>
            <li>女鞋 / 男鞋 / 箱包</li>
            <li>母婴 / 童装 / 玩具</li>
            <li>男装 / 运动户外</li>
            <li>美妆 / 彩妆 / 个护</li>
            <li>手机 / 数码 / 企业</li>
        </ul>
    </div>
    <div id="right">购买的商品</div>
</div>
</body>
</html>
<script>
    // 获取所有的li标签
    var liArr = document.getElementsByTagName("li");
    // 获取右侧div
    var rt = document.getElementById("right");
    for (var i = 0; i < liArr.length; i++) {
        // 批量添加样式，定义一个IIFE
        +function (index) {
            // 添加鼠标进入事件，选中的li颜色改变
            liArr[index].onmouseenter = function () {
                // 先让所有的li恢复初始状态的颜色
                for (var j = 0; j < liArr.length; j++) {
                    liArr[j].style.color = "black";
                }
                // 选中的li颜色改变
                liArr[index].style.color = "pink";

                // 右侧内容展示
                rt.style.display = "black";
                rt.innerHTML = "购买的物品是" + index;
            }
        }(i);
    }
</script>
```

### 15.淘宝放大镜效果

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>淘宝放大镜效果</title>
		<style>
			/*清除整个页面多余的样式*/
			* {
				margin: 0;
				padding: 0;
			}

			.outer {
				position: relative;
				/*相对定位*/
				width: 800px;
				height: 600px;
				background-image: url("img/7.png");
				/*设置背景图*/
				background-size: 800px 600px;
				/*背景图的大小*/
			}

			.sal {
				position: absolute;
				/*绝对定位*/
				width: 300px;
				height: 300px;
				background-color: skyblue;
				opacity: .3;
				/* 透明度  0~1之间*/
			}

			.small {
				position: absolute;
				/* 绝对定位*/
				width: 300px;
				height: 300px;
				right: -420px;
				top: 0;
				/* background-image: url("img/7.png"); */
				background-size: 800px 600px;
				/*让元素样式放大*/
				transform: scale(1.8);
				/* 放大1.8倍*/
			}
		</style>
	</head>
	<body>
		<div class="outer">
			<div class="sal"></div>
			<div class="small"></div>
		</div>
	</body>
</html>
<script>
	// 获取div类名为sal的节点
	var sal = document.querySelector(".sal");
	// 获取div类名为small的节点
	var small = document.querySelector(".small");
	// small.style.backgroundImage="none";
	// 添加鼠标按下事件
	sal.onmousedown = function(event) {
		// 短路操作解决浏览器兼容问题
		var e = event || window.event;
		var startX = e.offsetX;
		var startY = e.offsetY;
		// 添加鼠标移动事件
		document.onmousemove = function(event1) {
			var e = event1 || window.event;
			// 求出left和top的值
			var l = e.clientX - startX;
			var r = e.clientY - startY;
			// 如果if语句后面只有一条语句，{}可省
			// 如果left值小于0，则值恒等于0
			if (l <= 0) l = 0;
			// 如果left值大于700，则值恒等于700
			if (l >= 500) l = 500;
			// 如果top的值小于0，则值恒等于0
			if (r <= 0) r = 0;
			// 如果top的值大于700，则值恒等于700
			if (r >= 300) r = 300;
			// 设置内部盒子的左侧和顶部
			sal.style.left = l + "px";
			sal.style.top = r + "px";

			// 设置背景图
			small.style.backgroundImage = "url(./img/7.png)";
			//修改小图背景图定位
			small.style.backgroundPosition = "-" + l + "px -" + r + "px";
		}

		// 添加鼠标抬起事件
		document.onmouseup = function(event) {
			document.onmousemove = null;
			// small.style.backgroundImage = "none";
			var e = event || window.event;
			var l = e.clientX - startX;
			var r = e.clientY - startY;
			if (l < 0 || l > 600) {
				small.style.backgroundImage = "none";
			}
			if (r < 0 || r > 600) {
				small.style.backgroundImage = "none";
			}
		}
	}
</script>
```

### 16.淘宝特效制作

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>淘宝特效制作</title>
    <style>
        div {
            width: 520px;
            height: 570px;
            margin: 100px auto;
            /*border:2px solid orange;*/
        }

        .c {
            text-align: center;
            color: red;
            font-weight: bold;
            margin-top: 4px;
        }

        img {
            height: 500px;
            padding: 10px;
        }
    </style>
</head>
<body>
<div id="box">
    <img src="img/5.png" alt="">
    <p class="c">￥398.00</p>
</div>
</body>
</html>
<script>
    /*
    *  鼠标进入事件：
    *       onmouseenter
    *       onmouseover
    *  鼠标移除事件
    *       onmouseleave
    *       onmouseout
    * */
    var div = document.getElementById("box");
    // 鼠标进入出现边框
    div.onmouseenter = function () {
        div.style.border = "2px solid orange";
    }

    // 鼠标移除边框消失
    div.onmouseleave = function () {
        div.style.border = "none";
    }
</script>
```

### 17.网易云效果

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>网易云效果</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .container {
            width: 100%;
            height: 60px;
            background-color: red;
        }

        ul {
            width: 50%;
            margin: 0 auto;
            list-style: none;
        }

        ul li {
            float: left;
            width: 60px;
            height: 20px;
            color: white;
            font-size: 12px;
            /*border-radius: 10px 10px 10px 10px;   !*圆角*!*/
            text-align: center;
            margin: 20px; /*外边距*/
            /*opacity: .4;  !*透明*!*/
        }

    </style>
</head>
<body>
<div id="box" class="container">
    <ul>
        <li>推荐</li>
        <li>排行榜</li>
        <li>歌单</li>
        <li>主播电台</li>
        <li>歌手</li>
        <li>新碟上架</li>
    </ul>
</div>
</body>
</html>
<script>
    /**/
    // 获取所有的li
    var li_listArr = document.getElementsByTagName("li");
    for (var i = 0; i < li_listArr.length; i++) {
        // 批量添加事件  使用IIFE
        +function (index) {
            // 添加鼠标进入事件
            li_listArr[i].onmouseenter = function () {
                for (var j = 0; j < li_listArr.length; j++) {
                    // 节点样式和起始状态所有的样式一样
                    li_listArr[j].style.background = "red";
                    li_listArr[j].style.borderRadius = "none";
                }
                // 鼠标移动到某个节点上时添加样式
                li_listArr[index].style.background = "rgb(0,0,0,.3)";  /*(0,0,0)黑色 .3代表透明度*/
                li_listArr[index].style.borderRadius = "10px 10px 10px 10px";
            }

            // 鼠标移除事件
            li_listArr[i].onmouseleave = function () {
                // 鼠标移除恢复到起始状态
                for (var j = 0; j < li_listArr.length; j++) {
                    // 节点样式和起始状态所有的样式一样
                    li_listArr[j].style.background = "red";
                    li_listArr[j].style.borderRadius = "none";
                }
            }
        }(i);
    }
</script>
```



## 三. BOM对象  Browser Object Model 浏览器对象模型  也就是window对象

### 1.BOM对象的初识

```html
<script>
			// BOM:内置的window对象
			// 作为BOM对象属性，可以省略window
			console.log(window);
		
			// 获取地址栏信息
			console.log(window.location.href);
			console.log(location.href);
		
			// 获取屏幕的信息
			console.log(window.screen);
			console.log(window.screen.width);
			console.log(window.screen.height);
			console.log(screen.height);
		
			// 获取浏览器信息
			console.log(window.navigator);
			console.log(window.navigator.userAgent);
			console.log(navigator.userAgent);
		</script>
```

### 2.定时器

```
定时器：每隔一段时间执行一次回调函数  setInterval(callback,time) 1s=1000ms 单位为毫秒
定时器是一个异步语句，很耗时间
异步语句有一个很大的特征：先执行异步语句后面的代码，回首在执行异步语句
```

```html
<script>
console.log(setInterval(function () {
		    console.log("定时器");
		}, 1000));
		
		// 定时器后面的代码
		console.log("异步语句后面的代码");
		
		// 清除定时器
		clearInterval(1);
</script>
```

## 四. jQuery框架

```
jQuery是前端当中一个非常优秀的JS函数库,这个函数库对外暴露一个$函数,$是jQuery函数库中非常核心的一个函数
可以用来匹配节点树上的标签

注意：
    jQuery函数库支持很多选择器：*【通配选择器】， 标签选择器，类选择器，id选择器等
```



### 1. 类名操作

```
addClass:  给匹配的节点添加元素
	$("div").addClass("bobxxx");  给div添加类名bobxxx
removeClass: 给匹配的节点移除元素
	$("div").removeClass("bobxxx"); 给div移除类名bobxxx
index:获取匹配节点的索引值
	console.log($(".cur").index());
each:遍历全部匹配的节点  each(callback) 里面有一个回调函数
	该回调函数有两个参数，一个是节点的索引值，一个是节点
    $("li").each(function (index, element) {
    // index:索引值
    // element:匹配的节点
    console.log(index, element);
    $(element).css({"color": "red", "width": "100"});
    });
```

### 2. 特效函数

```
原理:动态修改高度
slideDown：向下滑动  slideDown(time, callback)
    第一个参数：代表每一次动画时间 【可有可无】
    第二个参数：回调函数 动画结束后立即执行一次 【可有可无】

slideUp：向上卷起

原理:动态修改透明度
    fadeOut: 淡出
    fadeout(time, callback)
        第一个参数：动画每一次需要的时间 单位毫秒  【可有可无】
        第二个参数：回调函数        【可有可无】
fadeIn:	 淡入
```

### 3.节点文本

```
非表单元素的文本：html()
表达元素的文本：val()
【可以对节点的文本进行获取和设置】
```

```html
<script>
    /*
    *  html:获取非表单元素的文本
    *  val:获取表单元素的文本
    * */
    // 获取表单元素的文本
    console.log($("input").val());

    // 设置表单元素的文本
    $("input").val("啊啊啊啊");

    // 获取非表单元素的文本
    console.log($("div").html());

    // 设置非表单元素的文本
    $("div").html("啊聚集到");
</script>
```

### 4.节点属性

```
attr:获取节点的属性值，也可以修改节点的属性值
// 获取属性值
console.log($("input:eq(1)").attr("type"));

// 修改属性值
$("input:eq(1)").attr("type", "text");

// 获取图片属性值
console.log($("img").attr("src"));

// 修改图片属性值
$("img").attr("src", "img/2.jpg");
```

### 5.节点样式

```
css()方法，里面传递一个json格式的数据，使用链式语法
	$("div").css({"color": "red", "background":"cyan", "fontSize": 40});
```

### 6.jQuery独有选择器

```
:first:获取节点匹配的第一个元素
:last:获取节点匹配的第二个元素
:odd:匹配奇数
:even:匹配偶数
:gt(index)：获取匹配节点大于某一个索引值
:lt(index): 获取匹配节点小于某一个索引值
:eq(index): 获取匹配节点，某一个准确索引值节点
```

### 7.jQuery节点关系

```
parent:获取到某一个匹配节点的父节点
siblings:获取兄弟姐妹节点
children:获取某个节点的子节点
this:上下文，当前的节点
```

### 8.jQuery事件的绑定

```
jQuery事件的绑定，没有on这个关键字
绑定单击事件:
	$(selector).click(function(){
	函数执行的内容;
	});
绑定的事件有:
    mouseenter(鼠标进入)
    mouseleave(鼠标离开)
```

### 9.animate动画函数

```
语法格式：
	$(selector).animate(json, time, callback);
    第一个参数【必有】：JSON格式用来设置动画最终完成的样式属性值
    第二个参数【可有可无】:动画时间的设置 单位毫秒
    第三个参数【可有可无】:当动画执行完毕后立即执行一次
注意：
    ① animate函数很多属性都支持，但是颜色属性不支持
    ② 节点的可以绑定多个动画，按照书写顺序依次完成
```

### 10.动画积累问题

```
解决动画积累问题  在动画函数前面加上stop(true)
```

```html
<script type="text/javascript">
    // 解决动画积累问题  在动画函数前面加上stop(true)
    // 给第一个按钮绑定单击事件
    $("button:eq(0)").click(function () {
        $("div").stop(true).animate({"left": 200});
    });

    // 给第二个按钮绑定单击事件
    $("button:eq(1)").click(function () {
        $("div").stop(true).animate({"left": 0});
    });
</script>
```

### 11.传统轮播图

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>传统轮播图</title>
    <link rel="stylesheet" href="css/default.css">
    <script src="js/jQuery.min.js"></script>
</head>
<body>
<div class="container">
    <ul>
        <li class="cur"><img src="img/0.jpg" alt=""></li>
        <li><img src="img/1.jpg" alt=""></li>
        <li><img src="img/2.jpg" alt=""></li>
        <li><img src="img/3.jpg" alt=""></li>
        <li><img src="img/4.jpg" alt=""></li>
    </ul>
    <button class="lbtn">&lt;</button>
    <button class="rbtn">&gt;</button>
    <ol>
        <li class="show">1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
    </ol>
</div>
</body>
</html>
<script>
    // 定义一个信号量
    var index = 0;

    // 给左侧按钮绑定单击事件
    $(".lbtn").click(function () {
        // 当前展示的图片
        $("li:eq(" + index + ")").css({"left": 0}).stop(true).animate({"left": -600}, 500);
        index++;
        index = index > 4 ? 0 : index;
        // 下一张展示的图片
        $("li:eq(" + index + ")").css({"left": 600}).stop(true).animate({"left": 0}, 500);

        // 小球的颜色改变  将兄弟节点的颜色去掉
        $("ol li:eq(" + index + ")").addClass("show").siblings().removeClass("show");
    });

    // 右侧按钮绑定单击事件
    $(".rbtn").click(function () {
        // 当前展示的图片
        $("li:eq(" + index + ")").css({"left": 0}).stop(true).animate({"left": 600});
        index--;
        index = index < 0 ? 4 : index;

        // 下一张图片  当前图片的小球展示 兄弟节点的小球不展示
        $("li:eq(" + index + ")").css({"left": -600}).stop(true).animate({"left": 0});

        // 小球的颜色
        $("ol li:eq(" + index + ")").addClass("show").siblings().removeClass("show");
    });

    setInterval(
        function () {
            // 当前展示的图片
            $("li:eq(" + index + ")").css({"left": 0}).stop(true).animate({"left": -600}, 500);
            index++;
            index = index > 4 ? 0 : index;
            // 下一张展示的图片
            $("li:eq(" + index + ")").css({"left": 600}).stop(true).animate({"left": 0}, 500);

            // 小球的颜色改变  将兄弟节点的颜色去掉
            $("ol li:eq(" + index + ")").addClass("show").siblings().removeClass("show");
        }, 5000
    );
</script>
```



default.css

```css
* {
    margin: 0;
    padding: 0;
}

.container {
    width: 600px;
    height: 400px;
    position: relative;
    margin: 30px auto;
    border: 1px solid black;
    overflow: hidden;
}


ul {
    list-style: none;
}

ul li {
    position: absolute;
    left: 600px;
}

ul li.cur {
    left: 0;
}

.lbtn {
    position: absolute;
    width: 30px;
    left: 0;
    top: 48%;
    cursor: pointer;
}

.rbtn {
    position: absolute;
    width: 30px;
    right: 0;
    top: 48%;
    cursor: pointer;
}

ol {
    position: absolute;
    list-style: none;
    width: 150px;
    height: 20px;
    left: 40%;
    bottom: 10px;
}

ol li {
    width: 20px;
    height: 20px;
    float: left;
    background: white;
    margin-right: 5px;
    border-radius: 50%;
    text-align: center;
}

ol li.show {
    background: #2bc;
    color: white;
}

.container ul li img {
    width: 600px;
    height: 400px;
}
```



### 12.淡入淡出轮播图

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>淡入淡出轮播图</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .ddd {
            position: relative;
            width: 400px;
            height: 400px;
            margin: 30px auto;
            border: 1px solid black;
            overflow: hidden; /* 溢出隐藏*/
        }

        ul {
            position: absolute;
            width: 100%;
            height: 100%;
            list-style: none;
        }

        img {
            width: 400px;
            height: 400px;
        }

        .lt {
            position: absolute;
            left: 0;
            top: 200px;
        }

        .gt {
            position: absolute;
            right: 0;
            top: 200px;
        }

        button {
            width: 30px;
            cursor: pointer; /*小手*/
        }
    </style>
    <script src="js/jQuery.min.js"></script>
</head>
<body>
<div class="ddd">
    <ul>
        <li><img src="img/0.jpg" alt=""></li>
        <li><img src="img/1.jpg" alt=""></li>
        <li><img src="img/2.jpg" alt=""></li>
        <li><img src="img/3.jpg" alt=""></li>
        <li><img src="img/4.jpg" alt=""></li>
    </ul>
    <button class="lt">&lt;</button>
    <button class="gt">&gt;</button>
</div>

</body>
</html>
<script>
    var i = 0;
    $(".lt").click(function () {
        // 图片淡出
        $("li:eq(" + i + ")").fadeOut(1000, function () {
            i++;
            i = i > 4 ? 0 : i;
            // 下一张图片淡入
            $("li:eq(" + i + ")").fadeIn(1000);
        });
    });

    $(".gt").click(function () {
        // 图片淡出
        $("li:eq(" + i + ")").fadeOut(1000, function () {
            i--;
            i = i < 0 ? 4 : i;
            // 下一张图片淡入
            $("li:eq(" + i + ")").fadeIn(1000);
        });
    });
</script>
```



## 五. JSON数据格式

```
json是键值对格式  键需要加上双引号 值可以是任意类型
```

```html
<script>
var info = {
	    "name": "ene",
	    "age": 123
	}
	
	// 读取json数据
	console.log(info.name);
	console.log(info.age);
	console.log(info["name"]);
	console.log(info["age"]);
	
	// 修改json数据
	info.name="eee";
	info["age"] = 1211;
	console.log(info)
	
	// json添加键值对
	info.sex="男";
	console.log(info);

</script>
```

## 六.switch语句

```
格式：
		switch (变量){
			case 条件1:
				代码块;
			break;
			case 条件2:
				代码块;
			break;
			case 条件n:
				代码块;
			break;
			default:
				代码块;
			break;
		}
```

## 七. 闭包

```
闭包：一个可以访问其他作用域中的变量的函数称为闭包
```

```html
<script>
	    function func(x) {
	        console.log("这是外部函数");
	        // 内部函数
	        function inner(y) {
	            console.log("内部函数执行");
	            console.log(x + y);
	        }
	
	        inner(200);
	    }
	
	    func(100);
	</script>
```

## 八.JS变量

```
(1)命名规范
		① 可以是数字，字母，下划线，美元符号
		② 不能以数字开头
		③ 不可以是关键字，保留字
(2)变量在声明后，没有赋值，初始值为undefined
(3)声明变量，提升到当前作用域最上方
```

## 九.JS函数

### (1)IIFE

​	

```
IIFE:在声明表达式函数的同时立刻马上执行一次,每一个IIFE都有自己独立的作用域，相互不影响
		var fun = function(){
			console.log(表达式函数执行"");
		}();
```

### (2)关键字形式的函数变为表达式函数的方法

```
关键字形式的函数变为表达式函数的方法
			①  +号可以将关键字形式的函数转为表达式形式的函数 在关键字形式的函数前面加+
			②  -号可以将关键字形式的函数转为表达式形式的函数 在关键字形式的函数前面加-
			③  !号可以将关键字形式的函数转为表达式形式的函数 在关键字形式的函数前面加!
			④  ()号可以将关键字形式的函数转为表达式形式的函数  用()将关键字形式的函数进行包裹
		+function fun1() {
			console.log("+号可以将关键字形式的函数转为表达式形式的函数");
		}();
		
		-function fun2() {
			console.log("-号可以将关键字形式的函数转为表达式形式的函数");
		}();
		
		!function fun3() {
			console.log("!号可以将关键字形式的函数转为表达式形式的函数");
		}();
		
		(function fun4() {
			console.log("()号可以将关键字形式的函数转为表达式形式的函数");
		})();
```

### (3)表达式形式的函数【匿名函数】

```
var fun = function(){
			console.log("这是表达式形式的函数");
		}
	fun();  // 调用
```

### (4)递归函数  自己调用自己

```html
<script>
		    function fuc() {
		        console.log("递归");
		        fuc();
		    }
		</script>
```

### (5)关键字形式的函数与表达式形式的函数的区别

```
① 表达式形式的函数不可以在函数声明之前进行调用
② 关键字形式的函数可以在函数声明之前进行调用,解析器会将函数的声明提升到当前作用域的最上方
```

### (6)计算100-1000之间的水仙花数

```
Math对象     Math.pow 立方   parseInt 取整
function isshuixianhua(num) {
	var ge = num % 10;
	var shi = parseInt(num / 10) % 10;
	var bai = parseInt(num / 100);
	var result = Math.pow(ge, 3) + Math.pow(shi, 3) + Math.pow(bai, 3);
		// console.log(result);
	if (result == num) {
		return true;
		} else {
				return false;
		}
	}
```

### (7)回调函数

```
一个函数作为另一个函数的参数，这样的函数称为回调函数
		function pormise(a, b, callback) {
		    callback();
		}
		
		pormise(1, 2, function () {
		    console.log("回调函数调用");
		})
```

### (8)类数组对象arguments

```
函数体中拥有一个引用数据类型arguments【类数组对象】
类数组对象不是数组，只能使用数组的length属性，不能使用方法
存在意义：
		在函数没有形参的情况下，在函数体中可以获取到传递给函数的实参
```

## 十.三元运算符

```
三元运算符: A?B:C 如果A为真，返回B，否则返回C
```

## 十一.数据类型

```
① 数据类型的判断
    typeof检测数据的类型
    空对象类型 null   Null类型 返回object
			
② 数据类型的转换
    内置函数 parseInt 将字符串中的数字转为数字  精确到整数
    内置函数 parseFloat	 将字符串中的数字转为数字  精确到小数
    NaN和0会隐式转为布尔值为false,其他数字为true
    空字符   ---- > false
    非空字符串 ---> true
    未定义类型和Null转为布尔值 都为false
```

## 十二.数学对象

```
console.log(Math.PI);
console.log(Math.E);
	
// 获取数字的绝对值
console.log(Math.abs(122));

// 获取一个数字的N次幂
console.log(Math.pow(3,8));

// 随机一个0到1之间的小数
console.log(Math.random(0,1));
```

## 十三.数组

```
js使用[]表示数组
数组中可以存储任意类型的数据
可以将数组赋值给变量
读取数据:可以使用枚举法获取数据里的元素 元素的索引越界，程序不会报错，返回undefined

// 修改数据
arr1[1] = "号";
console.log(arr1);
		
// 添加数据
arr1[5] = false;
console.log(arr1);
```

### 数组常用的方法和属性

```
获取数组的长度 length
push:数组尾处添加一个或多个元素
pop:数组尾处移除一个元素
unshift：数组的头部添加一个或者多个元素
shift:数组头部移除一个元素
join: 将数组转为字符串
reverse:将数组元素倒置
indexOf:索引值  获取数组元素的索引值  如果获取的元素不在数组中，返回-1
includes:包含   检测当前是否在数组中，如果存在返回true,否则返回false
slice:从起始数组当中切割出一个新的数组  slice(起始索引值，结束索引值)  对原数组没有影响
包含起始位置的元素，不包含结束位置的元素
splice:可以对数组进行切割， 插入，替换 对原数组有影响
传递两个参数:第一个参数是起始位置的索引值，第二个代表要切割的长度
```

```html
<script>
			    var arr = [1, 2, 3, 5, 6, 7];
			    console.log(arr.length);  // 获取数组的长度 length
			</script>
			<script>
			    var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
			    for (i = 0; i < arr.length; i++) {
			        console.log(arr[i]);
			    }
			</script>
			<script>
			    /*
			    * push:数组尾处添加一个或多个元素
			    * pop:数组尾处移除一个元素
			    *
			    * */
			    var arr = [1, 2, 3, 4, 5, 6, 6, 7];
			    arr.push(56);
			    arr.push("4", 'g');
			    arr.pop();  // 删除数据的最后一个元素
			    console.log(arr);
			    console.log("-----------------------------");
			</script>
			
			<script>
			    /*
			    *  unshift：数组的头部添加一个或者多个元素
			    *  shift:数组头部移除一个元素
			    *
			    * */
			    var arr = [12, 3, 4, 5, 6, 7, 8, 9];
			    arr.unshift("哈哈");
			    arr.unshift("hao", "gh", "ghhhh");
			    // arr.shift("ghhhh");
			    arr.shift();   // 删除数据的第一个元素
			    console.log(arr);
			    console.log("------------------------------");
			</script>
			
			<script>
			    /*
			    *  join: 将数组转为字符串
			    *   reverse:将数组元素倒置
			    *
			    * */
			    var arr = [1, 2, 3, 4, 5, 6, 7, 8];
			    var str = arr.join("*");
			    var str1 = arr.join("");
			    console.log(str1);
			    console.log(str);
			    console.log("*********************");
			    var arr1 = [1, 2, 3, 4, 5];
			    arr1.reverse();
			    console.log(arr1);
			    console.log("==========================");
			</script>
			
			<script>
			    /*
			    *  indexOf:索引值  获取数组元素的索引值  如果获取的元素不在数组中，返回-1
			    *  includes:包含   检测当前是否在数组中，如果存在返回true,否则返回false
			    * */
			    var arr = [1, 2, 3, 4, 5, 6];
			    console.log(arr.indexOf(1));
			    console.log(arr.indexOf(7));
			    console.log(arr.includes(1));
			    console.log("------------------------");
			</script>
			
			<script>
			    /*
			    *  slice:从起始数组当中切割出一个新的数组  slice(起始索引值，结束索引值)  对原数组没有影响
			    *       包含起始位置的元素，不包含结束位置的元素
			    *  splice:可以对数组进行切割， 插入，替换 对原数组有影响
			    *       传递两个参数:第一个参数是起始位置的索引值，第二个代表要切割的长度
			    * */
			    var arr = [1, 2, 3, 4, 5];
			    var new_arr = arr.slice(3);
			    console.log(new_arr);
			    var new_arr1 = arr.slice(2, 4);  // 3,4
			    console.log(new_arr1);
			    console.log("-----------------------------------------");
			
			    // splice
			    var arr1 = [1, 2, 4, 5, 6, 67];
			    // 切割
			    // var newArr = arr1.splice(2);
			    // console.log(newArr);
			    console.log("=============================================");
			    // var newArr1 = arr1.splice(2,3);
			    // console.log(newArr1);
			
			    // 插入  没切割出来进行添加
			    // var arr_ = arr1.splice(2,0,"哈哈");
			    // console.log(arr_);
			    // console.log(arr1);
			
			    // 替换   切割出来进行替换
			    var newArr = arr1.splice(2, 2, "好", "en");
			    console.log(newArr);
			    console.log(arr1);
			</script>
```

## 十四.循环语句

### (1) break语句

```html
<script>
		    for (var m = 1; m <= 6; m++) {
		        console.log(m);
		        if (m % 2 == 0) {
		            break
		        }
		    }
</script>
```

### (2) do-while语句

```
格式:
		   do{
		   循环体;
		 }while(判断条件);
		 
		do{
		     var a = parseInt(Math.random()*10);
		     var b = parseInt(Math.random()*10);
		 }while (a==0&&b==0);
		console.log(a,b);
```

### (3) while语句

```
格式:
		   条件一般为布尔值
		   while (条件){
		       循环体;
		 }
		var i = 1;
		while (i <= 10) {
		    if (i%2==0){
		        console.log(i);
		    }
		    i++;
		}
```

## 十五.正则表达式

### (1)边界符

```
^ :开头
$ :结尾
	var str = "wev哈哈哈哈哈";
	console.log(/^wev/.test(str));
	console.log(/哈哈$/.test(str));
```

### (2)分组与汉字

```
分组：()  ()中的内容为一个整体
汉字：[\u4e00-\u9fa5]
		 
var str = "adfa";
console.log(/(a){1}/.test(str));
		 
var str_ = "哈哈哈哈哈111";
console.log(str_.replace(/[\u4e00-\u9fa5]+/g, "k"));
```

###  (3)量词

```
{n}  硬性量词  对应零次或者n次
{n,m} 软性量词  至少出现n次但不超过m次（中间不能有空格）
{n,}  软性量词  至少出现n次
?      软性量词 出现零次或者一次
*       软性量词  出现零次或者多次（任意次）
+       软性量词      出现一次或者多次（至少一次）
```

```html
<script>
// {n}  硬性量词  n代表数字
var str = "哈哈33456哈哈00000";
var arr = str.match(/\d{3}/g);
console.log(arr);
		
// 软性量词 {n, m}
var str_ = "34455法撒旦发生哦哦0 4456";
console.log(str_.replace(/\w{4,20}/g, "x"));
		
// 软性量词 {n,}
var str_r = "adt发噶魔法卡感觉撒酒疯8958650-";
var arr_ = str_r.match(/\d{1,}/g);
console.log(arr_);
</script>
```

### (4)修饰符

```
g: 全局匹配
i: 大小写不敏感匹配
		
var url = "https://www.baidu.com";
var arr = url.match(/[a-z]+/g);
console.log(arr);

var url_ = "hTTps://wWW.Xin.Com";
var arr_ = url_.match(/[a-z]+/ig);
console.log(arr_);
```

### (5)预定义类

```
\d  匹配任意的数字[0-9]
\D  匹配任意一个不是数字的字符
\s  匹配空白
\S  匹配任意不是空白的字符
\w  匹配任意的字母，下划线或者数字
\W  匹配任意的数字，字母下划线以外的内容
```

### (6)正则字符集

```
① 范围类:有时匹配的东西过多，类型又相同，全部输入太麻烦，可以在中间加个横线
			[0-9]  [A-Z]  [a-z]
			var str = "123456709哈哈哈，哈哈wc4564543543";
			var arr = str.match(/[0-9]+/g);
			console.log(arr);
		
② 简单类：把多个字符聚集在一起进行匹配，只能匹配某一个符合条件字符
			var str = "asdfaertyhfjakof";
			var arr = str.match(/[asd]er/g)
			console.log(arr);
		
③ 组合类：将多个范围类放在一起进行匹配
			var str = "A3455adfsafsadfas45456fdasf45FASFGSADFASF";
			var arr = str.match(/[A-Za-z0-9]+/)
			console.log(arr);
```

### (7)正则常用方法

```
正则表达式书写的时候是由//,这两个//称为定界符 属于引用数据类型
```

```
① 字符串split方法结合正则表达式使用
			var str = "ert rtt     tyyuuu    yyy";
			var arr = str.split(/\s+/);  // \s 一个空格  +多个
			console.log(arr);
		
② match:字符串方法，获取第一个符合条件的字符，并返回一个数组
			var str = "哈哈哈哈好啊好";
			console.log(str.match(/好/g))  // 匹配所有的好  g:修饰符，全局匹配  glob的简写
		
③ search:属于字符串方法，获取第一个满足条件的索引值
			var str = "adsafsadfs哈哈";
			console.log(str.search(/哈哈/));
		
④ replace 进行符合条件的字符串的替换
			var str = "爱得发疯阿斯顿发射点发射点范德萨";
			console.log(str.replace(/发/g, "fa"));   // 将所有的发替换为fa
			console.log("-----------------------------");
		
⑤ exec:在目标字符串中执行一次匹配 返回一个数组
⑥ test: 检测正则表达式当中的数据是否在目标字符串中 有返回true 否则返回false
			var str = "aaaabccccc";
			var reg = /abc/;
			console.log(reg.exec(str));  // 返回一个数组
			console.log("-----------==================");
			var str1 = "adfasdfsadfsfert8ew945ew4-859u";
			var reg1 = /zz/
			console.log(reg1.test(str1));
```

## 十六.字符串

```
字符串的属性和方法
		① length属性：获取到字符串总字符的个数
		② toLowerCase:将字符串中英文字母变为小写
		③ toUpperCase：将字符串中英文字母变为大写
		④ search:获取字符的索引值
		⑤ split:可以通过某一个字符，将字符串切割为一个数组
		⑥ substring: 在父串当中切割出一个子串  substring(起始索引值, 结束索引值)
				包含起始索引值，不包含结束索引值
		⑦ substr：从父串当中切割出一个子串
				substr(起始位置,切割长度);
		
		⑧ replace:替换某一个字符串中符合条件的字符进行替换
		⑨ match:将字符串中符合条件的第一个字符返回
```

## 十七.字面量

```
① 整数，浮点数
	// 小数注意事项  由于0.1和0.2在进行计算时，没办法整除，保留17位小数 遵循IEEE754浮点数算数标准
	console.log(0.1 + 0.2);
② 特殊值
		js中，数字有范围: -2^53 ~ 2^53,如果超出了这个范围，使用特殊值Infinity(无穷大)表示
		Infinity也有正负值之分
		console.log(Infinity);
		console.log(-Infinity);
		
NaN特殊值
			console.log(0/0);
			console.log(12/0);  // Infinity  分子不为0，分母为0，认为分子是趋近于0的数
```

# CSS笔记

```
小手：                  cursor: pointer;
溢出隐藏：               overflow: hidden;
元素放大效果：           transform: scale(1.8);
透明度：                 opacity: .3;
去除列表前的样式：        list-style: none;

清除页面中的多余的样式：
	* {
		margin: 0;
		padding: 0;
	}

隐藏元素： display: none;
显示元素： display: block;
圆角  border-radius: 10px 10px 10px 10px; 
margin  外边距
padding  内边距
text-decoration: none;  去掉下划线
```

## 1.CSS三种书写方式

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<!-- 样式优先级：就近原则 -->
		<!-- ② 内部样式 在head标签中加入style标签，定位到需要修饰的元素，然后加{}中加入需要修饰的样式 -->
		<style>
			h2{
				color: aliceblue;
				font-family: 宋体;
			}
		</style>
		<!-- ③ 外部样式(用的最多) -->
		<link rel="stylesheet" type="text/css" href="css/mystyle.css"/>
	</head>
	<body>
		<!-- 
		 ① 书写方式：内联样式(行内样式)
		 在标签中加入一个style属性，css的样式作为属性值
		 多个属性值使用;进行拼接
		 -->
		<h1 style="color: pink;font-family: 宋体;">这是一个标题</h1>
		<h2>这是二级标题</h2>
		<h3>这是三级标题</h3>
	</body>
</html>
```

## 2.CSS选择器

### (1)关系选择器

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style>
			/* 
			 关系选择器:
				后代选择器,只要是这个元素的后代，样式都会改变
			 */
			/* div h1{
				color: red;
			} */

			/* 
			 关系选择器：子代选择器
			 只改变子标签的样式
			 */
			div>h1 {
				color: #FFC0CB;
			}
			span>h1{
				color: red;
			}
		</style>
	</head>
	<body>
		<div>
			<h1>一级标题</h1>
			<h1>一级标题</h1>
			<h1>一级标题</h1>
			<h1>一级标题</h1>
			<span>
				<h1>一级标题</h1>
				<h1>一级标题</h1>
				<h1>一级标题</h1>
				<h1>一级标题</h1>
			</span>
		</div>
	</body>
</html>
```

### (2)基本选择器

```
选择器的优先级：
	id选择器>类选择器>元素选择器
```



```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style>
			/* 选择器的优先级：id选择器>类选择器>元素选择器 */
			/* 
			 基本选择器：元素选择器:
			 通过元素的名字进行定位，获取页面上所有的这个元素,无论藏得多深，都能获取到
			 */
			h1{
				color: red;
			}
			i{
				color: gray;
			}
			
			/* 
			 基本选择器：类选择器
			 应用场景：不同类型的标签使用相同的类型
			 */
			.mycls{
				color: pink;
			}
			
			/* 基本选择器：id选择器
			 应用场景：可以定位唯一的一个元素
			 不同的标签可以使用相同的id，但是一般会进行控制，让id唯一定位到一个元素
			 */
			#myid{
				color: bisque;
			}
		</style>
	</head>
	<body>
		<h1>
			一级<i>标题</i>
		</h1>
		<h1 class="mycls">一级标题</h1>
		<h2 class="mycls">二级标题</h2>
		<h2>二级标题</h2>
		<h2 id="myid">二级标题</h2>
	</body>
</html>
```

### (3)属性选择器

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<!-- 属性选择器 -->
		<style type="text/css">
			input[type="text"]{
				background-color: #FF0000;
			}
			input[type="password"]{
				background-color: green;
			}
		</style>
	</head>
	<body>
		<form>
			用户名: <input type="text" value="python"/>
			密码: <input type="password" value="111"/>
			<input type="submit"  value="登录"/>
		</form>
	</body>
</html>
```

### (4)伪类选择器

```
伪类选择器：向某些选择器添加特殊效果，一般伪类选择器用在超链接上
    hover:鼠标悬浮在上面，颜色改变
    link:设置静止状态
    hover:设置鼠标悬浮状态
    active:设置触发状态
    visited:设置完成状态
```

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style type="text/css">
			/* 
			伪类选择器：向某些选择器添加特殊效果
			一般伪类选择器用在超链接上
			hover:鼠标悬浮在上面，颜色改变
			
			 */
		/* 	h1:hover {
				color: yellow;
			} */
			/* 设置静止状态 */
			a:link{
				color: red;
			}
			/* 设置鼠标悬浮状态 */
			a:hover{
				color: yellow;
			}
			/* 设置触发状态 */
			a:active{
				color: burlywood;
			}
			/* 设置完成状态 */
			a:visited{
				color: #008000;
			}
		</style>
	</head>
	<body>
		<h1>标题</h1>
		<a href="index.html">超链接</a>
	</body>
</html>
```

## 3.浮动

```
float:left;
```

### 3.1消除浮动的影响

```
外层div使用浮动需要考虑影响，看看是否对其他的元素有影响
消除浮动的影响 
    方式一：给浮动的父节点加入属性：overflow: hidden;
    方式二：给浮动的父节点加上高的属性
    方式三: 操作被影响的元素 加入属性 clear: both;
```

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<!-- 外层div -->
		<!-- 
		 使用浮动需要考虑影响，看看是否对其他的元素有影响
		 -->
		<!-- 
		  消除浮动的影响 
			方式一：给浮动的父节点加入属性：overflow: hidden;
		    方式二：给浮动的父节点加上高的属性
			方式三: 操作被影响的元素 加入属性 clear: both;
		  -->
		<!-- <div style="background-color: pink;overflow: hidden;"> -->
		<div style="background-color: pink;">
			<div id="div01" style="width: 100px; height: 100px; background-color: aquamarine; float: left;">11</div>
			<div id="div02" style="width: 200px; height: 200px; background-color: royalblue;float: left;">22</div>
			<div id="div03" style="width: 300px; height: 300px; background-color: gray;float: left;">33</div>
		</div>
		<div style="width: 500px; height: 500px;background-color: chartreuse;clear: both;"></div>
	</body>
</html>
```

## 4.定位

### 4.1固定定位

```
position: fixed;
```

### 4.2静态定位

```
静态定位：
		如果不写position属性，默认就是静态定位
		静态效果:元素出现在本该出现的位置  一般使用静态可以直接省略不写
```

### 4.3绝对定位

```
元素设置了绝对定位，会一层一层向上找父级是否有定位，如果直到找到了body还没有找到定位
那么就相对于body进行变化；如果父级节点有定位(绝对定位,相对定位,固定定位),一般配合使用父级为相对定位，当前元素为绝对定位，这样这个元素就会相对于父级位置进行变化。无论使用哪一种，都会释放原来的位置,然后其他元素就会占用那个位置。
建议使用：
    父级：相对定位  relative
    子级：绝对定位  absolute
```

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style type="text/css">
			#outer{
				width: 500px;
				height: 500px;
				background-color: pink;
				margin-left: 300px;
				position: relative;
			}
			#div01{
				width: 100px;
				height: 100px;
				background-color: yellow;
				position: absolute;
				left: 10px;
				top: 30px;
			}
			
			#div02{
				width: 100px;
				height: 100px;
				background-color: aliceblue;
			}
		</style>
	</head>
	<body>
		<!-- 
		 元素设置了绝对定位，会一层一层向上找父级是否有定位，如果直到找到了body还没有找到定位
		 那么就相对于body进行变化；如果父级节点有定位(绝对定位,相对定位,固定定位),
		 一般配合使用父级为相对定位，当前元素为绝对定位，这样这个元素就会相对于父级位置进行变化。
		 无论使用哪一种，都会释放原来的位置,然后其他元素就会占用那个位置。
		 建议使用：
			父级：相对定位  relative
			子级：绝对定位  absolute
		 -->
		<div id="outer">
			<div id="div01">111</div>
			<div id="div02">222</div>
		</div>
	</body>
</html>
```

### 4.4相对定位

```
相对定位
相对元素自身所在的位置进行定位，可以设置left,right,bottom,top四个属性
效果：在进行相对定位的后，元素原来所在的位置被保留了，被占用了  其他元素的位置不会发生改变
一般情况下，left和right不会同时使用，bottom和top不会同时使用,选择一个方向即可
优先级：左上>右下
相对定位的应用场景：
			① 元素在小范围内移动使用
			② 结合绝对定位使用
属性:z-index
		   设置堆叠顺序，设置元素谁上谁下
		   注意：z-index要设置在定位的元素上
```

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<!-- 
		 相对定位
		 相对元素自身所在的位置进行定位
		 可以设置left,right,bottom,top四个属性
		 效果：在进行相对定位的后，元素原来所在的位置被保留了，被占用了  其他元素的位置不会发生改变
		 一般情况下，left和right不会同时使用，bottom和top不会同时使用,选择一个方向即可
		 优先级：左上>右下
		 -->
		 <!-- 
		  相对定位的应用场景：
			① 元素在小范围内移动使用
			② 结合绝对定位使用
		  -->
		  <!-- 
		   属性:z-index
		   设置堆叠顺序，设置元素谁上谁下
		   注意：z-index要设置在定位的元素上
		   -->
		<div style="width: 500px;height: 500px; background-color: aliceblue;">
			<div style="width: 100px; height: 100px; background-color: aqua;position: relative;left: 10px;z-index: 50;"></div>
			<div style="width: 100px; height: 100px; background-color: yellow; position: relative;bottom: 10px;right: 20px;z-index: 10;"></div>
			<div style="width: 100px; height: 100px; background-color: pink;"></div>
		</div>
	</body>
</html>
```

## 5.盒模型

### 5.1盒子

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style type="text/css">
			div{
				width: 100px;
				height: 100px;
				background-color: gray;
				margin-left: 100px;
				border: 4px red solid;
			}
		</style>
	</head>
	<body>
		<div>我是div</div>
	</body>
</html>
```

### 5.2盒子代码

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style type="text/css">
			/* 将页面上所有的外边距，边框，内边距设置为0 */
			*{
				margin: 0px;
				border: 0px;
				padding: 0px;
			}
			#outer{
				width: 440px;
				height: 450px;
				background-color: aliceblue;
				margin-left: 100px;
				margin-top: 100px;
				padding-top: 50px;
				padding-left: 60px;
			}
			#mydiv{
				width: 200px;
				height: 200px;
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div id="outer">
			<div id="mydiv">我是div</div>
		</div>
	</body>
</html>
```



# HTML笔记

## 1.head标签的内容

### (1) 设置页面编码，防止乱码

```html
<meta charset="utf-8" />
```

### (2)页面标题

```html
<title>hello，你好</title>
```

### (3)页面刷新效果  3秒刷新到百度首页

```html
<meta http-equiv="refresh" content="3;https://www.baidu.com" />
```

### (4)页面作者

```html
<meta name="author" content="msb;23456465e@qq.com" />
```

### (5)设置页面搜索的关键字 

```html
<meta name="keywords" content="hello; 线上; 书籍" />
```

### (6)页面描述

```html
<meta name="description" content="详情页" />
```

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
		<!-- <meta name="au" content=""/> -->
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

## 2.表格标签

```
table:表格
tr:行
td:单元格
th:表头 效果:加粗，居中
默认情况下，表格下没有边框,可以通过属性增加边框
border:设置边框大小
cellspacing:设置边框与单元格之间的间隙
background:设置背景图片
bgcolor:设置背景颜色
rowspan:行合并
colspan:列合并
横着的是列合并
竖着的是行合并
```

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>表格</title>
	</head>
	<body>
		<!-- 表格 
		table:表格
		tr:行
		td:单元格
		th:表头 效果:加粗，居中
		默认情况下，表格下没有边框,可以通过属性增加边框
		border:设置边框大小
		cellspacing:设置边框与单元格之间的间隙
		background:设置背景图片
		bgcolor:设置背景颜色
		rowspan:行合并
		colspan:列合并
		横着的是列合并
		竖着的是行合并
		-->
		<table border="1px" cellspacing="0px" width="400px" height="300px" background="img/壁纸.jpg" bgcolor="aliceblue">
			<tr bgcolor="aqua">
				<th>学号</th>
				<th>姓名</th>
				<th>年龄</th>
				<th>成绩</th>
			</tr>
			<tr align="center">
				<td>001</td>
				<td>张三</td>
				<td>23</td>
				<td rowspan="3">99</td>
			</tr>
			<tr align="center">
				<!-- <td>002</td> -->
				<td colspan="2">李四</td>
				<td>22</td>
				
			</tr>
			<tr align="center">
				<td>003</td>
				<td>王五</td>
				<td>21</td>
				
			</tr>
		</table>
	</body>
</html>
```

## 3.超链接标签

```
href:跳转的位置
target:_self 自身页面打开 （默认）  _blank 空白页面打开
```

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

## 4.超链接设置锚点

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

## 5.多媒体标签

### 5.1图片标签

```
src:引入图片的位置 引入本地资源
width:设置高度
	注意：一般高度和宽度只设置一个即可，另一个会按照比例自动设置
title：鼠标悬浮在图片上的提示语，默认情况下（没有设置alt属性）图片加载失败那么提示语title的内容
```

### 5.2音频标签

```html
<embed src="music/鹿先森乐队%20-%20春风十里.mp3" type="">
```

### 5.3 视频标签

```html
<embed src="//player.video.iqiyi.com/4ca1496a17b3c9486ad541503f1e52df/0/0/v_19rqsgc8to.swf-albumId=1654878400-tvId=1654878400-isPurchase=0-cnId=undefined" allowFullScreen="true" quality="high" width="480" height="350" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>
```

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

## 6.列表标签

### 6.1无序列表

```
无序列表 
type：设置列表前图标的样式 有三种样式
想要更换图标样式，需要借助css，style="list-style:url(图片地址);"
```

### 6.2有序列表

```
有序列表
type:设置列表的标号：1,I,A
start:设置起始位置
```

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

## 7.内嵌框架

```
内嵌框架：用于在网页中嵌入一个网页并让它在网页中进行展示
语法：
	<iframe name=""></iframe>
	src:默认内容，可以是图片，也可以是一个网页
```

```html
<!DOCTYPE html>
<html>
	<!-- 内嵌框架
	内嵌框架：用于在网页中嵌入一个网页并让它在网页中进行展示
	语法：
		<iframe name=""></iframe>
	 -->
	<head>
		<meta charset="utf-8">
		<title>内嵌框架</title>
	</head>
	<body>
		<iframe src="武器列表.html" width="30%" height="700px"></iframe>
		<!-- 创建一个内嵌框架 
		src:默认内容，可以是图片，也可以是一个网页
		-->
		<iframe name="my_iframe" width="68%" height="700px" src="img/壁纸.jpg"></iframe>
	</body>
</html>
```

## 8.其他页面使用锚点

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

## 9.文本标签

### 6.1标题标签

```
h1-h6  字号逐渐变小,自带换行  h7后属于无效标签
```

### 6.2横线标签

```
width:设置宽度
300px: 固定宽度
30%:  页面宽度的百分比，随着页面宽度变化而变化
align: 设置位置  默认不写居中
<hr width="300px" align="left"/>
```

### 6.3段落标签

```
段落效果：自动换行，段落与段落之间有空行
&emsp;:换行  比&nbsp换行大
&lt;:< 
&gt;:>
&copy ©
```

### 6.4加粗，倾斜，下划线

```html
<b>加粗</b>
<i>倾斜</i>
<u>下划线</u>
<u><i><b>加粗倾斜下划线</b></i></u>
```

### 6.5预编译标签

```
预编译标签:在页面上显示原样效果
<pre>
			public static void main(String[] args){
				System.out.println("Hello Word")；
			}
</pre>
```

### 6.6换行

```
<br>
```

### 6.7一箭穿心

```html
<del>你好，哈哈</del>
```

### 6.8字体标签

```html
<font color="antiquewhite" size="7">边界框内的像素</font>
```

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
		&copy ©
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

## 10.框架集合

```
框架集合:和body是并列的概念，不要将框架集合放入body中
```

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title></title>
</head>
<!-- 框架集合:和body是并列的概念，不要将框架集合放入body中 -->
<!-- rows="20%, *, 30%" 按行切割  上面的占20%，下面占30%，*代表中间剩余的部分 -->
<frameset cols="" rows="20%, *, 30%">
    <frame src="">
    <frameset cols="30%, 40%, *">
        <frame src="">
        <frame src="">
        <frame src="">
    </frameset>
    <frameset cols="50%, *">   <!-- 按列切割 第一个框架50%  -->
        <frame src="">
        <frame src="">
    </frameset>
</frameset>
</html>
```

## 11.form表单

### 11.1 form表单

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<!-- 定义一个form表单 -->
		<form action="" method="get">
			用户名：<input type="text" name="username"> <br>
			密码: <input type="password" name="password"> <br>
			提交： <input type="submit">
		</form>
	</body>
</html>
```

### 11.2 表单元素

#### (1) 表单元素

```html
文本框：使用广泛
表单元素必须有一个属性  name  用来提交数据
value属性：文本框中的具体内容
键值对：name=value
placeholder：提示语
readonly:只读  数据可以提交，不能修改数据
disabled:禁用  无法正常提交数据 无法修改数据
写法：
    readonly="readonly"
    readonly
    readonly="true"
```

#### (2)密码框

```html
<input type="password" name="password" >
```

#### (3)单选按钮

```
type="radio"
```

```
注意：一组单选按钮，必须通过name属性控制，让它们在一个分组里，然后在一个分组里只能选择一个
正常状态下，提交数据为gender=on,不同选项的value要进行区分   便于后台区分
默认选中：checked="checked"
```

```html
性别:
<input type="radio" name="gender" id="" value="0" checked="checked">男
<input type="radio" name="gender" id="" value="1">女
```

#### (4)多选按钮  name属性控制在同一个分组

```html
<input type="checkbox" name="lovebox" value="1" checked="checked">雷神
<input type="checkbox" name="lovebox" value="2" checked="checked">无影
<input type="checkbox" name="lovebox" value="3">火麒麟
<input type="checkbox" name="lovebox" value="4">毁灭
```

#### (5)文件

```html
<input type="file">
```

#### (6)隐藏域

```html
<input type="hidden" name="uname" value="123456">
```

#### (7)按钮

```html
<!-- 普通按钮 普通按钮没有什么效果,需要结合js-->
<input type="button" value="普通按钮">

<!-- 特殊按钮 重置按钮 将页面恢复到初始页面 -->
<input type="reset">

<!-- 图片按钮 -->
<img src="img/Screenshot_20190226-232915.jpg" alt="">
<input type="image" src="img/Screenshot_20190226-232915.jpg">
```

#### (8)下拉列表

```
selected="selected" 默认选中    multiple="multiple" 多选
```

```html
书籍列表
<select name="book" id="" multiple="multiple">
    <option value="0">---请选择---</option>
    <option value="1">《呐喊》</option>
    <option value="2">《彷徨》</option>
    <option value="3" selected="selected">《数据结构》</option>
    <option value="4">《算法刨析》</option>
</select>
```

#### (9)多行文本框  resize:none 大小不可变

```html
<textarea style="resize: none;" rows="10" cols="30">
				这里输入文字
</textarea>
```

#### (10)label标签

```
 一般会在想要获得焦点的标签上加入一个id属性，然后label中的for属性跟id配合使用
```

```html
<label for="uname">用户名：</label><input type="text" name="username3" id="uname">
```

#### (11) 提交按钮

```html
<input type="submit" value="提交">
```

### 11.3模拟百度搜索

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>百度一下，你就知道</title>
		<link rel="shortcut icon" href="https://www.baidu.com/favicon.ico" type="image/x-icon" />
	</head>
	<body>
		<form action="https://www.baidu.com/s" method="get">
			<input type="text" name="wd">
			<input type="submit" value="百度一下">
		</form>
	</body>
</html>
```

### 11.4 HTML5新增

```
email  html5增加了校验
<input type="email" name="email" id="" value="" />

url
<input type="url" name="" id="">

color
<input type="color" name="" id="">

number
min:最小值
max:最大值
step:步长
value:默认值，默认值一定在步长的范围中

range
1<input type="range" name="range" id="" min="1" max="10" step="3">10

日期
<input type="date">

月份
<input type="month">

星期
<input type="week">
```

#### html5新增属性

```
multiple:多选
placeholder:默认提示
autofocus:自动获取焦点
required:必填
<input type="text" autofocus="autofocus">
<input type="text" name="" id="" required="required">
<input type="submit" value="提交">
```

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<form action="" method="get">
			<!-- email  html5增加了校验 -->
			<input type="email" name="email" id="" value="" />
			
			<!-- url -->
			<input type="url" name="" id="">
			
			<!-- color -->
			<input type="color" name="" id="">
			
			<!-- number 
			min:最小值
			max:最大值
			step:步长
			value:默认值，默认值一定在步长的范围中
			-->
			<input type="number" name="" id="" min="1" max="10" step="3" value="4">
			
			<!-- range -->
			1<input type="range" name="range" id="" min="1" max="10" step="3">10
			
			<!-- 日期 -->
			<input type="date">
			
			<!-- 月份 -->
			<input type="month">
			
			<!-- 星期 -->
			<input type="week">
			<br>
			<br>
			<br>
			<br>
			<!-- html5新增属性
			 multiple:多选
			 placeholder:默认提示
			 autofocus:自动获取焦点
			 required:必填
			 -->
			<input type="text" autofocus="autofocus">
			<input type="text" name="" id="" required="required">
			<input type="submit" value="提交">
		</form>
		
	</body>
</html>
```

