# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:34:36 2021

@author: Administrator
"""

from tkinter import *
from tkinter import messagebox
# def s():
#     # l1['text']='all in '
#     # r.set=(n1.get()+n2.get())
#     i=radiovale.get()
#     messagebox.showinfo('resullt:',d[i])
def nf():
    messagebox.showinfo('open')
def of():
    messagebox.showinfo('open2')
def ab():
    messagebox.showinfo('about')
    
        

w=Tk()

m=Menu()
w['menu']=m
fm=Menu(m,tearoff=0)
m.add_cascade(label='file',m=fm)
fm.add_command(label='open file',command=nf)
fm.add_command(label='open file2',command=nf)
fm.add_separator()
fm.add_command(label='exit',command=w.destroy)
helpmenu=Menu(m)
m.add_cascade(label='help',command=helpmenu)
helpmenu.add_command(label='about',command=ab)





# l5=Label(w,text='choice').pack
# d={0:'紅茶',1:'綠茶'}
# radiovale=IntVar()
# radiovale.set(0)
# for i in range(len(d)):
#     Radiobutton(w,text=d[i],variable=radiovale,value=i).pack()
# Button(w,text='sure',command=s).pack()  

# n1=DoubleVar()
# n2=DoubleVar()
# r=DoubleVar()


w.title('my window')
w.geometry('300x200')
w.maxsize(600,400)

# b=Button(w,text='1',command=showMsg,bg='lightyellow')
# b['fg']='red'
# b.pack()

l1=Label(w,text='1',width=30,bg='lightyellow')
l2=Label(w,text='2',width=30,bg='lightblue')
l3=Label(w,text='3',width=30,bg='lightgray')
l1.pack()
l2.pack()
l3.pack()

# Entry(w,width=10,textvariable=n1).pack(side=LEFT)
# Label(w,width=5,text='+').pack(side=LEFT)
# Entry(w,width=10,textvariable=n2).pack(side=LEFT)
# Button(w,width=5,text='=',command=a).pack(side=LEFT)
# Entry(w,width=10,textvariable=r).pack(side=LEFT)


# w.resizable(False,False)
w.mainloop()
