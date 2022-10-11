import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Calculator')


#Entry
input_box=Entry(root,width=59,borderwidth=5)
input_box.grid(row=0,column=0,columnspan=5,padx=10,pady=20)

#define number buttons
def press(number):
    Ans=input_box.get()
    input_box.delete(0,END)
    input_box.insert(0, str(Ans)+str(number))

#define clear button
def clear():
    input_box.delete(0,END)

#define add button
def add():
    ip1=input_box.get()
    global i1
    global operation
    operation="add"
    i1=int(ip1)
    input_box.delete(0,END)

#define subtract button
def subtract():
    ip1=input_box.get()
    global i1
    global operation
    operation="sub"
    i1=int(ip1)
    input_box.delete(0,END)

#define division button
def division():
    ip1=input_box.get()
    global i1
    global operation
    operation="divide"
    i1=int(ip1)
    input_box.delete(0,END)

#define multiply button
def multiply():
    ip1=input_box.get()
    global i1
    global operation
    operation="multiply"
    i1=int(ip1)
    input_box.delete(0,END)

#define mod button
def mod():
    ip1=input_box.get()
    global i1
    global operation
    operation="mod"
    i1=int(ip1)
    input_box.delete(0,END)

#define equal button
def equal():
    ip2=input_box.get()
    input_box.delete(0,END)
    if operation=="add":
        input_box.insert(0, i1+int(ip2))
    elif operation=="sub":
        input_box.insert(0, i1-int(ip2))
    elif operation=="divide":
        if int(ip2)==0:
            input_box.insert(0, "Undefined")
        else:
            input_box.insert(0, i1/int(ip2))
    elif operation=="mod":
        input_box.insert(0, i1%int(ip2))
    elif operation=="multiply":
        input_box.insert(0, i1*int(ip2))



    
    

#Define & Display butons using grid function
b1=Button(root,text="1",padx=40,pady=20,command=lambda:press(1)).grid(row=3,column=0)
b2=Button(root,text="2",padx=40,pady=20,command=lambda:press(2)).grid(row=3,column=1)
b3=Button(root,text="3",padx=40,pady=20,command=lambda:press(3)).grid(row=3,column=2)
b4=Button(root,text="4",padx=40,pady=20,command=lambda:press(4)).grid(row=2,column=0)
b5=Button(root,text="5",padx=40,pady=20,command=lambda:press(5)).grid(row=2,column=1)
b6=Button(root,text="6",padx=40,pady=20,command=lambda:press(6)).grid(row=2,column=2)
b7=Button(root,text="7",padx=40,pady=20,command=lambda:press(7)).grid(row=1,column=0)
b8=Button(root,text="8",padx=40,pady=20,command=lambda:press(8)).grid(row=1,column=1)
b9=Button(root,text="9",padx=40,pady=20,command=lambda:press(9)).grid(row=1,column=2)
b0=Button(root,text="0",padx=40,pady=20,command=lambda:press(0)).grid(row=4,column=0)


#Operation buttons
b_plus=Button(root,text="+",padx=39,pady=20,command=add).grid(row=2,column=3)
b_subtract=Button(root,text="-",padx=41,pady=20,command=subtract).grid(row=3,column=3)
b_division=Button(root,text="/",padx=40,pady=20,command=division).grid(row=4,column=1)
b_mod=Button(root,text="%",padx=38,pady=20,command=mod).grid(row=4,column=2)
b_mul=Button(root,text="x",padx=40,pady=20,command=multiply).grid(row=4,column=3)
b_clear=Button(root,text="clear",padx=30,pady=20,command=clear).grid(row=1,column=3)
b_dot=Button(root,text=".",padx=40,pady=20,command=DISABLED).grid(row=5,column=0)
b_equal=Button(root,text="=",padx=135,pady=20,command=equal).grid(row=5,column=1,columnspan=3)

root.mainloop()