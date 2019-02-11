# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:55:24 2019

@author: WANGZEYAO
"""
# 写入内容到文件
text = 'This is my first test.\nThis is my next line'
# print(text)
my_file = open('D:/pythonProject/tutorials/files/test0.txt', 'w')
my_file.write(text)
my_file.close()

# 增加内容到文件
append_text = '\tThis is my second test.\n\tThis is the second line.\n\tThis is the third line'  # 延伸 使用 \t 对齐
# print(text)
my_file = open('D:/pythonProject/tutorials/files/test0.txt', 'a')
my_file.write(append_text)
my_file.close()

# 从文件中读取内容
file = open('D:/pythonProject/tutorials/files/test0.txt', 'r')  # 实际上是把文件存到file中
content = file.read()  # 读取文件的内容
# print(content)
file.close()

file = open('D:/pythonProject/tutorials/files/test0.txt', 'r')
line1 = file.readline()  # 读取第一行
line2 = file.readline()  # 读取第二行
print(line1)
file.close()

file = open('D:/pythonProject/tutorials/files/test1.txt', 'r')
lines = file.readlines()  # 将文件的每一行以python_list的形式储存，方便以后的迭代
print(lines)
