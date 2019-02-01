#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

#print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出, ','号被替换为空格
print('hello', 'world')

print('100+200 =', 100+200)

#从控制台读取输入，并输出提示
#name=input('enter name:')
#print('name is',name)

#符串是以单引号'或双引号"括起来的任意文本

	
#Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('a'), chr(66))

#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
#如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#Python对bytes类型的数据用带b前缀的单引号或双引号表示
#要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
x = b'abc'
y = 'abc'
print(x, y)

print('abc'.encode('ascii'), 'abc'.encode('utf-8'), '你'.encode('utf-8'))

print(b'abc'.decode('ascii'), b'\xe4\xb8\xad'.decode('utf-8'))

print(len('abc'), len('中文'), len('中文'.encode('utf-8')))

#在Python中，采用的格式化方式和C语言是一致的，用%实现, %f 
name = 'lester'
age = 11
score = 5.5
print('%s, %d, %f, %x' % (name, age, score, age))

#list是一种有序的集合，可以随时添加和删除其中的元素。
list = ['h1','h2','h3']
print(list[0],list, list[-1])
list.insert(1,'hh')
print(list)
list.pop(1)
print(list)

#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
tuple = ('t1','t2','t3')
print(tuple)

age = 16
if age > 18:
	print('adult')
elif age > 60:
	print('old')
else:
	print('teenager')


#score = input('input score:')
#s = int(score)
s = 60
if s > 60:
	print ('good')
else:
	print('bad')

#Python的循环有两种，一种是for...in循环
listName = ['aa', 'bb', 'cc']
for name in listName:
	print ('name is', name)
	
#Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
print (range(5))
for x in range(10):
	print(x)
	
#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
#计算100以内所有奇数之和
sum = 0
i = 0
while i < 100:
	if i % 2 == 1:
		sum = sum + i
	i = i + 1
print(sum)


#如果要提前结束循环，可以用break语句：
i = 1
while i < 100:
	if i > 10:
		break
	print(i)
	i = i + 1

#也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
#只打印奇数
i = 1
while i < 100:
	i = i + 1
	if i % 2 ==  1:
		continue
	print(i)
	
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储
dict = {'z':60,'x':70, 'y':80}
print(dict['z'], dict)

# 判断 key 是否存在
print ('z' in dict, 'a' in dict)

#二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print (dict.get('z'), dict.get('a'), dict.get('a',99))

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
dict.pop('z')
print(dict)

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1,2,2,3,4])
print(s)
s.add(5)
s.remove(2)

print(abs(-889))
#函数max()可以接收任意多个参数，并返回最大的那个
print (max(1,11))

#数据类型转换函数 int() float() str() bool()
#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
abs_new = abs
print(abs_new(-88))
print (hex(100)) #把整数转换成16进制

#定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
#然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
	if x > 0:
		return x
	else:
		return -x
		
print (my_abs(-55))

#如果想定义一个什么事也不做的空函数，可以用pass语句：
#pass语句什么都不做，那有什么用？
#实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

#数据类型检查可以用内置函数isinstance()实现
print (isinstance(56, (int, float)))

#返回多个值

#必选参数在前，默认参数在后
def move(x, y, step, angle=0):
	nx = x + (step+angle)*10
	ny = y + (step+angle)*20
	return nx,ny
# *key 可变参数， **key 关键参数，键值对

	
print(move(5,6,2))
#原来返回值是一个tuple

# 递归函数
def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)

print (fact(10))

