# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window') #标题
window.geometry('200x100') #窗口长*宽

var = tk.StringVar() #字符串变量
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15,
             height=2) #标签的设计

# 不变的标签
#l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)

l.pack() 

# 可变的标签：点击则显示 "you hit me" ，再点击则无
on_hit = False #全局变量，控制它显示or不显示

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

# Button 点击则执行command=hit_me函数
b = tk.Button(window, text='hit me', width=15,
              height=2, command=hit_me)
b.pack()


window.mainloop() #循环刷新
