import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Messagebox')
window.geometry('300x300')
var1 = tk.StringVar()
tk.Label(window,
         textvariable=var1).pack()


# 创建点击事件
def press_warning_btn():
    messagebox.showwarning(title='NO',  # 显示警告
                           message='NO')


def press_info_btn():
    messagebox.showinfo(title='Hi',  # 显示信息
                        message='hi')


def press_error_btn():
    messagebox.showerror(title='Hi',  # 显示错误
                         message='ERROR')


def press_question_btn():
    result = messagebox.askquestion(title='Hi',  # 返回string类型的yes or no 给result
                                    message='are you ok')
    var1.set('R U OK? ' + result)


def press_question_btn():
    result = messagebox.askyesno(title='Hi',  # 返回bool给result
                                 message='?')
    if result:
        var1.set('sure')
    else:
        var1.set('Nah')


# 创建button
btn1 = tk.Button(window,
                 text='info',
                 command=press_info_btn)
btn1.pack()

tk.Button(window,
          text='warning',
          command=press_warning_btn).pack()

tk.Button(window,
          text='error',
          command=press_error_btn).pack()

tk.Button(window,
          text='question',
          command=press_question_btn).pack()

tk.Button(window,
          text='Yes or no',
          command=press_question_btn).pack()

window.mainloop()
