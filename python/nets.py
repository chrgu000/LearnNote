
# -*- coding:UTF-8 -*-

import requests, os
from bs4 import BeautifulSoup


if __name__ == '__main__':
	target = 'https://www.biqukan.com/1_1094/5447905.html'
	resp = requests.get(url=target)
	html = resp.text
	bf = BeautifulSoup(html)
	texts = bf.find_all('div', class_ = 'showtxt')
	texts[0] = texts[0].text.replace('\xa0'*8, '\n')
	
	with open('book.txt', 'a') as book:
		pass
		#book.write(str(texts[0].text))

	print(texts)

class Downlaod(object):
	def __init__(self):
		self.server = "https://www.biqukan.com/"
		self.target = 'https://www.biqukan.com/1_1094/'
		self.names = [] #存放章节名
		self.urls = []  #存放章节链接
		slef.nums = 0  #章节数
	
	"""
    函数说明:获取章节标题和链接
	"""		
	def get_title_url(self):
		resp = requests.get(url=self.target)
		html = resp.text
		div_bf = BeautifulSoup(html)
		div = div_bf.find_all('div',  class_ = 'listmain')
		a_bf = BeautifulSoup(str(div[0]))
		
		# <a href="/1_1094/5403177.html">第一章 他叫白小纯</a>
		a = a_bf.find_all('a')
		num = len(a[16:]) #前面的节点不算正文章节，需要排除
		for each in a[16:]:
			names.append(each.string)
			urls.append(self.server + each.get('href'))
			print (names[:10], urls[:10])
	
	"""
    函数说明:获取章节内容
	"""		
	def get_content(self, url):
		resp = requests.get(url=url)
		html = resp.text
		bf = BeautifulSoup(html)
		texts = bf.find_all('div', class_ = 'showtxt')
		content = texts[0].text.replace('\xa0'*8, '\n')
		return content
	
	"""
    函数说明:将内容写入文件
	"""
	def write_to_file(self, fileName, title, content):
		
	
	
	