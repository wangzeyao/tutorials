import numpy as np

A = np.arange(2, 14).reshape((3, 4))
print(A)

# 最小值的索引
print('最小值的索引，最大值同理:', np.argmin(A))

# 计算平均值
print('平均值：', np.mean(A))

# 中位数
print('中位数：', np.median(A))

# 累加
print('累加：', np.cumsum(A))

# 每两个数之前的差
print('相差:', np.diff(A))

# 找出非0的数
print('非零数:', np.nonzero(A))  # 第一个array是非零数的行数，第二个array输出非零列的列数

# 排序
print('每行内部排序：', np.sort(A))

# 矩阵的转置
print('矩阵的转置：', np.transpose(A))

# clip
print('Clip: ', np.clip(A, 5, 9))  # 把矩阵中小于5的数改成5，大于9的数改成9后输出
