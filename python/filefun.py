#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

cur = os.path.abspath('.')
print ("cur path:",cur)
files = [cur + os.sep + x for x in os.listdir('.')]

for f in files:
	print (f, os.path.isfile(f))

print (os.path.exists(cur + os.sep + 'a'))
print (os.path.exists(cur + os.sep + 'abc'))
print (os.path.exists(cur + os.sep + 'Hello.py'))