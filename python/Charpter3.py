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

#类通过self 绑定的变量属于实例本身的属性，如果定义在类中，则属于类属性
class Stu(object):
	name = 'baby'
	
stu = Stu()
s2 = Stu()
stu.name = 'ant' # 给实例绑定name属性
print (stu.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print (s2.name)
del stu.name # 如果删除实例的name属性 
print (stu.name) #再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了