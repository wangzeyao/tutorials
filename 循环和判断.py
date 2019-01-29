# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 17:40:01 2019

@author: WANGZEYAO
"""

### while循环

# 1.如果 while 后面接着的语句数据类型 None, 将会返回 False。
# 2.在 Python 中集合类型有 list、 tuple 、dict 和 set 等，如果该集合对象作为 while 判断语句， 
#   如果集合中的元素数量为 0，那么将会返回 False, 否则返回 True。
a = range(10)
while a:
    print(a[-1])
    a = a[:len(a)-1]

### range的使用
# 1.range(start,stop),不包括stop值
    for i in range(1,5):
        print(i)

# 2.range(stop),相当于range(0,stop)
    for i in range(5):
        print(i)

# 3.range(start,stop,step),直到等于或大于stop
    for i in range(0,10,2):
        print(i)
        
        
### 迭代器
#Python 中的 for 句法实际上实现了设计模式中的迭代器模式 ，所以我们自己也可以按照迭代器的要求自己生成
#迭代器对象，以便在 for 语句中使用。 只要类中实现了 __iter__ 和 next 函数，那么对象就可以在 for 语
#句中使用。 现在创建 Fibonacci 迭代器对象

class Fib(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

# using Fib object
for i in Fib(5):
    print(i)
    
    
### 生成器
#除了使用迭代器以外，Python 使用 yield 关键字也能实现类似迭代的效果，yield 语句每次 执行时，立即返回结果给
#上层调用者，而当前的状态仍然保留，以便迭代器下一次循环调用。这样做的 好处是在于节约硬件资源，在需要的时候才
#会执行，并且每次只执行一次。

def fib(max):
    a, b = 0, 1
    while max:
        r = b
        a, b = b, a+b
        max -= 1
        yield r

# using generator
for i in fib(5):
    print(i)
    
### 三目运算符
# 形式： var = var1 if condition else var2
    
worked = True
result = 'done' if worked else 'not yet'
print(result)

###elif
x = 4
y = 2
z = 3
if y == 1:
    print('y=1')
elif y == 2:
    print('y=2')
elif y == 3:
    print('y=3')
elif z == 3:
    print('z=3')
else:
    print('x = 1')
    