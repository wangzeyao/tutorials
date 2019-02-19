import numpy as np

A = np.arange(3, 15)

print(A)

print(A[3])

A = A.reshape((3, 4))
print(A)
print(A[2])
print(A[2, 1])  # 两种方法一样
print(A[2][1])

print(A[2, :])  # 第三行的所有数
print(A[2, 1:3])  # 第三行，第二个到第三个数

for row in A:  # 迭代矩阵中的行
    print(row)

for col in np.transpose(A):  # 并不能直接用for col in A: 用转置后的矩阵迭代行
    print(col)

print('flatten()函数', A.flatten())
for item in A.flat:  # 将矩阵变为一行
    print(item)
