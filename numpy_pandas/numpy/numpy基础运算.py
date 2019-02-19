import numpy as np

a = np.array([[10, 20, 30, 40]])
b = np.arange(1, 5, 1)

# 加减乘除
print('加减乘除：')
c = a - b
print(c)

c = a + b
print(c)

c = a * b
print(c)

c = a / b
print(c)

# b的平方
print('平方： ')
c = b ** 2
print(c)

# 三角函数
print('三角函数: ')
c = 10 * np.sin(a)
print(c)

# 显示b中的元素哪些小于3
print('显示b中的元素哪些小于3')
print(b, '\n', b < 3)

# 矩阵相乘
print('矩阵乘法: ')
matrix = np.array([[1, 1],
                   [0, 1]],
                  dtype=int)
b = b.reshape((2, 2))

c = matrix * b
print('逐个相乘: ' + '\n', c)

c = np.dot(matrix, b)
print('矩阵乘法: ' + '\n', c)
c = matrix.dot(b)  # 矩阵乘法的另一种形式

# 创建随机生成的数组,最大值，最小值，求和
print('最大值，最小值，求和')
a = np.random.random((2, 4))  # 参数为shape
print(a)
a = np.array([[1, 5, 5, 2],
              [9, 6, 2, 8],
              [3, 7, 9, 1]])
print(a, a.shape)
print('求和: ', np.sum(a))
print('行求和: ', np.sum(a, axis=0))  # 行求和，第一行加第二行加第三行
print('列求和: ', np.sum(a, axis=1))  # 列求和，第一列加第二列加第三列
print('最小值： ', np.min(a))
print('每列最小值： ', np.min(a, axis=0))  # 这里axis=0变成了每列最小值，似乎跟上面有些相反，不是很懂
print('每行最小值： ', np.min(a, axis=1))
print('最大值: ', np.max(a))


