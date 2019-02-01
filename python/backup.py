#!/usr/bin/pyhton
#Filename: backup.py
#功能说明:备份文件，以当前日期为子目录存放备份后的文件

import os
import time

#要备份的目录，可在此列表中增加
source = [r'C:\logs']

#备份文件存放的目录
target_dir = 'D:/backup/'
os.mkdir(target_dir)
#取当前时间为备份子目录名
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

#在备份文件名中加入注释
comment = input('Enter a comment:')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
                 comment.replace(' ',  '_') + '.zip'

#如果目标目录不存在就创建
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',  today)

#备份命令，可替换为7z, Linux下可改为tar等
zip_command = "7z a %s %s" %(target,  ' '.join(source))

#执行命令
if os.system(zip_command) == 0:
    print('Successful backup to',  target)
else:
    print('Backup failed')