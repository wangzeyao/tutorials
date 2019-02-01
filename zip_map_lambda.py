# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 13:06:08 2019

@author: WANGZEYAO
"""
### zip的用法，可以zip多个元素
a = [1,2,3]
b = [4,5,6]
print(list(zip(a,b))) # 将a的第一位和b的第一位，a的第二位和b的第二位分装在一起

# 应用
for i,j in zip(a,b):
    print(i/2,j*2)
    
    
###  lambda
def fun1(x,y):
    return (x+y)

fun2 = lambda x,y:x+y # 使用lambda定义同样功能的方程


### map
map(fun1,[1],[2])# 将函数和其参数绑定在一起
print(list(map(fun1,[2],[2])))

print(list(map(fun1,[2,3],[2,4]))) # 可以有多个元素，得到两个结果