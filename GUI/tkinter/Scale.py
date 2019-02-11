import tkinter as tk

window = tk.Tk()
window.title('Scale')
window.geometry('300x300')

var = tk.StringVar()
label1 = tk.Label(window,
                  bg='yellow',
                  width=20,
                  textvariable=var)

label1.pack()


def print_selection(v):
    var.set('you have selected ' + v)


scale = tk.Scale(window,
                 label='try me',  # scale的名字
                 from_=0, to=10,  # 选择的范围
                 orient=tk.HORIZONTAL,  # 选择横向的bar
                 length=200,  # 像素长度为200
                 showvalue=0,
                 tickinterval=2,  # 标签的单位长度
                 resolution=0.01,  # 保留小数的位数
                 command=print_selection  # 会传入一个参数给到print_selection函数
                 )
scale.pack()

window.mainloop()
