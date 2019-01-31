# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 14:54:25 2019

@author: WANGZEYAO
"""
### 打开一个文件

try:
    file = open('D:/pythonProject/tutorials/files/eeee.txt','w')
except Exception as e: #如果有错误，接收错误存储在e 这个变量中
    print('there is no file')
    response = input('Do you wanna create it? ')
    if response == 'yes':
        file = open('D:/pythonProject/tutorials/files/eeee.txt','w')
        print('file created')
    else:
        pass
else:# 如果没有错误，执行else中的语句
    content = input('what do you want to write in this file? ')
    file.write(content)
    print('content writed')
    file.close()
    
    