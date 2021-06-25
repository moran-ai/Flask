# Python实用小技巧

各位同学，大家下午好，接下来由我为大家分享五个python小知识，欢迎大家一起讨论交流

## 1.jupyter-notebook快捷键

```
jupyter-notebook快捷键
运行快捷键：
     shift+回车 运行并跳转到下一行
     Ctrl+回车  只运行光标所在行
     Alt+回车   运行光标所在行，并在跳转下一行之前插入一行
	 
删除快捷键：
     esc键进入命令行模式
     dd 删除光标所在行（必须在命令行环境下才行，编辑环境下不行，方框为蓝色是命令行环境，绿色是编辑环境)
	 
标题快捷键：
     设置标题：前面加上#号，输入标题内容，按esc键，然后按m键，shift+回车就行
     设置一级标题：#标题
     设置二级标题：##标题
     设置三级标题：###标题
	 
剪切，粘贴文件快捷键：（必须在命令行环境下操作）
       剪切：在所要剪切行按x键
       粘贴:v键，粘贴到所在行的下一行
	    shift+v键，粘贴到所在行的上一行
```

## 2.控制print函数不换行

Python3中的print()函数默认是换行的,可以在print函数中加入end=' ',让print()函数输出不会换行

```python
for i in a:
    print(i, end=' ')

1 2 3 4 5
```

## 3.导出Python环境中安装的所有模块名以及版本号到txt文件中

在终端中使用下面的命令将模块名及版本号导出到requirements.txt文件中

```pytohn
pip freeze > requirements.txt
```

想要在其他环境中使用这些包，可以使用下面的命令进行安装这些模块

```python
pip install -r requirements.txt  
```

## 4.Python链式调用

```python
def MultiPlicAtion(a, b):
    return a * b


def Add(a, b):
    return a + b


b = False
print((MultiPlicAtion if b else Add)(5, 7))
```

## 5.使用切片来删除列表中的某一段

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[1:5]=[]
print(a)
```

以上就是今天的python小知识分享的所有内容，这些小知识只要大家简单了解，有个印象，用到的时候可以查看python的官方文档，不需要死记硬背。小伙伴们先阅读消化一下，有不明白的地方，欢迎交流讨论。稍后媛媛老师会把整理好的文档发到群里，以便方便大家保存。