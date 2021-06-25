# Windows中配置CLion和MinGw

**1. MinGw的下载**

[MinGw下载地址](https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win64/Personal Builds/mingw-builds/)

拉到下面，下载

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191030231623538.png)

然后解压，得到这样的文件夹

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191030231631656.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTUxOTQ2Mw==,size_16,color_FFFFFF,t_70)



**2.下载CLion**

[CLion下载地址](https://www.jetbrains.com/clion/download/#section=windows)



**3.配置CLion**

打开CLion，左上角File-Settings-Build-Toolchains，然后点击 **+** 号，Environment选择MinGW，然后填入刚刚解压的MinGW64的路径

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191030231638964.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTUxOTQ2Mw==,size_16,color_FFFFFF,t_70)



然后就可以跑代码了。注意项目地址路径不能有中文，否则会报错。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191030231646144.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTUxOTQ2Mw==,size_16,color_FFFFFF,t_70)

