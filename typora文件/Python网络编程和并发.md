

# Python网络编程和并发

## 1.OSI模型

```
OSI网络体系结构分为7层
    ① 物理层       网卡
    ② 数据链路层   交换机   单位为帧
    ③ 网络层       路由
    ④ 传输层       送信
    ⑤ 会话层       定制通话的方式和规则
    ⑥ 表示层       规定数据交换的格式
    ⑦ 应用层       用户的应用程序和网络之间的接口
```

## 2.TCP/IP模型

```
TCP:传输层的协议
IP:网络层的协议
```

## 3.协议

```
    协议也叫网络协议，是通信计算机双方必须遵循的一组约定
    三要素：语法，语义，时序
    常用的协议：网络层协议IP，传输层协议TCP和UDP,应用层协议HTTP
    IP:IPV4  IPV6
    IP地址:网络地址和主机地址组成
    IP地址的分类：
        ① A类地址：1个字节的网络地址 3个字节的主机地址
        ③ B类地址：2个字节的网络地址 2个字节的主机地址
        ③ C类地址：3个字节的网络地址 1个字节的主机地址
            用于局域网 例如：192.168.1.234  192.168.1：网路地址  234：主机地址
        ④ D类地址：第一个字节以'1110'开始，是一个专门保留的地址  用于广播
        ⑤ E类地址：以'1111'开始，为将来使用保留  供实验和开发使用
        ⑥ 私有IP
            范围：
                10.0.0.0 ~ 10.255.255.255
                172.16.0.0 ~ 172.31.255.255
                192.168.0.0 ~ 192.168.255.255
        IP地址在127.0.0.1 ~ 127.255.255.255 用于回路测试

    子网掩码：规定了IP地址中的主机地址在0~255之间变化
        例如：
            255.255.255.0
            255.255.255 为网络地址
            0为主机地址   范围是0~255
```

## 4.TCP/UDP协议

```
    TCP:传输控制协议
        特点：面向连接，提供可靠的字节流服务
    UDP：用户数据报协议
        特点：面向数据报的传输层协议 提供非面向连接 不可靠的数据流传输 UDP不提供可靠性 也不提供报文到达确认
    这两种协议是传输层最重要的两种协议，为上层用户提供级别的通信可靠性
    TCP和UDP的最大区别是TCP是面向连接的，UDP是无连接的

    面向连接的TCP：TCP协议是一种可靠的，一对一的，面向有连接的通信协议
    '面向连接'：在正式通信前必须要与对方建立起连接
    通道的建立 ----- > 三次握手
        ① 在建立通道时，客户端首先要向服务端发送一个SYN同步信号
        ② 服务端接收到这个信号后会向客户端发出SYN同步信号和ACK确认信号
        ③ 当服务端的ACK和SYN到达客户端后，客户端与服务端之间的这个'通道'就被建立起来

    通道的关闭 ----> 四次挥手
        ① 在数据传输完毕后，客户端会向服务端发出一个FIN终止信号
        ② 服务端收到这个信号后会向客户端发送一个ACK确认信号
        ③ 如果服务端此后也没有数据发给客户端时服务端会向客户端发送一个FIN终止信号
        ④ 客户端收到这个信号之后，会回复一个确认信号，服务端接收到这个信号后，服务端与客户端之间的通道关闭

    无连接的UDP协议：UDP协议是一种不可靠的，面向无连接，可以实现多对一，一对多和一对一连接的通信协议
```

## 5.HTTP协议

```
    HTTP协议是一个应用层的协议，是一个简单的请求-响应协议  基于TCP
    请求和响应消息的头以ASCII码形式给出
    消息内容具有一个类似MIME的格式
    HTTP协议是基于客户/服务器模式，面向连接
    HTTP事务处理过程：
        ① 客户与服务器建立连接
        ② 客户向服务器发送请求
        ③ 服务器接手请求，并根据请求返回相应的文件作为应答
        ④ 客户与服务器关闭连接
    客户与服务器之间的连接是一次性连接，限制每次只处理一个请求
    HTTP是一种无状态协议
    客户在一个特定的TCP端口(端口一般为80)上打开一个套接字，如果服务器一直在这个周知的端口上，倾听连接
```

## 6.端口

```
    端口：设备与外界交流的出口
    端口就像是一个房子的门，是出入这间房子的必经之路
    在Linux系统中，端口可以有65536(2的16次方)之多
    端口只有整数，范围从0~65535
    知名端口从0~1024
        80端口分配给HTTP服务
        21端口分配给FTP服务
        22端口分配给SSH协议
    动态端口从1024~65535
    win系统查看端口状态：
        netstat -an
```

## 7.BS/CS结构

```
CS结构是Client/Server的缩写
BS结构是Browser/Server的缩写
```

## 8.Socket

```
Socket也叫套接字
Socket在应用层和传输层之间
Socket是一组接口，用来网络编程
```

## 9.Python Socket编程

### 9.1 创建Socket

```python
import socket

# 创建套接字  TCP协议
"""
参数：
    第一个参数：
      address family:  AF_INET(常用) 用于Internet之间的通信  AF_UNIX 用于同一台机器之间的进程通信
    第二个参数：
        Type:套接字类型 
            SOCK_STREAM  流式套接字，用于TCP协议
            SOCK_DGRAM   数据报套接字 用于UDP协议
"""
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s1)
# UDP协议
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

### 9.2 Socket发送数据

```
分别创建socket的客户端和服务端
            客户端：
                ① 创建客户端的socket
                ② 确定目标服务器的ip地址和端口号
                ③ 对要发送的消息进行编码，编码为bytes形式
                ④ 发送消息
                ⑤ 关闭套接字,节省系统资源
            服务端：
                ① 创建服务端的socket
                ② 创建服务端的ip和端口 如果一个计算机有多个网卡，就有很多个ip，使用空字符串代替ip
                ③ 绑定Ip和端口
                ④ 接收客户端发送的信息,信息需要解码
                ⑤ 关闭套接字,节省系统资源
```

UDP客户端

```python
from socket import *

# 创建一个UDP协议的套接字 发送数据到网络上的另外一个进程
client_sock = socket(AF_INET, SOCK_DGRAM)

# 定义一个接收消息的目标  127.0.0.1 为服务器的ip地址  8080为端口号
server_host_port = ('127.0.0.1', 8080)

# 准备发送的数据  需要将输入的内容进行编码 编码为字节bytes
data = input("请输入：").encode('utf-8')

# 发送数据  在网络中使用ip+端口+协议标识一个进程
client_sock.sendto(data, server_host_port)

print("发送完成")

# 关闭套接字,释放资源
client_sock.close()
```

UDP服务端

```python
from socket import *

# 创建一个服务端的socket
socet_server = socket(AF_INET, SOCK_DGRAM)

# 创建服务端的IP地址和端口号
host_post = ("127.0.0.1", 8080)

# Socket绑定这个IP地址和端口号 只有绑定了端口号和地址 才能成为服务端的Socket
socet_server.bind(host_post)

# 接收客户端发送过来的数据  接收1KB的数据  1KB=1024
# 收到的数据是一个元组，第一个值是收到的内容 第二个值是IP地址 第三个值是端口号
data = socet_server.recvfrom(1024)
print(data)
# 需要对接收到的数据进行解码
data_ = data[0].decode("utf-8")
print(data_)

# 关闭套接字  释放资源
socet_server.close()
```

### 9.3 echo服务

```
对socket发送消息进行一个改进
            分别创建socket的客户端和服务端
            客户端和服务端需要使用while循环，服务端为死循环
            客户端：
                ① 创建客户端的socket
                ② 确定目标服务器的ip地址和端口号
                ③ 对要发送的消息进行编码，编码为bytes形式
                ④ 发送消息
                ⑤ 接收服务器返回的信息，信息需要解码
                ⑥ 是否退出客户端
                ⑦ 关闭套接字,节省系统资源
            服务端：
                ① 创建服务端的socket
                ② 创建服务端的ip和端口 如果一个计算机有多个网卡，就有很多个ip，使用空字符串代替ip
                ③ 绑定Ip和端口
                ④ 接收客户端发送的信息,信息需要解码
                ⑤ 将客户端发送的信息返回给客户端
                ⑥ 关闭套接字,节省系统资源
```

客户端

```python
from socket import *

"""
客户端可以发送多条信息
客户端如果发送一个exit则退出
服务端如果获取到了什么就响应什么
"""

# 定义一个标志位，用来判断
flag = True

while flag:

    # 创建一个UDP协议的套接字 发送数据到网络上的另外一个进程
    client_sock = socket(AF_INET, SOCK_DGRAM)

    # 定义一个接收消息的目标  127.0.0.1 为服务器的ip地址  8080为端口号
    server_host_port = ('127.0.0.1', 8080)

    # 准备发送的数据  需要将输入的内容进行编码 编码为字节bytes
    data = input("请输入：").encode('utf-8')

    # 发送数据  在网络中使用ip+端口+协议标识一个进程
    client_sock.sendto(data, server_host_port)

    # 接收服务器返回的数据  并进行解码
    data_ = client_sock.recvfrom(1024)[0].decode('utf-8')
    print("服务端返回的数据是:", data_)

    if flag == "eixt":
        flag = False
    
# 关闭套接字  释放系统资源
client_sock.close()
```

## 10.TFTP

```
TFTP：简单文件传输协议,是TCP/IP协议族中一个用来在客户端和服务端进行简单文件传输的协议
特点：
    ① 简单
    ② 占用资源小
    ③ 适合在局域网进行文件传递
    ④ 端口号为69 默认监听69端口
    ⑤ 基于UDP实现
如果发送的文件较大，服务器会多次发送，因为发送的次数过多，为了让客户端对接收到的数据进行排序，在服务端发送多个字节数据的同时，会发送2个字节的数据，用来存储序号，放在多个字节数据的前面，序号从1开始

因为需要从服务器上下载文件， 文件可能不存在，此时服务器就会发送一个错误的信息过来，为了区分发送的是文件内容还是错误的信息，又用了2个字节表示这个数据包的功能【即操作码】，在序号的前面
操作码             功能
    1                 读请求，即下载
    2                 写请求，即上传
    3                 表示数据包，即DATA
    4                 确认码，即ACK
    5                 错误
    
    
数据包的格式:
        读写请求[客户端---》服务器]：操作码(2个字节) + 文件名(n个字节) + 0(1个字节) + 模式(n个字节) + 0(1个字节)
        数据包【服务器--->客户端】：操作码(2个字节) + 块编号(2个字节) + 数据(512)
        ACK[客户端---》服务器]：操作码(2个字节) + 块编号(2个字节)
        ERROR【服务器--->客户端】:操作码(2个字节) + 差错码(2个字节) + 差错信息(n个字节) + 0(1个字节)
```

```
实现思路：客户端向服务器发送一个读写请求，服务器接收到这个请求之后，判断这个请求是下载请求，还是上传请求，如果是下载请求，就进行下载，在下载时需要创建一个新的socket进行处理这个下载请求，将下载的内容分割为一个个的数据包进行传送给客户端，每个数据包的大小为512，同时客户端需要接收服务器传送过来的内容，服务器如果接收的内容在服务器上找不到，则需要返回一个错误的信息，服务器需要判断客户端是否下载完成，如果没有下载完成，需要接收客户端发送过来的ACK确认码，同时客户端接收到了数据包之后，需要判断数据包的内容是否是错误信息，如果不是则进行保存。
```

## 11.TCP

```:
服务端的流程:
    ① socket创建一个套接字
    ② bind绑定ip和port
    ③ listen使用套接字变为被动链接
    ④ accept等待客户端的链接
    	accept返回两个值，一个是新的socket,一个客户端地址  阻塞函数
    ⑤ recv/send接收发送数据
    	recv一般用于TCP协议
客户端：
    ① 创建一个套接字
    ② 使用connect(ip, addres)链接服务器的ip和端口
    ③ 客户端发送数据 send
    ④ 客户端也可以接收数据 recv
```

server.py

```python
from socket import *

# 创建一个套接字 SOCK_STREAM用于TCP
server_socket = socket(AF_INET, SOCK_STREAM)

# 绑定IP和端口
server_socket.bind(('', 8080))

# 服务器的socket监听，listen让Socket处于被动  5代表客户端处理的线程
server_socket.listen(5)

# 等待客户端的链接请求 【TCP是面向链接的协议】  返回两个值，一个是新的socket,一个是客户端的ip地址
new_socket, client_addr = server_socket.accept()  # 阻塞函数

# 服务端接收客户端发送过来的请求
data = new_socket.recv(1024)
print('服务器接收的数据是:', data.decode('utf-8'))

# 服务端发送数据给客户端
# new_socket.send('thank you'.encode('utf-8'))
new_socket.send(data)

# 关闭socket
new_socket.close()  # 当前客户端的socket关闭
server_socket.close()  # 整个服务器的socket关闭
```

Client.py

```python
from socket import *

# 创建一个socket
client_socket = socket(AF_INET, SOCK_STREAM)

# 确定服务器的ip和端口
server_host_port = ('127.0.0.1', 8080)

# 客户端建立一个链接（不是用来进行数据传输）
client_socket.connect(server_host_port)

# 客户端发送数据
data = input("请输入:")
client_socket.send(data.encode('utf-8'))

# 客户端接收服务器返回数据
rec_data = client_socket.recv(1024)
print('客户端接收到的数据是:', rec_data.decode('utf-8'))

client_socket.close()
```

### 模拟QQ聊天

server.py

```python
from socket import *

# 创建socket
server_socket = socket(AF_INET, SOCK_STREAM)

# 绑定ip
server_socket.bind(('', 8080))
# 让服务端处于被动
server_socket.listen(5)

while True:
    # 接收客户端发送的链接
    new_socket, client_host_port = server_socket.accept()
    print(client_host_port[0], client_host_port[1])

    while True:
        # 服务器接收数据
        data = new_socket.recv(1024)
        # print('客户端:', data.decode('utf-8'))

        if len(data) > 0:
            print(f'客户端{client_host_port[0]}:{client_host_port[1]}:', data.decode('utf-8'))
        if data.decode('utf-8') == 'exit':
            print(f'客户端{client_host_port[0]}:{client_host_port[1]}已经退出')
            break
        # 服务器发送数据
        send_data = input("send:")
        if len(send_data) > 0:
            new_socket.send(send_data.encode('utf-8'))
    new_socket.close()

server_socket.close()
```

client.py

```python
from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))

while True:
    data_ = input("send:")
    # 客户端发送数据
    if len(data_) > 0:
        client_socket.send(data_.encode('utf-8'))
    if data_ == 'exit':
        client_socket.close()
        break

    # 客户端接收数据
    data = client_socket.recv(1024)
    print(f'服务端127.0.0.1:{8888}:', data.decode('utf-8'))

client_socket.close()
```

## 12.黏包

```
黏包：黏包指的是数据与数据之间没有明确的分界线，导致不能正确读取数据
TCP可靠，但是会黏包
TCP在三种情况下会出现黏包:
    ① 当单个数据包较小时接收方可能一次性读取了多个数据包的数据
    ② 当单个数据包较大时接收方可能一次性仅读取了多个包的一部分数据
    ③ 另外TCP协议为了提高效率，增加了一种优化机制，会将数据较小且发送间隔较短的数据合并发送，该机制也会导致发送方将两个数据包黏在一起发送
```

### 客户端黏包问题

​	数据较小且发送间隔较短的数据合并发送

server.py

```python
from socket import *

# 创建socket
server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(('', 8088))

server_socket.listen(5)

new_socket, client_address = server_socket.accept()
data = new_socket.recv(1024)
data1 = new_socket.recv(1024)
print('第一条数据：',data)
print('第二条数据：',data1)
```

client.py

```python
from socket import *

client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8088))
client_socket.send('hello'.encode('utf-8'))
client_socket.send('word'.encode('utf-8'))
client_socket.close()
```

### 服务端黏包问题

```
当单个数据包较小时接收方可能一次性读取了多个数据包的数据
当单个数据包较大时接收方可能一次性仅读取了多个包的一部分数据
```

server.py

```python
from socket import *

server_scoket = socket(AF_INET, SOCK_STREAM)
server_scoket.bind(('', 8080))
server_scoket.listen(5)
new_socket, client_address = server_scoket.accept()
print(f'{client_address[0]}:{client_address[1]}连接成功')
data = new_socket.recv(3)
print('data:', data)
data1 = new_socket.recv(10)  # 将第一个数据中没有接收完的数据继续进行接收
print('data1:', data1)
new_socket.close()
server_scoket.close()
```

client.py

```python
import time
from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))
client_socket.send('hello'.encode('utf-8'))
time.sleep(5)
client_socket.send('hhaha'.encode('utf-8'))
client_socket.close()
```

黏包问题的解决

```
较为合理的解决方式：
    为字节流加上一个报头，告诉发送的字节流总大小，然后接收端来一个死循环接收完所有数据，用struct将序列化的数据长度打包成4个字节，4个字节够用
```

### 案例：传输文件案例，基于TCP协议，解决黏包问题

server.py

```python
import struct
from socket import *

# 创建socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', 8080))
server_socket.listen(5)
new_socket, client_address = server_socket.accept()

# 创建一个空白文件，用来接收数据
f = open('服务端.mp3', 'wb')

# 接收客户端发送过来的数据
# 接收报头
header_data = new_socket.recv(4)
size = struct.unpack('!i', header_data)[0]

size_ = 0  # 用来标记接收的数据的大小
# 如果接收的数据大小小于实际大小，则进行循环接收
while size_ < size:
    # 接收1024的数据大小
    data = new_socket.recv(1024)
    # 标记需要加上接收到的数据长度
    size_ += len(data)
    f.write(data)

print('服务端接收完成')
f.close()
new_socket.close()
server_socket.close()
```

client.py

```python
import struct
import os
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

# 给定文件的路径
file_path = '1.mp3'
# 以只读的方式打开这个文件
f = open('1.mp3', 'rb')

# 获取这个文件的大小
size = os.path.getsize(file_path)
# 准备一个报头 i占四个字节
header = struct.pack('!i', size)
# 发送这个报头
client.send(header)

# 发送文件内容
while True:
    data = f.read(1024)
    # 如果文件内容发送完毕，结束循环
    if not data:
        break
    client.send(data)

print('客户端发送完成')
f.close()
client.close()
```

## 13. Python多线程和多进程

```
进程：正在执行的程序可以看作是进程
线程：线程是进程的执行单元
进程与线程的对比：
    进程是重量级的。具体包括进程映像结构的结构，执行细节以及进程间切换的方法，在进程中，需要处理的问题包括进程间通信，临界区管理和进程调度等，这些特性使得进程开销比较大
	线程是轻量级的。线程之间有许多共享的资源，容易通信，生成一个线程的开销较小但是线程会有死锁，数据同步和实现复杂等问题

并发编程解决方案：
    ① 启动多个进程，每个进程虽然只有一个线程，但多个进程可以一起执行多个任务
    ② 启动一个进程，在一个进程中启动多个线程，多个线程也可以一起执行多个任务
    ③ 启动多个进程，每个进程启动多个线程，这样同时执行的任务就更多，这种模型复杂，实际很少采用
由于Python使用全局解释锁(GIL)和队列模块，其在线程实现的复杂度上相对于其他语言来说要低很多，由于GIL的存在,所以Python解释器不是线程安全的，因为当前线程必须持有这个全局解释锁，才可以安全访问Python对象,虽然使用GIL使得Python不能很好的利用多GPU优势，但是现在还没有很好的办法来代替它，因为去掉GIL会带来很多麻烦

针对I/O受限:
    如网络下载类，可以使用多线程
对于GPU受限:
    如科学计算类，使用多线程不会提高效率，建议使用进程和进程与线程混合的方法实现
```

### 相关模块

```
os/sys  包含基本进程管理函数
subprocess python基本库中多进程编程相关模块，适用于与外部进程进程交互，调用外部进程
multiprocessing python基本库中进程编程模块，核心机制是fork,重开一个进程，首先会把父进程的代码copy重载一遍
threading python基本库中多线程管理相关模块
```

## 多进程

### subprocess.run()方法

```
    subprocess 模块首先推荐使用的是它的 run 方法，更高级的用法可以直接使用 Popen 接口
    run()方法语法格式如下：
        subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None,
        capture_output=False, shell=False, cwd=None, timeout=None, check=False,
        encoding=None, errors=None, text=None, env=None, universal_newlines=None)
        
            参数列表：
            args：表示要执行的命令。必须是一个字符串，字符串参数列表。
            stdin、stdout 和 stderr：子进程的标准输入、输出和错误。其值可以是 subprocess.PIPE、subprocess.DEVNULL、一个已经存在的文件描述符、已经打开的文件对象或者None
            subprocess.PIPE 表示为子进程创建新的管道 父进程和子进程之间通信
            subprocess.DEVNULL 表示使用 os.devnull。默认使用的是 None，表示什么都不做。将数据丢失
            另外，stderr 可以合并到 stdout 里一起输出。stderr=subprocess.STDOUT
            timeout：设置命令超时时间。如果命令执行时间超时，子进程将被杀死，并弹出 TimeoutExpired 异常。
            check：如果该参数设置为 True，并且进程退出状态码不是 0，则弹 出 CalledProcessError 异常。
            encoding: 如果指定了该参数，则 stdin、stdout 和 stderr 可以接收字符串数据，并以该编码方式编码。否则只接收 bytes 类型的数据。
            shell：如果该参数为 True，将通过操作系统的 shell 执行指定的命令。
```

### subprocess调用系统命令

简单的写法

```python
import subprocess
# 开启一个子进程，用来执行系统命令 args,encoding,shell三个参数
run_cmd = subprocess.run('dir E:\\virenv\\python全栈\\Python网络编程和并发', encoding='utf-8', shell=True)
print(run_cmd)
```

定义一个方法，调用系统中的所有命令

```python
import subprocess
def runCmd(command):
    # 定义一个子进程，用来执行系统所有命令
    runMd = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='GBK', shell=True)
    # 判断执行是否正常  returncode为0代表正常
    if runMd.returncode == 0:
        print('success:')
        print(runMd.stdout)
    else:
        print('命令执行错误:')
        print(runMd.stderr)

runCmd('dir E:\\virenv\\python全栈\\Python网络编程和并发')
runCmd('exit 1')
```

###  使用文件句柄的方式传参数

```python
import subprocess

# 通过文件句柄的方式传参
f = open('1.txt')
# PIPE不能传给系统命令 subprocess有一个接口Popen可以传参给系统命令
run_cmd = subprocess.run('python', stdin=f, stdout=subprocess.PIPE, shell=True)
print(run_cmd.stdout)
f.close()
```

### 使用Popen接口传给系统命令

Popen 是 subprocess的核心，子进程的创建和管理都靠它处理

```python
class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, 
preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False, 
startupinfo=None, creationflags=0,restore_signals=True, start_new_session=False, pass_fds=(),
*, encoding=None, errors=None)
```

常用参数：

args：shell命令，可以是字符串或者序列类型（如：list，元组）

bufsize：缓冲区大小。当创建标准流的管道对象时使用，默认-1。
	0：不使用缓冲区
	1：表示行缓冲，仅当universal_newlines=True时可用，也就是文本模式
	正数：表示缓冲区大小
	负数：表示使用系统默认的缓冲区大小。
stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄
preexec_fn：只在 Unix 平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
shell：如果该参数为 True，将通过操作系统的 shell 执行指定的命令。
cwd：用于设置子进程的当前目录。
env：用于指定子进程的环境变量。如果 env = None，子进程的环境变量将从父进程中继承。

```python
import subprocess

# 使用popen传参数
popen = subprocess.Popen('python', stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
popen.stdin.write('print("hello word")\n'.encode('utf-8'))  # 转为字节数据
popen.stdin.write('import os'.encode('utf-8'))
popen.stdin.close()

out = popen.stdout.read().decode('gbk')
popen.stdout.close()
print(out)
```

### multiprocessing模块

进程ID: os.getpid()

父进程ID：os.getppid()

```python
import time
import os
from multiprocessing import Process

def test(name):
    print('当前进程的id', os.getpid())
    print('当前父进程的id', os.getppid())
    print('当前进程的名字', name)

    time.sleep(3)

if __name__ == '__main__':
    for i in range(10):
        process_ = Process(target=test, args=(f'进程id是{i}',))
        process_.start()

    print('父进程执行完毕')
    # 父进程中没有任何阻塞的代码，父进程必须等待所有子进程执行完毕后才结束
```

使用自定义的方式创建进程

```python
import os
import time
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print('当前进程的id', os.getpid())
        print('当前父进程的id', os.getppid())
        print('当前进程的名字', self.name)
        time.sleep(3)


if __name__ == '__main__':
    start = time.time()
    process_list = []
    for i in range(10):
        process_ = MyProcess(f'进程名是：{i + 1}')
        process_.start()
        process_list.append(process_)

    for ii in process_list:
        # 阻塞 父进程等待所有的子进程结束，才会执行后面的代码
        ii.join()

    #所有子进程结束才会执行
    end_time = time.time() - start
    print(end_time)
```

### 进程间的通信

进程和进程之间无法共享全局变量

Python提供了多种实现进程间通信的机制，主要有以下2种：
    ① Python multiprocessing模块下的Queue类，提供了多个进程之间实现通信的诸多方法
    ② Pipe ，又称为管道，常用于实现2个进程间的通信，这2个进程分别位于管道的两端

#### Queue实现进程之间的通信

简单的理解，Queue实现进程间的通信，使用了操作系统给开辟的一个队列空间，各个进程可以把数据放到该
队列中，当然也可以从队列中将自己需要的数据取走

```python
import os
from multiprocessing import Process, Queue


# 创建两个进程，一个用于写，一个用来读
class WriterProcess(Process):
    def __init__(self, name, q):
        Process.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        print(f'进程{self.name},ID{os.getpid()}已经启动')
        for i in range(1, 6):
            self.q.put(i)
        print(f'进程{self.name},ID{os.getpid()}已经结束')


class ReaderProcess(Process):
    def __init__(self, name, q):
        Process.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        print(f'进程{self.name},ID{os.getpid()}已经启动')
        while True:
            # 读数据
            value = self.q.get(True)  # get()会阻塞
            print(value)
        # 队列中没有数据，会一直处于阻塞状态，后面的代码不会执行
        print(f'进程{self.name},ID{os.getpid()}已经结束')


if __name__ == '__main__':
    # 创建一个队列
    q = Queue()

    # 创建写进程
    pw = WriterProcess('writer', q)
    # 创建读进程
    pr = ReaderProcess('read', q)
    pw.start()
    pr.start()
    pw.join()
    # 杀死进程pr
    pr.terminate()
    print('父进程结束')
```

#### Pipe实现进程间的通信

Pipe有两个口，Pipe用来实现2个进程之间的通信，这个2个进程分别位于管道的两端，一端用来发数据，一端用来接收数据

1.send(obj)

​	发送一个obj给管道的另一端，另一端使用recv()方法接收,，该obj必须是可序列化的，如果可序列化的数据超过32MB，可能会引发ValueError异常

2.recv()

​	接收另一端通过send()方法发送过来的数据

3.close()

​	关闭连接

4.poll(timeout)

​	返回连接中是否还有数据可以读取

### 进程池

​	Python提供了更好的管理多个进程的方式，使用进程池。进程池可以提供指定数量的进程给用户使用。即当有了新的请求提交到进程池中，如果未满，则会创建一个新的进程用来执行该请求；反之，如果进程池中的进程数已经达到最大，那么该请求就会等待，只有进程池空闲下来，该请求才会执行。

使用进程池的优点:

​	1.提高效率，节省开辟进程和开辟内存空间的时间以及销毁进程的时间

​	2.节省内存空间

 Pool()中的函数说明

​	Pool() 创建多个进程，表示可以同时执行的进程数量，默认大小是CPU的核心数量

 	join() 会等待进程池中所有的子进程结束后再去执行父进程

​	close() 如果使用的进程池 在调用join()之前必须先close，在close之后不能继续向进程池中添加新的进程

​	pool.apply_async(func,args,kwargs) 异步执行 将事件放入进程池队列。args以元组方式传参，kwargs以字典格式
​	pool.apply_sync(func, args, kwargs) 同步执行 将事件放入进程池队列

```python
import os
import time
import random
from multiprocessing import Process
from multiprocessing.pool import Pool


def run(name):
    start = time.time()
    print(f'进程{name}已经启动，ID{os.getpid()}')
    time.sleep(random.choice([1, 2, 3, 4, 5]))
    end_time = time.time() - start
    print(f'进程{name}已经结束，ID{os.getpid()},耗时{end_time}')


if __name__ == '__main__':
    # 创建一个进程池
    p = Pool(5)
    for i in range(10):
        p.apply_async(run, (f'process{i}',))
    p.close()
    p.join()
    print('主进程结束')
```

## 多线程

线程：
    ① 内核线程：由操作系统内核创建和撤销
    ② 用户线程：不需要内核支持而在用户程序中实现的线程

线程的状态：
    ① 新建
    ② 就绪状态  由CPU调度进入运行状态
    ③ 运行状态  等待的条件 等待/阻塞    满足条件就进入就绪状态  运行结束进入终止状态
    ④ 终止

Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。

_thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。

threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：

- threading.currentThread(): 返回当前的线程变量。
- threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
- threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:

- run(): 用以表示线程活动的方法。
- start():启动线程活动。
- join([time]):等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
- isAlive(): 返回线程是否活动的。
- getName: 返回线程名。
- setName:设置线程名。
- isDaemon:查看线程是否是后台运行标志
- setDaemon:设置线程的后台运行标志

### 多线程的创建

#### 函数的封装方式

```python
import threading
import time, os


def run(name):
    for i in range(3):
        print(f'线程名字{name},输出:{i}')
        time.sleep(1)


if __name__ == '__main__':
    print(f'主线程开始时间{time.time()}')
    s = 'abcdef'
    for i in range(5):
        thread_t = threading.Thread(target=run, args=(s[i]))
        thread_t.start()
    print('主线程结束')
```

#### 类的创建

```python
import threading
import time, os

class MyThreading(threading.Thread):
    def run(self):
        for i in range(3):
            print(f'线程名字{self.name},输出:{i}')
            time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    print(f'主线程开始时间{start}')
    s = 'abcdef'
    thread_list = []
    for i in range(5):
        thread_t = MyThreading(name=s[i])
        thread_t.start()
        thread_list.append(thread_t)

    for j in thread_list:
        j.join()
    end=time.time()
    print(f'主线程结束，时间为{(end-start):.2f}')
```

### 获取线程数量 

len(threading.enumerate())

threading.activeCount()

```python
import threading
import time, os

class MyThreading(threading.Thread):
    def run(self):
        for i in range(3):
            print(f'线程名字{self.name},输出:{i}')
            time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    print(f'主线程开始时间{start}')
    s = 'abcdef'
    for i in range(5):
        thread_t = MyThreading(name=s[i])
        thread_t.start()

    while True:
        count = len(threading.enumerate())
        print(f'当前线程的数量是：{count}')

        if count <= 1:
            break
    print('主线程结束')
```

### 守护线程

主线程结束，子线程也结束

thread_t.setDaemon(True)

thread_t.daemon = True

```python
import threading
import time, os

class MyThreading(threading.Thread):
    def run(self):
        for i in range(3):
            print(f'线程名字{self.name},输出:{i}')
            time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    print(f'主线程开始时间{start}')
    thread_t = MyThreading(name='my_thread_1')
    thread_t.setDaemon(True)
    # thread_t.daemon = True 设置守护线程  主线程结束，子线程也结束
    thread_t.start()
    time.sleep(1)
    print('主线程结束')
```

### 同步

同步的简单方式是使用锁机制。提供了两种操作：加锁和解锁

同一进程中的所有线程都是共享数据的，如果对线程中共享数据的并发访问不加以限制，结果不可预期，在严重的情况下，还会产生死锁

#### 线程之间共享数据

```python
import time
from threading import Thread

num = 0


def run1():
    global num
    for _ in range(10):
        num += 1
    print(f'线程一的num值是{num}')


def run2():
    global num
    print(f'线程二的num值是{num}')


if __name__ == '__main__':
    t1 = Thread(target=run1)
    t2 = Thread(target=run2)
    t1.start()
    time.sleep(1)
    t2.start()
    print('主线程结束')
```

```python
import time
from threading import Thread


def run1(num):
    for _ in range(10):
        num[0] += 1
    print(f'线程一的num值是{num[0]}')


def run2(num):
    print(f'线程二的num值是{num[0]}')


if __name__ == '__main__':
    i = [0]  # 为了让多个线程可以共享数据，需要使用可变类型
    t1 = Thread(target=run1, args=(i,))
    t2 = Thread(target=run2, args=(i,))
    t1.start()
    time.sleep(1)
    t2.start()
    print(f'全局变量i的值是{i}')
    print('主线程结束')
```

#### 线程独立的私有变量

threading.local()

```python
import time, random
from threading import *


def run():
    #  定义一个私有变量
    local_var = local()
    local_var.numbers = [1]  # 给定初始值为1
    # 给定休眠时间，模拟不同线程的执行
    time.sleep(random.random())
    for i in range(8):
        local_var.numbers.append(random.choice(range(10)))
    # 打印当前线程的私有变量值
    print(current_thread(), local_var.numbers)


if __name__ == '__main__':
    thread_list = []

    for i in range(5):
        t1 = Thread(target=run)
        t1.start()
        thread_list.append(t1)

    for j in thread_list:
        j.join()
```

#### 线程共享数据的混乱问题

```python
from threading import *

num = 0


def run():
    global num
    print(f'线程{current_thread().name}开始执行')
    for i in range(500000):
        num += 1
    print(f'线程{current_thread().name}执行完毕，num的值是{num}')


if __name__ == '__main__':
    threads = []
    for i in range(5):
        t1 = Thread(target=run)
        t1.start()
        threads.append(t1)

    for i in threads:
        i.join()

    print(f'主线程结束,全局变量num的值是{num}')
```

#### 解决线程共享数据的混乱问题

lock = Lock()  锁机制

lock.acquire() # 加锁

lock.release() # 解锁

```python
from threading import *

num = 0


def run():
    lock.acquire()  # 加锁
    print(f'线程{current_thread().name}开始执行')
    global num
    for i in range(500000):
        num += 1
    print(f'线程{current_thread().name}执行完毕，num的值是{num}')
    lock.release()  # 解锁


if __name__ == '__main__':
    # 创建锁
    lock = Lock()
    threads = []
    for i in range(5):
        t1 = Thread(target=run)
        t1.start()
        threads.append(t1)

    for i in threads:
        i.join()

    print(f'主线程结束,全局变量num的值是{num}')
```

#### with解决线程共享数据的混乱问题

with会自动加锁和释放锁

```python
from threading import *

num = 0


def run():
    # with会自动加锁和释放锁
    with lock:
        print(f'线程{current_thread().name}开始执行')
        global num
        for i in range(500000):
            num += 1
        print(f'线程{current_thread().name}执行完毕，num的值是{num}')


if __name__ == '__main__':
    # 创建锁
    lock = Lock()
    threads = []
    for i in range(5):
        t1 = Thread(target=run)
        t1.start()
        threads.append(t1)

    for i in threads:
        i.join()

    print(f'主线程结束,全局变量num的值是{num}')
```

### 死锁

在多线程程序中，死锁问题很大一部分是由于线程同时获取多个锁造成的

在线程间共享多个资源时，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁

#### 第一种死锁

一个线程同时获得多把锁

```python
import time
from threading import *

lock1 = Lock()
lock2 = Lock()


class MyThread1(Thread):
    def run(self):
        lock1.acquire()
        print('线程1获得了lock1')
        time.sleep(1)
        lock2.acquire()
        print('线程1获得了lock2')
        lock1.release()
        lock2.release()


class MyThread2(Thread):
    def run(self):
        lock2.acquire()
        print('线程2获得了lock2')
        time.sleep(1)
        lock1.acquire()
        print('线程2获得了lock1')
        lock2.release()
        lock1.release()


if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
```

#### 第二种死锁  

锁被自己本身拿到，没有释放，使用逻辑锁

Lock()  互斥锁

RLock() 逻辑锁  只针对一个线程

```python
import time
from threading import *

lock3 = RLock() 
class MyThread3(Thread):
    def run(self):
        lock3.acquire()
        print('线程3获得lock3')
        time.sleep(1)
        self.run()
        lock3.release()
if __name__ == '__main__':
        t3 = MyThread3()
    	t3.start()
```

### 死锁的解决办法

使用while循环交叉执行，解决死锁的问题

```python
import time
from threading import *

# 使用while循环交叉执行，解决死锁的问题

lock1 = Lock()
lock2 = Lock()


class MyThread1(Thread):
    def run(self):
        while True:
            lock1.acquire()
            print('线程1获得了鱼')
            time.sleep(1)
            lock1.release()

            lock2.acquire()
            print('线程1获得了熊掌')
            time.sleep(1)
            lock2.release()


class MyThread2(Thread):
    def run(self):
        while True:
            lock2.acquire()
            print('线程2获得了熊掌')
            time.sleep(1)
            lock2.release()

            lock1.acquire()
            print('线程2获得了鱼')
            time.sleep(1)
            lock1.release()


if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
```

### 线程间的通信

#### 信号量

信号量来设置在多线程中，并行运行的线程个数

```python
import threading
import time

# 创建一个信号量
Semap_hore = threading.BoundedSemaphore(3)  # 一次允许3个线程运行

def run(num):
    Semap_hore.acquire()
    print(f'第{num}个num')
    time.sleep(1)
    Semap_hore.release()

if __name__ == '__main__':
    for i in range(100):
        t = threading.Thread(target=run, args=(i, ))
        t.start()
```

#### Queue

Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。

这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。

Queue 模块中的常用方法:

- Queue.qsize() 返回队列的大小
- Queue.empty() 如果队列为空，返回True,反之False
- Queue.full() 如果队列满了，返回True,反之False
- Queue.full 与 maxsize 大小对应
- Queue.get([block[, timeout]])获取队列，timeout等待时间
- Queue.get_nowait() 相当Queue.get(False)
- Queue.put(item) 写入队列，timeout等待时间
- Queue.put_nowait(item) 相当Queue.put(item, False)
- Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
- Queue.join() 实际上意味着等到队列为空，再执行别的操作

```python
import threading
import time
import queue

# 创建一个队列
q = queue.Queue(maxsize=1000)  # 先进先出队列  设置队列中存放的数据为1000


# q = queue.LifoQueue() # 后进先出队列
# q = queue.PriorityQueue()  # 优先级队列

# 创建一个生产者线程
class Producter(threading.Thread):
    def run(self):
        global q
        count = 0
        while True:
            # q.size() 获取队列中的数据的总数
            if q.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = f'生产{count}'
                    # 将数据放入队列
                    q.put(msg)
                    print(msg)
            time.sleep(2)


class Customer(threading.Thread):
    def run(self):
       global q
       while True:
           for i in range(100):
               msg = q.get()
               print(f'消费{msg}')
           time.sleep(3)

if __name__ == '__main__':
    t1 = Producter()
    t2 = Customer()
    t1.start()
    t2.start()
```

### 生产者和消费者模式

### Enevt事件

线程的一个关键特性是每个线程都是独立运行且状态不可预测。如果程序中的其 他线程需要通过判断某个线程的状态来确定自己下一步的操作,这时线程同步问题就会变得非常棘手。为了解决这些问题,我们需要使用threading库中的Event对象。 对象包含一个可由线程设置的信号标志,它允许线程等待某些事件的发生。在 初始情况下,Event对象中的信号标志被设置为假。如果有线程等待一个Event对象, 而这个Event对象的标志为假,那么这个线程将会被一直阻塞直至该标志为真。一个线程如果将一个Event对象的信号标志设置为真,它将唤醒所有等待这个Event对象的线程。如果一个线程等待一个已经被设置为真的Event对象,那么它将忽略这个事件, 继续执行。

Event其实就是一个简化版的 Condition。Event没有锁，无法使线程进入同步阻塞状态。

is_set()
当且仅当内部标志为True时返回True。

set()
将内部标志设置为True。所有等待它成为True的线程都被唤醒。当标志保持在True的状态时，线程调用wait()是不会阻塞的。

clear()
将内部标志重置为False。随后，调用wait()的线程将阻塞，直到另一个线程调用set()将内部标志重新设置为True。

wait(timeout=None)
阻塞直到内部标志为真。如果内部标志在wait()方法调用时为True，则立即返回。否则，则阻塞，直到另一个线程调用set()将标志设置为True，或发生超时。
该方法总是返回True，除非设置了timeout并发生超时。

```python
import threading
import time
import random

"""
门的状态有三种：
    ① 门已经打开,可以进入  0,1,2 打开
    ② 门已经关闭，需要刷卡进入  
    ③ 门自动关闭  3 关闭

人的状态有两种：
    ① 门打开，人可以直接进入
    ② 门关闭，需要刷卡
"""
# 设置一个事件
enevt = threading.Event()  # 默认为false
enevt.set()  # 设置一个标志位 门一开始就是打开的
# 设置一个状态  状态为打开
status = 0


def door():
    global status
    while True:
        print(f'当前门的状态是{status}')
        if status >= 3:
            print("门已经自动关闭")
            enevt.clear()
        if enevt.is_set():
            print("门已经打开，可以进入")
        else:
            print("门已经关闭，需要刷卡进入")
            enevt.wait()
            continue
        time.sleep(1)
        status += 1

def people():
    global status
    count = 0
    while True:
        count += 1
        if enevt.is_set():
            print(f'门开着,{count}号进入里面')
        else:
            print(f"门被关闭，{count}号刷卡进入")
            enevt.set()
            status = 0
        time.sleep(random.randint(1, 10))

if __name__ == '__main__':
    d = threading.Thread(target=door)
    p = threading.Thread(target=people)
    d.start()
    p.start()
```

### 异步

```python
import time
import os
from multiprocessing import Pool

def test1():
    print(f'当前进程id是{os.getpid()},父进程id是{os.getppid()}')
    print('起床')
    time.sleep(3)
    return 'abc'


def test2():
    print(f'开始早读,当前进程id是{os.getpid()}')
    time.sleep(5)
    print('早读完成')


def test3(args):
    """
    test3是test1和test3执行完毕后才会执行
    :return:
    """
    print(f'吃早餐,当前进程idhi是{os.getpid()}')
    print(f'参数是{args}')

if __name__ == '__main__':
    po = Pool(4)
    # 异步
    po.apply_async(func=test1,callback=test3)
    test2()
```

### 协程

协程又称微线程，纤程。（协程是一种用户态的轻量级线层）

作用：在执行A函数的时候，可以随时中断，去执行B函数，然后中断继续执行A函数(可以自动切换)

协程只有一个线程在执行

协程的标准：

​	① 必须在只有一个单线程里实现并发

​    ② 修改共享数据不需要加锁

​	③ 用户程序里自己保存多个控制流的上下文栈

​	④ 一个协程遇到IO操作自动切换到其他协程

#### greenlet模块

```python 
from greenlet import greenlet


# 创建一个协程案列，一问一答
def ask(name):
    print(f'{name}: 买mac笔记本')
    g1.switch('o')
    print(f'{name}: 买macpro')
    g1.switch()


def answer(name):
    print(f'{name}: 买')
    g.switch()
    print(f'{name}: maimai')


if __name__ == '__main__':
    # 创建一个协程
    g = greenlet(ask)
    g1 = greenlet(answer)
    g.switch('k')  # 函数第一次调用时需要传递参数
```

#### gevent模块

```python 
import gevent


def ask(name):
    print(f'{name}: 买mac笔记本')
    gevent.sleep(2)  # 人为模拟IO阻塞
    print(f'{name}: 买macpro')


def answer(name):
    print(f'{name}: 买')
    gevent.sleep(2)  # 人为模拟IO阻塞
    print(f'{name}: maimai')


if __name__ == '__main__':
    # 创建一个协程
    g = gevent.spawn(ask, 'kkk')
    g1 = gevent.spawn(answer, '哈哈')
    gevent.joinall([g, g1])  # 自动切换并执行
```

#### asyncio模块

```python
import asyncio


async def fun1():
    for i in range(5):
        print("协程a执行")
        await asyncio.sleep(1)


async def fun2():
    for i in range(5):
        print("协程b执行")
        await asyncio.sleep(2)


# 创建协程事件循环
loop = asyncio.get_event_loop()

# 运行协程
loop.run_until_complete(asyncio.gather(fun1(), fun2()))
loop.close()
```

#### asyncio嵌套

```python
import asyncio


async def func(x, y):
    resutl = await fun(x, y)  # 让下一个协程进行计算
    print(f'{x}+{y}的值是：{resutl}')


async def fun(x, y):
    print(f'开始计算：{x} + {y}')
    await asyncio.sleep(1)
    return x + y


loop = asyncio.get_event_loop()
loop.run_until_complete(func(1, 2))
loop.close()
```

## 生成器

### (1) 创建生成器的方式：

​	① 通过列表推导式

​	② 通过yield关键字

生成器不会把内容保存到内存中，生成器是一个对象，里面保存了产生元素的算法，同时会记录游标的位置

```python
# 通过列表生成式创建一个生成器
g = (x for x in range(1, 10) if x % 2 == 0)

# 通过函数创建生成器 yield
def test():
    a, b = 0, 1
    while True:
        # yield用于创建生成器，返回后面的变量给生成器
        yield b  # b是斐波拉契数中的一个元素
        a, b = b, (a + b)
```

### (2) 遍历生成器

​	① 使用内置的函数next() 获取第一个值

​	② 使用for循环遍历

​	③ 使用object对象中的__next__方法遍历

​	④ 使用send()函数，生成器第一次调用时需要传递send(None) 后面没有限制

```python
g = test()
print(g.__next__())
print(g.send(None))
print(g.send(''))
print(g.send(''))
print(g.next())
```

## 迭代器

Iterable:可迭代对象 能够通过for循环来遍历里面的元素的对象
可以被next()函数调用并不断返回下一个值的对象称为迭代器[Iterator]
使用isinstance()方法判断一个对象是否是可迭代对象

```python
from collections.abc import Iterable

a = {}
b = (1,)
c = []

def tesdt1(args):
    if isinstance(args, Iterable):
        print('是可迭代对象')
    else:
        print('不是可迭代对象')

tesdt1(1)
```

使用isinstance()方法判断一个对象是否是迭代器

生成器是迭代器 

list,set,dict,tuple不是迭代器

```python
from collections.abc import Iterator
def tesdt2(args):
    if isinstance(args, Iterator):
        print('是可迭代对象')
    else:
        print('不是可迭代对象')
tesdt2((x for x in range(32)))
```

使用iter()将list,dict,str变为迭代器

## 高阶函数

函数式编程的一个优点：允许把函数本身作为一个参数传给另一个函数，还允许返回一个函数

```python
# 定义一个函数，计算阶乘
def test1(num):
    if num == 1:
        return 1
    else:
        return num * test1(num - 1)

# test2是高阶函数   参数是有一个是函数
def tests2(list1, func):
    new_list = []
    for i in list1:
        new_list.append(func(i))
    return new_list


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tests2(list1, test1))
```

### 匿名函数

```python
func = lambda x, y: x + y
print(func(2,3))
```

### 内置的高阶函数

内置的高阶函数：
    map()函数：把可迭代对对象中的每一个元素转成一个的对象，并返回一个迭代器
    reduce函数：把可迭代对象中的每一个元素做聚合处理，返回一个聚合的值

​	filter函数:把一个可迭代对象中的元素做过滤操作，如果func为True则留下，否则则过滤掉,返回一个迭代器

​	max和min

​	sorted 把一个可迭代对象里面的每个元素进行排序，返回一个列表

```python
lis = [1, 2, 34, 5, 6, 7]
it1 = map(lambda x: x ** 2, lis)
# print(next(it1))
# print(next(it1))
# print(list(it1))

from functools import reduce

my_list = [1, 23, 4, 5, 6, 6, 7, 8]
print(reduce(lambda x, y: x + y, my_list))


def getMax(x, y):
    if x > y:
        return x
    else:
        return y


print(reduce(getMax, my_list))
```

```python
students = [
    {'name': 'k', 'age': 34},
    {'name': 'j', 'age': 23},
    {'name': 'jk', 'age': 18}
]
print(list(filter(lambda x: x['age'] > 18,students)))
```

```python
"""
内置的高阶函数：
    map()函数：把可迭代对对象中的每一个元素转成一个的对象，并返回一个迭代器
    reduce函数：把可迭代对象中的每一个元素做聚合处理，返回一个聚合的值
    filter函数:把一个可迭代对象中的元素做过滤操作，如果func为True则留下，否则则过滤掉,返回一个迭代器
    max和min
    sorted 把一个可迭代对象里面的每个元素进行排序，返回一个列表
"""
lis = [1, 2, 34, 5, 6, 7]
it1 = map(lambda x: x ** 2, lis)
# print(next(it1))
# print(next(it1))
# print(list(it1))

from functools import reduce

my_list = [1, 23, 4, 5, 6, 6, 7, 8]
print(reduce(lambda x, y: x + y, my_list))


def getMax(x, y):
    if x > y:
        return x
    else:
        return y


print(reduce(getMax, my_list))

students = [
    {'name': 'k', 'age': 34},
    {'name': 'j', 'age': 23},
    {'name': 'jk', 'age': 18},
    {'name': 'jh', 'age': 90}
]
print(list(filter(lambda x: x['age'] > 18, students)))
print(max(students, key=lambda x: x['age']))
print(min(students, key=lambda x: x['age']))
print(sorted(students, key=lambda x: x['age'], reverse=True))
```

### 高阶函数作为返回值

```python
def get_num(*args):
    def t():
        s = 0
        for i in args:
            s += i
        return s

    return t


f = get_num(1, 23, 4, 5, 6, 8, 90)
print(f())
```

定义一个函数，来打印出100以内的所有质数 0和1不是质数，2是最小的质数

```python
def get_num():
    """
    获取所有的奇数
    :return:
    """
    n = 1
    while True:
        n += 2
        yield n


f = get_num()


# 定义一个函数，用来过滤奇数中不是质数
def my_filter(n):
    return lambda x: x % n > 0


# 定义一个质数生成器
def t():
    yield 2
    # 拿到所有的奇数
    g = get_num()
    while True:
        # 从生成器中拿取奇数
        x = next(g)
        # 过滤掉不是质数的奇数
        g = filter(my_filter(x), g)
        yield x


for i in t():
    if i < 100:
        print(i)
    else:
        break
```

### 闭包

闭包：函数可以引用函数作用域外的变量，并且可以在函数定义之外被调用

闭包的三个条件：

​	① 必须有一个内部函数

​	② 内部函数必须定义在一个外部函数的闭合范围内，内部函数引用外部变量

​	③ 外部函数必须返回定义的内部函数

#### 闭包的定义

```python
def func_a(num_a):
    def func_b(num_b):
        print(f'内部函数func_b的参数是{num_b}, 外部函数func_a的参数是{num_a}')
        return num_a + num_b

    return func_b


f = func_a(100)
print(f(200))
```

#### 闭包的应用

```python
def create_line(a, b):
    def line(x):
        return a * x + b

    return line


l1 = create_line(2, 4)
l2 = create_line(9, -8)


print(l1(4))
print(l2(4))
```

#### 闭包引用外部变量

```python
def test1():
    c = 0  # c不是全局变量，是介于全局变量和局部变量之间的变量 需要使用nonlocal进行标识

    def add_test():
        nonlocal c
        print(c)
        c += 1
        # print(c)
        return c

    return add_test

t =test1()()
print(t)
```

#### 闭包的陷阱

```python
def tes():
    add_list = []
    for i in range(1, 4):
        def tes_(_i=i):
            return _i ** 2

        add_list.append(tes_)
    return add_list


f1, f2, f3 = tes()
print(f1(), f2(), f3())
```

### 装饰器

作用：为已经存在的函数添加额外的功能

```python
from functools import wraps


# 定义一个装饰器
def test1(func):
    @wraps(func)  # 使用@wraps包装func
    def test2():
        print('ok')
        func()
        print('pl')

    return test2


@test1
def test3():
    print('hahah')


test3()
print(test3.__name__)  # test3
```

```python
"""
装饰器的作用：给已经存在的函数添加额外的功能
"""
import time
from functools import wraps


def logger(func):
    @wraps(func)
    def writer_logging():
        print(f'[info] ------>时间是：{time.strftime("%H:%M:%S", time.localtime())}')
        func()

    return writer_logging


@logger
def work():
    print('正在工作')


work()
```

#### 带参的装饰器

```python
import time
from functools import wraps


def logger(func):
    @wraps(func)
    def writer_logging(*args, **kwargs):
        print(f'[info] ------>时间是：{time.strftime("%H:%M:%S", time.localtime())}')
        func(*args, **kwargs)

    return writer_logging


@logger
def work():
    print('正在工作')


@logger
def work1(name):
    print(f'{name}在工作')


work()
work1('jk')
```

```python
import time
from functools import wraps


def main_logger(logfile='work.log'):
    def logger(func):
        @wraps(func)
        def writer_logging(*args, **kwargs):
            log = f'[info] ------>时间是：{time.strftime("%H:%M:%S", time.localtime())}'
            print(log)
            with open(logfile, 'a') as f:
                f.write(log)
            func(*args, **kwargs)

        return writer_logging

    return logger


@main_logger()
def work():
    print('正在工作')


@main_logger('log1.log')
def work1(name):
    print(f'{name}在工作')


work()
work1('jk')
```

#### 类的方式定义装饰器

```python
import time
from functools import wraps


class Logger():
    def __init__(self, log_file='work.txt', level='INFO'):
        self.log_file = log_file
        self.level = level

    def __call__(self, func):
        @wraps(func)
        def logger(*args, **kwargs):
            log = f'{[self.level]}------> 时间是:{time.strftime("%H:%M:%S", time.localtime())}'
            print(log)
            with open(self.log_file, 'a') as f:
                f.write(log)
            func(*args, **kwargs)

        return logger


@Logger()
def work():
    print('工作')

@Logger(log_file='work1.txt',level='WARING')
def work1():
    print('共')

work()
work1()
```

### 偏函数

```python
import functools

int_2 = functools.partial(int, base=2)  # base 代表进制
print(int_2('10000'))
```

### 面向对象进阶

给实例化对象添加一个函数，使用types.MethodType(函数名,实例化对象)

给类添加一个函数,使用装饰器@classmethod

给类添加一个静态函数，使用装饰器@staticmethod

__slots__用来限制类属性,只有被规定的属性才能使用

```python
import types


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student():
    __slots__ = ('name', 'sex')


if __name__ == '__main__':
    p = Person('jk', 90)

    # 给实例对象添加一个属性
    p.sex = '女'
    # 给类添加一个属性
    Person.address = '背景'


    # 给实例对象添加一个函数
    def run(self, work):
        print(f'正在{work}')


    p.method = types.MethodType(run, p)


    # p.method('学习')

    # 给类添加一个函数
    @classmethod
    def run1(cls, wokr1):
        print(f'这是类里面的函数{wokr1}')


    Person.method = run1


    # Person.method('s')

    # 给类添加一个静态函数
    @staticmethod
    def run2(wokr):
        print(f'这是类中的静态方法{wokr}')


    Person.staticRun = run2
    Person.staticRun('3')

    s = Student()
    s.name = 'jk'
    s.sex = '女'
    # s.age=24
    print(s.name, s.sex)
```

#### property装饰器的使用

```python
class Student1():
    @property
    def age(self):
        return self._age

    @age.setter  # 当前属性值可以修改
    def age(self, value):
        if value >= 0 and value <= 88:
            self._age = value
        else:
            raise ValueError('年龄必须在0到88之间')

    @property   # 对外暴露的是name，实际上的属性值应该是self._name
    def name(self):
        self._name = '张三'
        return self._name


if __name__ == '__main__':
    s = Student1()
    s.age = 23
    print(s.age)  # age可读可写
    print(s.name)  # name只可读
```

#### 多继承

有多个父类，多个父类有多个相同的方法，按照优先级进行调用方法

优先级：自己本身>父类1>父类2>....>object

```python
class Father():
    def work(self):
        print('父亲的工作')


class Mather():
    def work(self):
        print('母亲的工作')


class Children(Father, Mather):  # 有多个父类，多个父类有相同的方法，按照优先级进行调用
    def __init__(self, name):
        self.name = name

    def work(self):
        print('自己的工作')


c = Children('jk')
c.work()
print(Children.__mro__)  # 打印Children的继承结构，按照优先级
```

#### 定制类

```
定制对象的描述信息：__str__
将对象变为一个可迭代对象，返回一个迭代器：__iter__
将对象变为一个迭代器：__next__
将对象当作list对待：__getitem__
访问对象中不存在的属性或者方法时，会出现错误AttributeError，如果不想看见这个错误：重写__getattr__方法
将对象变为一个函数：__call__
判断对象是否可以调用：callable(对象名)  返回值为布尔类型
__new__ 创建一个实例
```

```python
class Person():
    def __init__(self, name):
        self.name = name
        self.a = 0
        self.b = 1

    # 定制对象的描述信息
    def __str__(self):
        return f'Person object------>{self.name}'

    # 将对象变为一个可迭代对象，返回一个迭代器
    def __iter__(self):
        return self

    # 将对象变为一个迭代器
    def __next__(self):
        # 打印斐波拉契数列
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:  # 如果超出1000，则抛出异常
            raise StopIteration
        return self.a

    # 将对象当作list对待
    def __getitem__(self, item):  # item可能是一个下标，也可能是一个切片
        # 如果是下标
        if isinstance(item, int):
            a, b = 1, 1
            for i in range(item):
                a, b = b, a + b
            return a
        # 如果是切片
        elif isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0  # 给定初始值
            a, b = 1, 1
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    # 访问对象中不存在的属性或者方法时，会出现错误AttributeError，如果不想看见这个错误，可以重写__getattr__方法
    def __getattr__(self, item):
        if item == 'age':
            return 19
        if item == 'eat':
            return lambda: print('eat函数执行')

    # 将对象变为一个函数
    def __call__(self, *args, **kwargs):
        print('person函数执行')


p = Person('jk')
print(p)
for i in p:
    print(i)

print('索引为5的值是：', p[5])
print('切片为5-10的值是：', p[5:10])
print('--------------------------------')
print(p.age)
p.eat()
p()
print(callable(p))  # 判断对象是否可以调用
```

#### 枚举

枚举：一个名字对应一个值 类似于字典
枚举中的值从1开始，不会重复

```python
from enum import Enum

# 枚举：一个名字对应一个值 类似于字典
# Month是抬头，可以省略
Month = Enum('Month', ('一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'))
# 拿到枚举里的所有数据
print(Month.__members__)  # 枚举中的值从1开始，不会重复

# 通过名字获取值
print(Month['二'].value)
# 通过值获取名字
print(Month(2).name)


# 自定义一个颜色枚举类
class Color(Enum):
    """
    不允许key和value重复，如果重复根据value取name，只会返回第一个name
    """
    red = 200
    yellow = 100
    orange = 300
    blue = 200
print(Color(200).name)
```

#### 元类

 元类是用来创建其他的一个类

第一种方式 使用from  ....  import 的方式 引入模块之后，动态创建了一个Person类，本质上python解释器自动调用了type函数创建了一个类

第二种方式 使用type()函数创建一个类  参数一：类名，参数二：父类 参数三：类中的方法或者属性

第三种方式：第三种方式  使用metaClass创建一个元类

```python
# 第一种方式
from Python高级编程.面向对象进阶.元类.元类 import Person
# 引入模块之后，动态创建了一个Person类  本质上python解释器自动调用了type函数创建了一个类

def say(name):
    print(f'{name}在吃饭')


# 第二种方式
# 使用type()函数创建一个类  参数一：类名，参数二：父类 参数三：类中的方法或者属性
Person = type('Person', (object,), dict(say=say))


# 第三种方式  使用metaClass创建一个元类
class PersonMetaClass(type):
    def __new__(cls, name, bases, attrs):
        """
        __new__ 创建一个实例
        :param name:  类的名字
        :param bases: 父类
        :param attrs: 属性
        """

        def func(cls, words='jk'):
            print(f'{words}吃啊哈哈')

        attrs['say'] = func
        return type.__new__(cls, name, bases, attrs)


# 通过元类来创建一个类
class Person(object, metaclass=PersonMetaClass):
    pass


p = Person()
p.say('jk')
print(type(p))
print(type(Person))
a = 1
print(a.__class__.__class__)
```

```python
# 定义一个元类，用来将属性名全部转为大写
def upper_attr(class_name, class_bases, class_attrs):
    new_attrs = {}
    for name, value in class_attrs.items():
        if not name.startswith('__'): # 判断是否是私有属性
            new_attrs[name.upper()] = value
    return type(class_name, class_bases, new_attrs)


class Person(object, metaclass=upper_attr):
    name = 'jk'
    age = 23


print(hasattr(Person, 'name'))
print(hasattr(Person, 'NAME'))
print(hasattr(Person, 'AGE'))
```

```python
class UppattrMetaclass(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        for name, value in attrs.items():
            if not name.startswith('__'):
                new_attrs[name.upper()] = value
        return type.__new__(cls, name, bases, new_attrs)


class Person(object, metaclass=UppattrMetaclass):
    name = 'jk'
    age = 'jk'


print(hasattr(Person, 'name'))
print(hasattr(Person, 'NAME'))
```

### 正则表达式

```
compile 返回第一个匹配的结果
match从匹配字符串的第一个字符开始
.  匹配任意单个字符
```

### 内存管理

```python
import sys


class TestObject():
    def __init__(self):
        print(f'当前对象已被创建，当前对象的地址是{hex(id(self))}')


a = TestObject()
print(f'当前对象的引用计数为{sys.getrefcount(a)}')
b = a
print(f'当前对象的引用计数为{sys.getrefcount(a)}')
```

