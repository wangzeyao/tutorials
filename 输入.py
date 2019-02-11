
# input()函数基本用法
a_input = input('pls input an int ')
print('the int is:', a_input)

# 可以使用在if语句中，但是需先将input定义为一个类型

b_input = int(input('pls input a number: '))
if b_input == 1:
    print('good')
elif b_input == 2:
    print('not bad')
else:
    print('maybe next time')
