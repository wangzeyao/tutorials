import numpy as np

A = np.arange(12).reshape((3, 4))
print(A)

# 分割
print(np.split(A, 2, axis=1))  # 横向的分割成两块
print('\n\n\n')
print(np.array_split(A, 3, axis=1))  # 不等量的分割，第一个array有两列，后两个只有一列

print(np.vsplit(A, 3))  # 同样的纵向分割
print(np.hsplit(A, 2))  # 同样的横向分割
