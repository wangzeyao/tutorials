import numpy as np
import tkinter as tk

w

a = np.arange(4)
print(a)


b = a
c = a
d = b
print(b is a) #b就是a，只是a另一个命名
print(d is a) #d也是a

a[0] = 11
print(b)  #b会跟着改变

d[1:3] = [22,33]
print(a) #同样改变d的是时候a也会改变

b = a.copy() #deep copy
a[3] = 44
print(b) #deep copy把a的值付给b但是并没有关联起来


