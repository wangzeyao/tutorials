import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
print(A)
print(A.shape)  # A和B为序列，不是矩阵，所以np.transpose(A)不起作用
print(B)

# 上下合并
print('vertical stack\n', np.vstack((A, B)))
# 左右合并
print('horizontal stack\n', np.hstack((A, B)))

# 增加一个维度
print(A[:, np.newaxis])  # 在列上加一个维度
print(A[np.newaxis, :])  # 在行上加一个维度

A = A[:, np.newaxis]
B = B[:, np.newaxis]
print('horizontal stack\n', np.hstack((A, B)))

# 多个array的合并
C = np.concatenate((A, B, B, A), axis=0)  # axis = 0,纵向合并，axis = 1横向合并
print(C)
