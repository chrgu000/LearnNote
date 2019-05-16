# Python学习

基础学习代码

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#编写文件：my.py ,执行文件： python my.py

#print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出, ','号被替换为空格
print('hello', 'world')

print('100+200 =', 100+200)

#从控制台读取输入，并输出提示
#name=input('enter name:')
#print('name is',name)

#符串是以单引号'或双引号"括起来的任意文本

在一个.py文件中，如果不是在定义函数，也就是说不是在def关键字的内嵌结构内，python会默认其余部分函数是main函数，并自动执行，但正规工程中，一般都会将main函数写为
#hello.py
def sayHello():
    str="hello"
    print(str);

if __name__ == "__main__":
    print ('This is main of module "hello.py"')
    sayHello()
    
    
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

#获取环境变量
import os
path = os.getenv('java_home')
print (path)
```

## **切片等用法**

```python
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

#字符串也可以看成list, tuple也可以切片


# 迭代
d = {'a':1, 'b':2, 'c':3}
for key in d: #dict的默认遍历是对其key遍历
	print(key, d.get(key))

for k,v in d.items(): #对 key value进行遍历
	print (k,'=',v)
	
for ch in 'ABCD':
	print(ch)


#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
print (list(range(20)))

lt2 = []
for x in range(1,11): #从1到10
	lt2.append(x*x)
	
print (lt2)

lt3 = [x*x for x in range(1,11)] #这个用法比较常见
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

gn = (x for x in range(1,11)) #generator
print (gn)

for x in range(10):
	print (next(gn))
	
gn = (x for x in range(1,11))	
for x in gn:
	print (x)
	
# 迭代器
from collections import Iterator
print (isinstance([], Iterator)) #False
print (isinstance(iter([]), Iterator)) #True


#map 
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素
#并把结果作为新的Iterator返回。
#  map(f, iter)

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
def get_sum(*val): #声明的参数形式 *val
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
print(f) #这里只是打印了 sum函数信息

#调用函数f时，才真正计算求和的结果
print (f()) #这里相当于sum() 调用了sum

#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f2 = lazy_sum(1,3,5,7,9)
print (f == f2)

#匿名函数 
lambda x: x * x  #关键字lambda表示匿名函数，冒号前面的x表示函数参数
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
```









