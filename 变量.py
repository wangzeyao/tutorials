a = None


def fun():
    global a  # 声明a为全局变量a
    a = 20


print('before: ', a)
fun()
print('after: ', a)
