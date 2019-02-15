import tkinter as tk

window = tk.Tk()
window.title('pack_grid_place')
window.geometry('300x300')

# tk.Label(window, text=1).pack(side='top')  # 创建label并放置到上方
# tk.Label(window, text=1).pack(side='bottom')
# tk.Label(window, text=1).pack(side='left')
# tk.Label(window, text=1).pack(side='right')

# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)  # 使用grid，按行列来控制,padx控制每个grid的面积

tk.Label(window, text=1).place(x=10, y=100, anchor='sw')  # 以像素为单位放在(10,100),anchor锚点

window.mainloop()