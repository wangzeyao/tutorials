import tkinter as tk
from tkinter import messagebox
import pickle

user_info = {}
try:
    with open('user_info.pickle', 'rb') as user_file:
        user_info = pickle.load(user_file)
except FileNotFoundError:
    with open('user_info.pickle','wb') as user_file:
        user_info['admin'] = 'admin'
        pickle.dump(user_info,user_file)
# try:
#     with open('user_info.pickle', 'rb') as usr_file:
#         user_info = pickle.load(usr_file)
# except FileNotFoundError:
#     with open('user_info.pickle', 'wb') as usr_file:
#         user_info = {'admin': 'admin'}
#         pickle.dump(user_info, usr_file)

window = tk.Tk()
window.title('Welcome')
window.geometry('500x350')

# 定义接收用户名和密码的变量
var_user_name = tk.StringVar()
var_user_name.set('example@python.com')  # 设置默认形式
var_password = tk.StringVar()

# 使用canvas画布加载图片
canvas = tk.Canvas(window,
                   height=200, width=500)

image_file = tk.PhotoImage(file='welcome.gif')  # 读取文件
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# 定义label
tk.Label(window,
         text='User name:').place(x=50, y=150)
tk.Label(window,
         text='Password:').place(x=50, y=190)

# 定义输入框
entry_user_name = tk.Entry(window,
                           textvariable=var_user_name)
entry_user_name.place(x=160, y=150)

entry_password = tk.Entry(window,
                          textvariable=var_password,
                          show='*')
entry_password.place(x=160, y=190)


# 定义登陆和注册函数
def user_login():
    user_name = var_user_name.get()
    user_passward = var_password.get()
    with open('user_info.pickle','rb')as user_file_login:
        user_info_login = pickle.load(user_file_login)
    if user_name in user_info_login:
        if user_passward == user_info[user_name]:
            tk.messagebox.showinfo(message='Welcome! ' + user_name)
        else:
            tk.messagebox.showerror(message='Wrong password')
    else:
        is_sign_up = tk.messagebox.askyesno(message='User not found. Sign up?')
        if is_sign_up:
            user_signup()


def user_signup():
    def sign_up_to_website():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        # try:
        with open('user_info.pickle', 'rb') as user_file:
            exist_usr_info = pickle.load(user_file)
        # except FileNotFoundError:
        #     with open('user_info.pickle', 'wb') as user_file:
        #         user_info = {'admin': 'admin'}
        #         pickle.dump(user_info, user_file)
        # 这里就是判断，如果两次密码输入不一致
        if nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        # 如果用户名已经在我们的数据文件中，则提示`'Error', 'The user has already signed up!'`
        elif np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        else:
            exist_usr_info[nn] = np
            with open('user_info.pickle', 'wb') as user_file:
                pickle.dump(exist_usr_info, user_file)
            with open('user_info.pickle', 'rb') as usr_file:
                info = pickle.load(usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)  # 窗口上的窗口
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up')
    # 建立label
    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name:').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password:').place(x=10, y=50)
    entry_new_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_new_pwd.place(x=150, y=50)
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Password Confirm').place(x=10, y=90)
    entry_new_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_new_pwd_confirm.place(x=150, y=90)

    # 建立注册按钮
    btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_up_to_website)
    btn_confirm_sign_up.place(x=150, y=130)


# 定义login和signup两个按钮
btn_login = tk.Button(window,
                      text='Login',
                      command=user_login)
btn_login.place(x=170, y=230)

btn_signup = tk.Button(window,
                       text='Signup',
                       command=user_signup)
btn_signup.place(x=270, y=230)

window.mainloop()
