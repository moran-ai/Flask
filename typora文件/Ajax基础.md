# Ajax基础

**AJAX = Asynchronous JavaScript and XML (异步的JavaScript和XML)**

**AJAX是一种在无需重新加载整个网页的情况下，能够更新部分网页的技术。**

**Ajax不是一种新的编程语言，而是一种用于创建更好更快以及交互性更强的Web应用程序的技术。**





增强B/S的体验性



```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset='UTF-8'>
    <title> 伪造Ajax</title>
</head>
<body>
 	<div>
    	<p>请输入要加载的地址:</p>
        <p>
            <input type="text" id="url" value="">
            /* onclick 代表事件 */ 
            <input type="button" value="提交" onclick="">
        </p>
    </div>   
    
    <div>
        <h3>
            加载的页面的位置:
        </h3>
        /* iframe代表内联标签 */
        <iframe style="width: 100%; height:500px">
            
        </iframe>
    </div>
 </body>
</html>
```

