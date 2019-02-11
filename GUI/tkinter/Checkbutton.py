import tkinter as tk

window = tk.Tk()
window.title('CheckButton')
window.geometry('300x300')

var = tk.StringVar()
label1 = tk.Label(window,
                  bg='yellow',
                  width=20,
                  textvariable=var)

label1.pack()

var2 = tk.IntVar()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):  # 如果选中第一个选项，未选中第二个选项
        var.set('I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1):  # 如果选中第二个选项，未选中第一个选项
        var.set('I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):  # 如果两个选项都未选中
        var.set('I do not love either')
    else:
        var.set('I love both')  # 如果两个选项都选中


var1 = tk.IntVar()
check1 = tk.Checkbutton(window,
                        text='Python',
                        variable=var1, onvalue=1, offvalue=0,  # 选定时是1，不选定时为0，赋值给val1
                        command=print_selection)
check1.pack()

var2 = tk.IntVar()
check2 = tk.Checkbutton(window,
                        text='c++',
                        variable=var2, onvalue=1, offvalue=0,  # 选定时是1，不选定时为0，赋值给val2
                        command=print_selection
                        )
check2.pack()
window.mainloop()
