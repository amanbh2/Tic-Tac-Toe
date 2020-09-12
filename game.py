from tkinter import *
import tkinter.font as font

root =Tk()
root.title("TIC TAC TOE")
#root.geometry("400x400")
root['bg']="#242423"

myfont=font.Font(name="Calibri",size=20)
global m,a1,a2,a3,box
m=0
box=0
a1=2
a2=3
a3=4
b1=5
b2=6
b3=7
c1=8
c2=9
c3=10

def check():
    if (a1==a2 and a2==a3) or (b1==b2 and b2==b3) or (c1==c2 and c2==c3) or (a1==b1 and b1==c1) or (a2==b2 and b2==c2) or (a3==b3 and b3==c3) or (a1==b2 and b2==c3) or (a3==b2 and b2==c1)or box==9:
        a2_btn.configure(state="disabled")
        a1_btn.configure(state="disabled")
        a3_btn.configure(state="disabled")
        b1_btn.configure(state="disabled")
        b2_btn.configure(state="disabled")
        b3_btn.configure(state="disabled")
        c1_btn.configure(state="disabled")
        c2_btn.configure(state="disabled")
        c3_btn.configure(state="disabled")
        global footer1, footer2
        footer1.configure(text="Game Over")
        if box==9:
            footer2.configure(text="Try Again")
        else:
            if m==1:
                footer2.configure(text="♥ Won")
            if m==0:
                footer2.configure(text="✖ Won")
    

def btn_click_a1():
    global m,a1,box
    if m==0:
        a1_btn.configure(text="♥",state="disabled", disabledforeground="#d90429")
        m=1
        a1=0
    else:
        a1_btn.configure(text="✖",state="disabled", disabledforeground="#001f3d")
        m=0
        a1=1
    box=box+1
    check()
def btn_click_a2():
    global m,a2,box
    if m==0:
        a2_btn.configure(text="♥",state="disabled", disabledforeground="#d90429")
        m=1
        a2=0
    else:
        a2_btn.configure(text="✖",state="disabled", disabledforeground="#001f3d")
        m=0
        a2=1
    box=box+1
    check()
def btn_click_a3():
    global m,a3,box
    if m==0:
        a3_btn.configure(text="♥",state="disabled", disabledforeground="#d90429")
        m=1
        a3=0
    else:
        a3_btn.configure(text="✖",state="disabled", disabledforeground="#001f3d")
        m=0
        a3=1
    box=box+1
    check()
def btn_click_b1():
    global m,b1,box
    if m==0:
        b1_btn.configure(text="♥",state="disabled", disabledforeground="#d90429")
        m=1
        b1=0
    else:
        b1_btn.configure(text="✖",state="disabled", disabledforeground="#001f3d")
        m=0
        b1=1
    box=box+1
    check()
def btn_click_b2():
    global m,b2,box
    if m==0:
        b2_btn.configure(text="♥",state="disabled", disabledforeground="#d90429")
        m=1
        b2=0
    else:
        b2_btn.configure(text="✖",state="disabled", disabledforeground="#001f3d")
        m=0
        b2=1
    box=box+1
    check()
def btn_click_b3():
    global m,b3,box
    if m==0:
        b3_btn.configure(text="♥",state="disabled", disabledforeground="#d90429")
        m=1
        b3=0
    else:
        b3_btn.configure(text="✖",state="disabled", disabledforeground="#001f3d")
        m=0
        b3=1
    box=box+1
    check()
def btn_click_c1():
    global m,c1,box
    if m==0:
        c1_btn.configure(text="♥",state="disabled", disabledforeground="#d90429")
        m=1
        c1=0
    else:
        c1_btn.configure(text="✖",state="disabled", disabledforeground="#001f3d")
        m=0
        c1=1
    box=box+1
    check()
def btn_click_c2():
    global m,c2,box
    if m==0:
        c2_btn.configure(text="♥",state="disabled", disabledforeground="#d90429")
        m=1
        c2=0
    else:
        c2_btn.configure(text="✖",state="disabled", disabledforeground="#001f3d")
        m=0
        c2=1
    box=box+1
    check()
def btn_click_c3():
    global m,c3,box
    if m==0:
        c3_btn.configure(text="♥",state="disabled", disabledforeground="#d90429")
        m=1
        c3=0
    else:
        c3_btn.configure(text="✖",state="disabled", disabledforeground="#001f3d")
        m=0
        c3=1
    box=box+1
    check()


a1_btn=Button(root, width=10,height=5,bg="#f5cb5c",font=myfont, command=btn_click_a1)
a1_btn.grid(row=0,column=0)

a2_btn=Button(root, width=10,height=5,bg="#f5cb5c",font=myfont,  command=btn_click_a2)
a2_btn.grid(row=0,column=1)

a3_btn=Button(root, width=10,height=5,bg="#f5cb5c",font=myfont,  command=btn_click_a3)
a3_btn.grid(row=0,column=2)

b1_btn=Button(root, width=10,height=5,bg="#f5cb5c",font=myfont,  command=btn_click_b1)
b1_btn.grid(row=1,column=0)

b2_btn=Button(root, width=10,height=5,bg="#f5cb5c",font=myfont,  command=btn_click_b2)
b2_btn.grid(row=1,column=1)

b3_btn=Button(root, width=10,height=5,bg="#f5cb5c",font=myfont,  command=btn_click_b3)
b3_btn.grid(row=1,column=2)

c1_btn=Button(root, width=10,height=5,bg="#f5cb5c",font=myfont,  command=btn_click_c1)
c1_btn.grid(row=2,column=0)

c2_btn=Button(root, width=10,height=5,bg="#f5cb5c",font=myfont,  command=btn_click_c2)
c2_btn.grid(row=2,column=1)

c3_btn=Button(root, width=10,height=5,bg="#f5cb5c",font=myfont,  command=btn_click_c3)
c3_btn.grid(row=2,column=2)

def new_game():
    global a1,a2,a3,b1,b2,b3,c1,c2,c3,m,footer1,footer2,box
    a1_btn.configure(text="",state="normal")
    a2_btn.configure(text="",state="normal")
    a3_btn.configure(text="",state="normal")
    b1_btn.configure(text="",state="normal")
    b2_btn.configure(text="",state="normal")
    b3_btn.configure(text="",state="normal")
    c1_btn.configure(text="",state="normal")
    c2_btn.configure(text="",state="normal")
    c3_btn.configure(text="",state="normal")
    m=0
    box=0
    a1=2
    a2=3
    a3=4
    b1=5
    b2=6
    b3=7
    c1=8
    c2=9
    c3=10
    footer1.configure(text="")
    footer2.configure(text="")


new=Button(root, text="New Game", font=myfont,fg="#f5cb5c",bg="#242423",bd=0,command=new_game)
new.grid(row=3,column=1)
global footer1,footer2
footer1 = Label(root, text="", font=myfont, bg='#242423',fg='#f5cb5c')
footer1.grid(row=3,column=0)
footer2 = Label(root, text="", font=myfont, bg='#242423',fg='#f5cb5c')
footer2.grid(row=3,column=2)
footer3 = Label(root, text="© Aman Bhaskar", bg='#242423',fg='#f5cb5c')
footer3.grid(row=4,columnspan=3)


root.mainloop()