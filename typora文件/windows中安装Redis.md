# windows中安装Redis

### 1.下载地址

```
https://github.com/tporadowski/redis/releases
```

### 2.安装

```
① 将下载好的文件解压到指定的文件夹
② 从解压的路径进入cmd，输入开启redis的命令:
	redis-server.exe redis.windows.conf
	出现这样的界面就代表开启服务成功
③ 连接redis服务，重新打开一个cmd,输入命令：
	redis-cli.exe
	出现这样的界面就代表连接redis服务成功
④ 将redis服务注册到windows服务中,输入命令：
	redis-server.exe --service-install redis.windows.conf --loglevel verbose
⑤ 配置redis环境变量
⑥ 设置redis的密码:
	进入redis后：
		输入命令: config set requirepass 密码
		登录输入密码：
			auth 密码
```

![image-20210320120621379](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20210320120621379.png)

![image-20210320120806067](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20210320120806067.png)

![image-20210320121043491](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20210320121043491.png)

