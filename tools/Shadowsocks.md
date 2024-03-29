# 搬瓦工

网站：

<https://www.bandwagonhost.net/2617.html>

<https://bwh88.net/>

账号：375531039@qq.com  密码：zht123456

**BWH26FXH3HIQ**

2xLaZgnytmtE

**一道隐形的墙**

众所周知，天朝局域网通过 [GFW](http://zh.wikipedia.org/wiki/%E9%87%91%E7%9B%BE%E5%B7%A5%E7%A8%8B) 隔离了我们与外界的交流，当然，这个隔离并非完全隔离，而是选择性的，天朝不希望你上的网站就直接阻断。每一个网络请求都是有数据特征的，不同的协议具备不同的特征，比如 HTTP/HTTPS 这类请求，会很明确地告诉 GFW 它们要请求哪个域名；再比如 TCP 请求，它只会告诉 GFW 它们要请求哪个 IP。

GFW 封锁包含多种方式，最容易操作也是最基础的方式便是域名黑白名单，在黑名单内的域名不让通过，IP 黑白名单也是这个道理。**如果你有一台国外服务器不在 GFW 的黑名单内**，天朝局域网的机器就可以跟这一台机器通讯。那么一个翻墙的方案就出来了：境内设备与境外机器通讯，境内想看什么网页，就告诉境外的机器，让境外机器代理抓取，然后送回来，我们要做的就是保证境内设备与境外设备通讯时不被 GFW 怀疑和窃听。

ssh tunnel 是比较具有代表性的**防窃听通讯隧道**，通过 ssh 与境外服务器建立一条加密通道，此时的通讯 GFW 会将其视作普通的连接。由于大家都这么玩，GFW 着急了，于是它通过各种流量特征分析，渐渐的能够识别哪些连接是 ssh 隧道，并尝试性的对隧道做干扰，结果还是玩不过 GFW，众多隧道纷纷不通。

如果你理解了上面那道隐形的墙的原理，那 Shadowsocks 的原理就可以用一句简单的描述来理解了：它发出的 TCP 包，没有明显包特征，GFW 分析不出来，当作普通流量放过了。

**1. 基本原理**

具体而言，Shadowsocks 将原来 ssh 创建的 Socks5 协议拆开成 Server 端和 Client 端，两个端分别安装在境外服务器和境内设备上。

```
+------+     +------+     +=====+     +------+     +-------+
| 设备  | <-> |Client| <-> | GFW | <-> |Server| <-> | 服务器 |
+------+     +------+     +=====+     +------+     +-------+
```

Client 和 Server 之间可以通过多种方式加密，并要求提供密码确保链路的安全性。

**2. 服务器端部署**

Shadowsocks 封装后对用户而言就是一个程序指令，以 Ubuntu 为例，首先安装 pip，

```
apt-get install python-pip
pip install shadowsocks
```

注意 pip 的安装现在要求 python 版本大于等于 2.6，然后通过 pip 安装 shadowsocks。启动 shadowsocks 有两种方式，一种是通过一行命令直接启动：

```
ssserver -p PORT -k PASSWORD -m rc4-md5 --log-file /tmp/ss.log -d start
```

另一种是使用 config 文件启动，如先配置好文件（/etc/shadowcfg.json）：

```
vim /etc/shadowcfg.json
{
    "server":"93.179.96.93",
    "local_address":"127.0.0.1", 
    "local_port":1080, 
    "port_password":{ 
         "443":"abcd123456", 
         "6666":"abcd123456", 
         "6667":"abcd123456",
	 	 "6668":"abcd123456"    
    }, 
    "timeout":300, 
    "method":"rc4-md5", 
    "fast_open": false 
}
```

然后通过 ssserver 启动：

```
ssserver -c /etc/shadowcfg.json -d start

ssserver -c /etc/shadowcfg.json --user nobody -d start

ssserver -c /etc/shadowcfg.json -d stop

设置开机启动
sudo ssserver -c /etc/shadowcfg.json --user nobody -d start

pip show shadowsocks
```

