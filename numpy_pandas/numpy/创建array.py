import numpy as np

array = np.array([[1, 2, 3],
                  [3, 4, 5],
                  [4, 5, 6]],
                 dtype=np.float32  # 定义value的形式
                 )

print(array, array.dtype)

zero = np.zeros((3, 4))  # 创建3行4列的0矩阵，注意要用括号括
one = np.ones((4, 4))  # 生成1矩阵
arange = np.arange(10, 20, 2)  # 生成连续数组，起始值，终止值，步长,
# 注意不包括终止值，类似range
print(arange)

a = np.arange(12)  # 生成一个0到11的数列
print(a)

a = a.reshape((3, 4))  # 将a改变为3行4列的矩阵
print(a)

a = np.linspace(1, 10, 5)  # 生成1到10等分为5段的数列
print(a)
