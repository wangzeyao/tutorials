import numpy as np

# 创建numpy可识别的数组
array = np.array([[1, 2, 3],
                  [2, 3, 4]])

print(array)

# 数组的维数
print('number of dim: ', array.ndim)

# 数组的结构
print('shape: ', array.shape)

# 数组的大小也就是总共的元素数量
print('size: ', array.size)
