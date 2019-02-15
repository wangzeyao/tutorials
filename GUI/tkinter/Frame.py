import tkinter as tk

window = tk.Tk()
window.title('Frame')
window.geometry('300x300')

tk.Label(window, text='on the window').pack()

# 定义在window上的主frm
frm = tk.Frame(window)
frm.pack()

sub_frm1 = tk.Frame(frm)
sub_frmr = tk.Frame(frm)
sub_frm1.pack(side='left')  # 将子frame定义在主frame的左边
sub_frmr.pack(side='right')  # 将右子frame定义在主frame的右边

# 定义在子frame中的label
tk.Label(sub_frm1, text='on the frm 1').pack()
tk.Label(sub_frmr, text='on the frm right').pack()
tk.Label(sub_frm1, text='on the frm 2').pack()

window.mainloop()
