#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#https://zhuanlan.zhihu.com/p/33288426


from PIL import Image
from io import BytesIO
import requests,json

# 带参数的GET请求,timeout请求超时时间
params = {'key1': 'python', 'key2': 'java'}
r = requests.get(url='http://httpbin.org/get', params=params, timeout=3)

# 注意观察url地址，它已经将参数拼接起来
print('URL地址：', r.url)
# 响应状态码，成功返回200，失败40x或50x
print('请求状态码：', r.status_code)
print('header信息:', r.headers)
print('cookie信息：', r.cookies)
print('响应的数据：', r.text)
# 如响应是json数据 ，可以使用 r.json()自动转换为dict
print('响应json数据', r.json())


# 请求获取图片并保存
r = requests.get('https://pic3.zhimg.com/247d9814fec770e2c85cc858525208b2_is.jpg')
i = Image.open(BytesIO(r.content))
# i.show()  # 查看图片
# 将图片保存
with open('img2.jpg', 'wb') as fd:
   for chunk in r.iter_content():
       fd.write(chunk)



# 带参数表单类型post请求
data={'custname': 'woodman','custtel':'13012345678','custemail':'woodman@11.com',
     'size':'small'}
r = requests.post('http://httpbin.org/post', data=data)
print('响应数据：', r.text)


# json数据请求
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
# 可以使用json.dumps(dict) 对编码进行编译
r = requests.post(url, data=json.dumps(payload))
print('响应数据：', r.text)

# 可以直接使用json参数传递json数据
r = requests.post(url, json=payload)
print('响应数据：', r.text)


# 上传单个文件
with open('report.txt', 'a') as f:
	f.write('hi')
	
url = 'http://httpbin.org/post'
# 注意文件打开的模式，使用二进制模式不容易发生错误
files = {'file': open('report.txt', 'rb')}
# 也可以显式地设置文件名，文件类型和请求头
# files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
r = requests.post(url, files=files)
r.encoding = 'utf-8'
print(r.status_code)
print (r.text)




