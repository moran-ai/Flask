# gitee

注册，然后登陆

新建一个远程仓库，复制远程仓库的地址

在本地建立一个仓库，进入cmd，进入本地仓库的地址

输入：git clone https://gitee.com/h-login/dongbao.git

然后进入.gitignore文件，然后添加.idea后缀,目的是忽视后缀为.idea的文件



进入Pycharm中创建一个项目，注意：**项目的创建路径需要选择本地仓库的路径**

创建项目后，然后在pycharm中选择VCS--->Git--->Remotes, 然后出现一个url， 然后点击OK





上传项目时，首先需要将本地.gitignore文件中所做的更改同步到gitee中

```
点击VCS--->commit
```

![image-20210625132937990](https://github.com/moran-ai/Flask/blob/main/image-20210625132937990.png)

然后点击Commit



在日志中可以看见刚刚提交的文件

![image-20210625133034425](https://github.com/moran-ai/Flask/blob/main/image-20210625133034425.png)



开始上传整个项目，在项目上右键，选择Git--->Add，目的是添加所有的文件到本地仓库

![image-20210625133214944](https://github.com/moran-ai/Flask/blob/main/image-20210625133214944.png)

点击Add以后，文件颜色会变成绿色

下面进行提交 Git  --- >  Commit Directory

![image-20210625133500114](https://github.com/moran-ai/Flask/blob/main/image-20210625133500114.png)

点击了提交会出现下面的窗口 在Commit message 中记录上传的状态，然后点击Commit旁边的下拉按钮，更新本地仓库和远程仓库的内容

![image-20210625133613309](https://github.com/moran-ai/Flask/blob/main/image-20210625133613309.png)

上传成功的界面如下

![image-20210625133838742](https://github.com/moran-ai/Flask/blob/main/image-20210625133838742.png)

对一个文件进行更新以后，只需要Add被修改的文件，然后上传即可

![image-20210625134337759](https://github.com/moran-ai/Flask/blob/main/image-20210625134337759.png)