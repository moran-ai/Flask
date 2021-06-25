linux

linux只有一个根目录，用/表示

无法ping通外网

vi /etc/resolv.conf



nameserver  windows的DNS地址

```
配置Centos阿里云yum源  需要root
① mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
② curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
③ yum makecache
```

```
查看yum的安装内容
yum repolist
```

```
一个源不够，再配置一个源
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo 
```

```
修改主机名
cat /etc/sysconfig/network
hostnamectl set-hostname 主机名
然后修改host
vi /etc/hosts
当前主机的IP  主机名
例如：
	192.168.164.130   mylinux
```

```
修改DNS配置
cat /etc/resolv.conf
nameserver 当前主机电脑的DNS(不是虚拟机的DNS)
```

```
rpm -ivh mysql-community-client-8.0.25-1.el7.x86_64.rpm --nodeps
```

