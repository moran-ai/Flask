# Redis数据库

**Redis非关系型数据库**

## **1.1Redis介绍**

​	1.解决的问题

- 由于用户量增大，请求数据也随之增大，数据压力过大
- 多台服务器之间，数据不同步
- 多台服务器之间的锁，互斥性已经不存在了

Redis基于内存存储数据和读取数据

![image-20201215121539346](C:\Users\20622\AppData\Roaming\Typora\typora-user-images\image-20201215121539346.png)



### 1.2 NoSQL

```
Redis就是一款NoSQL
NoSQL--->非关系型数据库---->Not Only SQL
	1.key-Value:Redis。。。
	2.文档型：ElasticSearch, Solr, Mongodb。。。
	3.面向型： Hbase, Cassandra。。。
	4.图形化:Neo4j。。。
除了关系型数据库都是非关系型数据库
NoSQL只是一个概念，泛指非关系型数据库，和关系型数据库做区分。
```

### 1.3 Redis介绍

```
由于MySQL的性能不好，意大利人Salvatore开发出了Redis非关系型数据库
Redis(Remote Dictionary Server) 即远程字典服务, Redis由C语言编写，Redis是一款基于Key-Value的NoSQL,而且Redis是基于内存读取数据的；Redis提供了多种持久化机制，可以防止数据库崩溃后，数据不会丢失；Redis的性能可以达到110000/s的读取数据，以及81000/s写入数据;Redis还提供了主从，哨兵以及集群的搭建方式，可以更方便的横向扩展以及垂直扩展。
```



## 二. Redis安装

### 1.Windows安装

```
下载安装包：https://github.com/redis/redis/releases
https://github.com/tporadowski/redis/releases
```



### 2.Linux安装

```
1.切换为root
2.更新源: apt-get update 
3.安装redis: apt-get install redis-server
4.测试是否能使用：
	redis-cli
	127.0.0.1:6379>
	ping一下
	127.0.0.1:6379>ping
	PONG
5.设置登录密码
	vi /etc/redis/redis.conf
	允许远程连接，将bind 127.0.0.1 ::1注释掉
	找到#requirepass foobared
	将foobared改成自己的密码
```

