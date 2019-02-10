# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 11:06:21 2019

@author: WANGZEYAO
"""

import tkinter as tk

window = tk.Tk()
window.title('Canvas')
window.geometry('400x400')

###创建canvas

canvas = tk.Canvas(window,
                   bg = 'blue',
                   height = 100,width = 200, #长200像素，宽100像素
                   )
### 读取图片文件
image_file = tk.PhotoImage(file = 'D:/pythonProject/tutorials/files/ins.gif')
image = canvas.create_image(0,0, #定义坐标为0，0
                            anchor='nw', # 确定锚点
                            image = image_file)
### 创建自定义图形
x0,y0,x1,y1 = 50,50,80,80 # 定义坐标,以左上角为原点
line = canvas.create_line(x0,y0,x1,y1) # 画直线
oval = canvas.create_oval(x0,y0,x1,y1,fill='red') # 画圆形
arc = canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=180) #画扇形
rect = canvas.create_rectangle(100,30,100+20,30+20) #画正方形
canvas.pack()

def moveit():
    canvas.move(rect, #选定要移动的元素
                0,2 # 移动的x，y坐标
                )
    
btn = tk.Button(window,
                text = 'move',
                command = moveit)
btn.pack()
window.mainloop()