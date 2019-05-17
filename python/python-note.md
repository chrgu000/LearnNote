# Python学习

## 基础学习代码

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

##  模块

Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。

模块让你能够有逻辑地组织你的 Python 代码段。

把相关的代码分配到一个模块里能让你的代码更好用，更易懂。

模块能定义函数，类和变量，模块里也能包含可执行的代码。

```python
创建模块 support.py
def print_func( par ):
   print "Hello : ", par
   return


# 导入模块
import support
 
# 现在可以调用模块里包含的函数了
support.print_func("Runoob")
```

Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。例如，要导入模块 fib 的 fibonacci 函数

```
from fib import fibonacci
```

这个声明不会把整个 fib 模块导入到当前的命名空间中，它只会将 fib 里的 fibonacci 单个引入到执行这个声明的模块的全局符号表。

把一个模块的所有内容全都导入到当前的命名空间也是可行的

```
from modname import *
```

当你导入一个模块，Python 解析器对模块位置的搜索顺序是：

- 1、当前目录
- 2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
- 3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。

模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。



python中的包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。

简单来说，包就是文件夹，但该文件夹下必须存在 `__init__.py` 文件, 该文件的内容可以为空。`__init__.py` 用于标识当前文件夹是一个包。

考虑一个在 **package_runoob** 目录下的 **runoob1.py、runoob2.py、__init__.py** 文件，test.py 为测试调用包的代码，目录结构如下：

```python
test.py
package_runoob
|-- __init__.py
|-- runoob1.py
|-- runoob2.py

#使用
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 导入 Phone 包
from package_runoob.runoob1 import runoob1
from package_runoob.runoob2 import runoob2
 
runoob1()
runoob2()
```



## 切片等高级操作

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



## 类的使用

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print ('hello nothing')
	elif len(args) == 2:
		print ('hello',args[1])
	else:
		print ("too many thing")
		

if __name__ == '__main__':
	test()
	
#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
#而如果在其他地方导入该hello模块时，if判断将失败

#作用域
#正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
#类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
#hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
#因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。


#默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
import sys
print (sys.path)

#如果我们要添加自己的搜索目录，有两种方法：

#一是直接修改sys.path，添加要搜索的目录：
import os
sys.path.append('C:' + os.sep)
print (sys.path)

#第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
print ('\n\n')

在Python中，定义类是通过class关键字：
class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

class Student(object):

	def __init__(self, name, age):
		self.name = name
		self._age = age

	def print_info(self):
		print (self.name, self._age)
		
bart = Student('lester', 22)
print(bart)
print (Student)
bart.print_info()
print (bart.name)

#print (bart.age) 属性的名称前加上 下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）
#变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量

#由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去

#注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去

#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

class Animal(object):
	def run(self):
		print("animal is running")
		
class Dog(Animal):
	def run(selt):
		print('dog is running')
	
class Cat(Animal):
	def run(self):
		print('cat is running')
	
dog = Dog()
cat = Cat()
dog.run()
cat.run()
print (isinstance(dog, Dog))
print (isinstance(dog, Animal))


#我们来判断对象类型，使用type()函数
print (type(123))
print (type('1'))
print (type(dog))
print (type(abs))

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
print (dir (dog))
print ('\n')
print (dir ('a'))

#果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
print (hasattr(dog, 'run'))
print (getattr(dog,'run','default'))

#给实例绑定属性的方法是通过实例变量，或者通过self变量
#但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有,当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。

#类通过self 绑定的变量属于实例本身的属性，如果定义在类中，则属于类属性
class Stu(object):
	name = 'baby'
    
>>> class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student


#实例属性的优先级高于类属性	
stu = Stu()
s2 = Stu()
stu.name = 'ant' # 给实例绑定name属性
print (stu.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print (s2.name)
del stu.name # 如果删除实例的name属性 
print (stu.name) #再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了


```

## 文件操作

```python

#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
#open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
#Python引入了with语句来自动帮我们调用close()方法

try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
        
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

    #前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件
>>> f = open('/Users/michael/test.jpg', 'rb')
>>> f.read()

w+：打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a+：打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
wb+, ab+ 对二进制文件进行读写，追加读写


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

 #序列化 Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
import json
d = {'a':1,'b':2,'c':3}
j = json.dumps(d) #把Python对象变成一个JSON
print (j)
print (json.loads(j), isinstance(json.loads(j), dict)) #把JSON反序列化为Python对象
#用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化

对自定义对象进行序列化和反序列化，必须实现特定方法
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])        
    
s = Student('Bob', 20, 88)

print(json.dumps(s, default=student2dict))
不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s, default=lambda obj: obj.__dict__))

#反序列化
print(json.loads(json_str, object_hook=dict2student))

#获取当前日期和时间
from datetime import datetime 
now = datetime.now()
print (now)
print (now.strftime('%Y %m %d %H:%M:%S'))

#内置的base64可以直接进行base64的编解码
import base64
s = base64.b64encode(b'hello')
print (s)
print (base64.b64decode(s))
```

## 网络操作

Python内置的urllib模块

Python第三方库，处理URL资源特别方便

pip install requests

要通过GET访问一个页面
>>> ```python
>>> import requests
>>> r = requests.get('https://www.douban.com/') # 豆瓣首页
>>> r.status_code
>>> 200
>>> r.text
>>> ```

对于带参数的URL，传入一个dict作为params参数
>>> ```python
>>> r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
>>> r.url # 实际请求的URL
>>> 'https://www.douban.com/search?q=python&cat=1001'
>>> ```

requests自动检测编码，可以使用encoding属性查看

无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象

要发送POST请求，只需要把`get()`方法变成`post()`，然后传入`data`参数作为POST请求的数据

```
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
```

requests默认使用`application/x-www-form-urlencoded`对POST数据编码。如果要传递JSON数据，可以直接传入json参数：

```
params = {'key': 'value'}
r = requests.post(url, json=params) # 内部自动序列化为JSON
```

除了能轻松获取响应内容外，requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头，获取指定的Cookie

```python
>>> r.headers
{Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Content-Encoding': 'gzip', ...}
>>> r.headers['Content-Type']
'text/html; charset=utf-8'
 >>> r.cookies['ts']
'example_cookie_12345'
 
#要在请求中传入Cookie，只需准备一个dict传入cookies参数：
 >>> cs = {'token': '12345', 'status': 'working'}
>>> r = requests.get(url, cookies=cs)
 
#要指定超时，传入以秒为单位的timeout参数：
r = requests.get(url, timeout=2.5) # 2.5秒后超时
```

