# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 13:59:01 2019

@author: WANGZEYAO
"""

# tuple and list

a_tuple = (12, 13, 43)
b_tuple = 12, 13, 45

a_list = [12, 13, 45]

# 进行迭代输出
for content in a_list:
    print(content)

# list列表功能
a = [1, 2, 3, 4, 3, 2, 1, 0]
a.insert(1, 0)  # 将数字0添加到‘1’位置
a.remove(2)  # 删除第一个值为2的元素
print(a[-1])  # 打印最后一个元素
print(a[0:3])  # 打印0，1，2位元素
print(a[-3:])  # 打印倒数第三个到最后一个元素
a.index(2)  # 第一次出现值为的索引
a.count(3)  # 计算出现的次数
a.sort()  # 默认从小到大排序
a.sort(reverse=True)  # 从大到小排序

# 多维列表
a = [1, 3, 4, 5]
multi_dim_a = [[1, 2, 3],
               [2, 3, 4],
               [3, 4, 5]]

# 字典dictionary,有key和value两种元素，一个key对应一个value
# key必须是不可变的，可以用数字或字符串或者元组充当key
# value可以是任何东西包括自定义的class
d1 = {'Name': 'WANGZeyao', 'Age': 24}
print(d1['Name'])  # 取出key对应的值WANGZeyao
d1['Age'] = 18  # 修改value
del d1['Name']  # 删除对应的key和value
d1.clear()  # 清空字典
