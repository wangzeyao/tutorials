# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:49:56 2019

@author: WANGZEYAO
"""

a = None
def fun():
    global a # 声明a为全局变量a
    a = 20
    
print('before: ',a)
fun()
print('after: ',a)