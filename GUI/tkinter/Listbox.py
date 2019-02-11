import tkinter as tk

window = tk.Tk()
window.title('Listbox')
window.geometry('300x300')

# 创建一个lable用于显示
var1 = tk.StringVar()
lable = tk.Label(window,
                 bg='yellow',
                 width=9,
                 textvariable=var1)
lable.pack()

# 定义listbox

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))  # 给定初始值

lb = tk.Listbox(window,
                listvariable=var2)
lb.pack()
# 在列表中插入元素
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')


# 创建一个按钮的点击事件
def print_selection():
    value = lb.get(lb.curselection())  # 获得光标当前选定的东西curselection
    var1.set(value)


# 创建按钮
btn = tk.Button(window,
                text='print selection',
                command=print_selection)
btn.pack()

window.mainloop()
