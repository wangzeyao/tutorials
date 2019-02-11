import tkinter as tk

# window setup
window = tk.Tk()
window.title('Radiobutton')
window.geometry('300x300')

# 创建显示lable
var0 = tk.StringVar()
var1 = tk.StringVar()
lable = tk.Label(window,
                 bg='yellow',
                 width=29,
                 textvariable=var0)
lable.pack()


# 创建一个按钮的点击事件
def print_selection():
    var0.set('you have selected ' + var1.get())


# 创建 radiaobutton
rb1 = tk.Radiobutton(window,
                     text='option A',
                     variable=var1, value='A',  # 当选中时，将var1赋值成A
                     command=print_selection)
rb1.pack()

rb2 = tk.Radiobutton(window,
                     text='option B',
                     variable=var1, value='B',  # 当选中时，将var1赋值成B
                     command=print_selection)
rb2.pack()

rb3 = tk.Radiobutton(window,
                     text='option C',
                     variable=var1, value='C',  # 当选中时，将var1赋值成C
                     command=print_selection)
rb3.pack()

window.mainloop()
