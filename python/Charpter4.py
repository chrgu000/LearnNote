#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
#open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
#Python引入了with语句来自动帮我们调用close()方法

#调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
with open(".\\Hello.py", 'r', encoding='utf-8', errors='ignore') as f:
	print (f.read())
	
#如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
with open(".\\backup.py", 'r', encoding='utf-8', errors='ignore') as f:
	for s in f.readlines():
		print (s)
		
with open('.\\file.txt', 'w') as f:
	f.write('hello, file\n')
	f.write(str(list(range(10))))
	
with open('.\\file.txt', 'a') as f:
	f.write('\n' + str([x*x for x in range(1,11)]))
	
from io import StringIO
f = StringIO()
f.write('hi')
f.write(' ')
f.write('baby')
print (f.getvalue())

f = StringIO('hi\nboy')
while True:
	s = f.readline()
	if s == '':
		break
	print (s)
	
from io import BytesIO
f = BytesIO()
f.write('中午'.encode('utf-8'))
print (f.getvalue())

f2 = BytesIO('不容易'.encode('utf-8'))
print(f2.read(),'\n')

import os
print(os.name)
print (os.environ)

print ('\n',os.environ.get('PATH'))

#查看当前目录的绝对路径:
print (os.path.abspath('.'))
#os.mkdir('.\\test')
#os.rmdir('.\\test')
#os.remove('f.txt')
#os.rename('.\\file.txt', '.\\f.txt')

fs = [x for x in os.listdir('.')]
print (fs)


fs = [x for x in os.listdir('C:\\')]
print (fs)
for f in fs:
	print (f, os.path.isfile(f))

import json
d = {'a':1,'b':2,'c':3}
j = json.dumps(d)

print (j)
print (json.loads(j), isinstance(json.loads(j), dict))

from datetime import datetime 
now = datetime.now()
print (now)
print (now.strftime('%Y %m %d %H:%M:%S'))

import base64
s = base64.b64encode(b'hello')
print (s)
print (base64.b64decode(s))

from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k,v in f.getheaders():
		print (k,':', v)
	print ('data:', data.decode('utf-8'), '\n')
	
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))