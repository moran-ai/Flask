# Windows Node.js安装配置

**1.Node.js的下载**

[官网下载](https://nodejs.org/zh-cn/)



**下载长期支持版本**

![image-20201128203841199](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20201128203841199.png)





**2.安装Node.js**

安装过程 一直next就行，安装路径可以自定义



**3.检验是否安装成功**

进入cmd 

输入node - v

![image-20201128204110394](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20201128204110394.png)



输入npm -v

![image-20201128204130032](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20201128204130032.png)



**4.进行全局配置**

由于npm下载包的地址默认在C盘，所以要对下载地址进行配置

在node的安装路径新建两个文件夹  node_global  和 node_cache

![image-20201128204313462](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20201128204313462.png)

进行修改

npm config set prefix "E:\Nodejsstu\node_global"    引号里面跟着的是自定义的路径

npm config set cache "E:\Nodejsstu\node_cache"

![image-20201128204540032](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20201128204540032.png)

![image-20201128204552136](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20201128204552136.png)



修改完路径之后要进行环境变量的配置， 否则会发生报错  例如：在cmd中输入node,在交互命令中输入 requure('vue') 会出现模块没有找到的错误

下载包  

![image-20201128204932432](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20201128204932432.png)



使用下载的包

![image-20201128204718657](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20201128204718657.png)



**5.配置环境变量**

我的电脑  --->   属性 ---->  环境变量 

首先修改用户变量：

​	编辑path 

![image-20201128205047029](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20201128205047029.png)

将蓝色的那行修改

改为 node_global文件夹所在的路径

![image-20201128205154891](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20201128205154891.png)



然后修改系统变量

在系统变量里新建一个变量NODE_PATH  变量值为node_global\node_modules的路径

![image-20201128205300882](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20201128205300882.png)



然后进入系统变量的path中，添加一个新的变量%NODE_PATH%

![image-20201128205439666](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20201128205439666.png)



然后重新打开cmd，重新进行测试

![image-20201128205551923](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20201128205551923.png)

出现的这样的界面代表环境配置成功





视频教程

[B站Node.js安装配置教程](https://www.bilibili.com/video/BV11V411o7Zh/?spm_id_from=333.788.videocard.2)