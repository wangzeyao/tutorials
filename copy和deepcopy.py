import copy

a = [1, 2, 3]
b = a
print('id b: ', id(b), '\nid a: ', id(a))  # 同一个id，改变a的时候会改变b

c = copy.copy(a)  # 使用浅复制
print(id(a) == id(c))  # 并不是同一个id，改变a的时候不会改变c

a = [1, 2, [3, 4]]  # 其中[3,4]为a的内部元素
d = copy.copy(a)  # d为a的浅拷贝
print(id(a) == id(d))

a[2][0] = 3224
print(d)  # 改变a的内部元素后，d的内部元素也被改变，因为d是a的浅拷贝，对内部元素只是引用
# 而不是拷贝对象本身

e = copy.deepcopy(a)  # e为a的深拷贝
a[2][0] = 5666
print(e)  # 深拷贝时，对外围和内部元素都拷贝了对象本身，而不是对象的引用
