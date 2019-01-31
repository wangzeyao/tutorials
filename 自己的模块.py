# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 14:33:27 2019

@author: WANGZEYAO
"""
import sys
sys.path.append('D:/pythonProject/tutorials/files')
import pck.printData as pt

### 方法一 将两个文件放在同一个目录下



### 方法二 将自定义模块打包
### 先把.py文件都放进一个文件中，添加一个__init__.py文件
### 再将整个文件夹放到/Lib/sit-packages/ 中，最后再import 文件夹名字.文件名字
data = 30
pt.print_data(data)

### 方法三 设置模块搜索路径
### import sys
### sys.path.append('D:/pythonProject/tutorials/files')
### import pck.printData as pt