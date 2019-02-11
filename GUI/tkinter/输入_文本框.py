import tkinter as tk

window = tk.Tk()

window.title('my window')
window.geometry('200x200')

e = tk.Entry(window,  # 建立输入框
             show=None,  # 输入以*显示
             )
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert', var)  # 在光标处插入


b1 = tk.Button(window,
               text='insert point',
               width=15, height=2,
               command=insert_point)
b1.pack()


def insert_end():
    var = e.get()
    t.insert(1.1, var)  # 在第一行第一列输入
    # t.insert('end',var) 在最末尾输入


b2 = tk.Button(window,
               text='insert end',
               command=insert_end)
b2.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()
