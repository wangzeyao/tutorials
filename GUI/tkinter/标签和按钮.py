# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 16:01:24 2019

@author: WANGZEYAO
"""
import tkinter as tk

### 窗口主体框架
window = tk.Tk() # 首先定义一个window 
window.title('my window') # 然后定义window的一些属性
window.geometry('200x100')




### 窗口内容
lable_1 = tk.Label(window,
                   text='my lable',# 标签的文字
                   bg='green', #背景颜色
                   font=('Arial',12), #字体和字体大小
                   width=15,height=2 #标签的长宽
                   )
lable_1.pack() #固定窗口位置


var=tk.StringVar() #创建一个文字变量存储器
l = tk.Label(window,
             textvariable=var, #使用textvariable替换text，这样可以使文本内容变化
             bg='green',
             font=('Arial',12),
             width=15,height=2)
l.pack()


on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me') #点击后改变文字内容
    else:
        on_hit = False
        var.set('')
### 增加按钮
button_1 = tk.Button(window,
                     text = 'click me',
                     width=15,height=2,
                     command=hit_me)
button_1.pack()





window.mainloop() # 最后执行mainloop启动窗口