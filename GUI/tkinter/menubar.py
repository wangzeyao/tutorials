import tkinter as tk

# window setup

window = tk.Tk()
window.title('Menu bar')
window.geometry('300x300')

var1 = tk.StringVar()
# 定义label
label = tk.Label(window,
                 textvariable=var1,
                 bg='yellow')
label.pack()
# 定义命令
counter = 0


def do_job():
    global counter
    var1.set('do ' + str(counter))
    counter += 1


# 定义menu bar
menu_bar = tk.Menu(window)

# 定义file menu
file_menu = tk.Menu(menu_bar,
                    tearoff=0  # 能否被分开
                    )
file_menu.add_command(label='New',
                      command=do_job)
file_menu.add_command(label='Open',
                      command=do_job)
file_menu.add_separator()  # 加入分离的一条线
file_menu.add_command(label='Exit',
                      command=window.destroy)
# 将file menu加入 menubar中
menu_bar.add_cascade(label='file',
                     menu=file_menu  # 将filemenu加入menubar
                     )
# 创建sub menu
sub_menu = tk.Menu(file_menu,
                   tearoff=0)
file_menu.add_cascade(label='Import',
                      menu=sub_menu,
                      underline=0)
sub_menu.add_command(label='import image',
                     command=do_job)

# 将menu bar 加到window中。把这个window的menu变成我们定义的menubar
window.config(menu=menu_bar)

window.mainloop()
