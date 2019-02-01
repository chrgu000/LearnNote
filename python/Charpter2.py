#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#切片

ls = ['z','a','s','d','f','g']

#取前3个元素, 从下标0开始，到3结束，不包括3
print (ls[0:3])

#如果第一个索引是0,则可省略，前3个数
print (ls[:3])

#支持倒数切片，后2个数
print (ls[-2:])

lt = list(range(100))
print (lt[5:10])

print (lt[:20:2]) #前20个数，每2个取一个

print (lt[::5]) #所有数，每5个取一个

#字符串也可以看成list,tuple也可以切片


# 迭代
d = {'a':1, 'b':2, 'c':3}
for key in d:
	print(key, d.get(key))

for k,v in d.items():
	print (k,'=',v)
	
for ch in 'ABCD':
	print(ch)


#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
print (list(range(20)))

lt2 = []
for x in range(1,11):
	lt2.append(x*x)
	
print (lt2)

lt3 = [x*x for x in range(1,11)]
print (lt3)

# 打印目录结构
import os
print ([d for d in os.listdir('C:'+os.sep)])


# 生成器
#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
#而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
#在Python中，这种一边循环一边计算的机制，称为生成器：generator。

#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
#我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？

#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
lt = [x for x in range(1,11)]
print (lt)

gn = (x for x in range(1,11))
print (gn)

for x in range(10):
	print (next(gn))
	
gn = (x for x in range(1,11))	
for x in gn:
	print (x)
	
# 迭代器

from collections import Iterator
print (isinstance([], Iterator))
print (isinstance(iter([]), Iterator))


#map 
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素
#并把结果作为新的Iterator返回。

def f(x):
	return x*x

r = map(f, list(range(1,11)))
print (list(r))

print (list(map(str, list(range(2,10))))) # 把序列转成字符

#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数
#，reduce把结果继续和序列的下一个元素做累积计算

from functools import reduce

def add(x,y):
	return x + y
	
ret = reduce(add, list(range(1,11))) # 求序列的和
print (ret)


#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(x):
	return  x % 2 == 1
	
print (list(filter(is_odd, range(1,11))))

# 排序
lt = sorted([5,1,9,7,0,-8,-3])
print (lt)

#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
lt = sorted([5,1,9,7,0,-8,-3], key=abs)
print (lt)


#可变参数的求和
def get_sum(*val):
	sum = 0
	for v in val:
		sum = sum + v
	return sum
	
print (get_sum(1,2,3))

nums = list(range(1,20))
print (get_sum(*nums))

#函数作为返回值
#如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
	def sum():
		ret = 0
		for v in args:
			ret = ret + v
		return ret
	return sum

#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1,3,5,7,9)
print(f)

#调用函数f时，才真正计算求和的结果
print (f())

#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f2 = lazy_sum(1,3,5,7,9)
print (f == f2)

#匿名函数 lambda x: x * x  键字lambda表示匿名函数，冒号前面的x表示函数参数
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
lt = map(lambda x : x *x, range(1,11))
print (list(lt))

#装饰器 类似于AOP


#假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
#但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

def log(func):
	def wrapper(*args, **kw):
		print('call %s()---' % (func.__name__))
		return func(*args, **kw)
	return wrapper
	
#借助Python的@语法，把decorator置于函数的定义处	
@log
def now():
	print ("2018-1-1")

now()

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now2():
    print('2015-3-25')
	
now2()

# 偏函数
#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
# int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
print (int('123', base=8))
print (int('123', 8))

#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
#返回一个新的函数，调用这个新函数会更简单。
import functools
int2 = functools.partial(int, base=2)
print(int2('1111'))

#相当于
kw = { 'base': 2 }
int('10010', **kw)
print (int('1111', **kw))