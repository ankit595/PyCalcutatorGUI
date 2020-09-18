# importing the libraries
from tkinter import *
import math
import tkinter.font as font

# root widget
root = Tk()
root.title("Calculator") # title of the window
root.iconbitmap('C:/Users/ANKIT SAXENA/Desktop/Calculator/Calculator.ico') # icon of the window
root.geometry('380x430')

# label widget
frame_1 = LabelFrame(root)
frame_1.grid(padx=10,pady=10)

# for using bold characters
myFont = font.Font(size=20)


# used to show the input and output
e = Entry(frame_1,width=53,bg="lightcyan",borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

# defining the functio 
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def clear():
    e.delete(0,END)

def add():
    f_no = e.get()
    global f_num
    global do
    do ="Add"
    if f_no is int:
        f_num = int(f_no)
    else:
        f_num = float(f_no)
    e.delete(0,END)

def sub():
    f_no = e.get()
    global f_num
    global do
    do = "Sub"
    if f_no is int:
        f_num = int(f_no)
    else:
        f_num = float(f_no)
    e.delete(0, END)

def mul():
    f_no = e.get()
    global f_num
    global do
    do = "Mul"
    if f_no is int:
        f_num = int(f_no)
    else:
        f_num = float(f_no)
    e.delete(0, END)

def div():
    f_no = e.get()
    global f_num
    global do
    do = "Div"
    if f_no is int:
        f_num = int(f_no)
    else:
        f_num = float(f_no)
    e.delete(0, END)

def equal():
    s_no = e.get()
    e.delete(0,END)
    if do == "sin":
        e.insert(0, math.sin(int(s_no)))
    if do == "cos":
        e.insert(0, math.cos(int(s_no)))
    if do == "tan":
        e.insert(0, math.tan(int(s_no)))
    if do == "Root":
        e.insert(0, math.sqrt(int(s_no)))
    if s_no is int:
        if do =="Add":
            e.insert(0,f_num+int(s_no))
        if do =="Sub":
            e.insert(0,f_num-int(s_no))
        if do =="Mul":
            e.insert(0,f_num*int(s_no))
        if do =="Div":
            e.insert(0,f_num/int(s_no))
    else:
        if do =="Add":
            e.insert(0,f_num+float(s_no))
        if do =="Sub":
            e.insert(0,f_num-float(s_no))
        if do =="Mul":
            e.insert(0,f_num*float(s_no))
        if do =="Div":
            e.insert(0,f_num/float(s_no))


def button_sin():
    global do
    do = "sin"

def button_cos():
    global do
    do = "cos"

def button_tan():
    global do
    do = "tan"

def button_sqrt():
    global do
    do = "Root"
    
# Button widget
button_1 = Button(frame_1,
                  text="1",
                  padx=25,
                  pady=5,
                  bg="aliceblue",
                  command=lambda:button_click(1))
button_1['font'] = myFont

button_2 = Button(frame_1,
                   text="2",
                   padx=25,
                   pady=5,
                   bg="aliceblue",
                   command=lambda:button_click(2))
button_2['font'] = myFont

button_3 = Button(frame_1,
                  text="3",
                  padx=25,
                  pady=5,
                  bg="aliceblue",
                  command=lambda:button_click(3))
button_3['font'] = myFont

button_4 = Button(frame_1,
                  text="4",
                  padx=25,
                  pady=5,
                  bg="aliceblue",
                  command=lambda:button_click(4))
button_4['font'] = myFont

button_5 = Button(frame_1,
                  text="5",
                  padx=25,
                  pady=5,
                  bg="aliceblue",
                  command=lambda:button_click(5))
button_5['font'] = myFont

button_6 = Button(frame_1,
                  text="6",
                  padx=25,
                  pady=5,
                  bg="aliceblue",
                  command=lambda:button_click(6))
button_6['font'] = myFont

button_7 = Button(frame_1,
                  text="7",
                  padx=25,
                  pady=5,
                  bg="aliceblue",
                  command=lambda:button_click(7))
button_7['font'] = myFont

button_8 = Button(frame_1,
                  text="8",
                  padx=25,
                  pady=5,
                  bg="aliceblue",
                  command=lambda:button_click(8))
button_8['font'] = myFont

button_9 = Button(frame_1,
                  text="9",
                  padx=25,
                  pady=5,
                  bg="aliceblue",
                  command=lambda:button_click(9))
button_9['font'] = myFont

button_0 = Button(frame_1,
                  text="0",
                  padx=25,
                  pady=5,
                  bg="aliceblue",
                  command=lambda:button_click(0))
button_0['font'] = myFont

button_dec = Button(frame_1,
                    text=".",
                    padx=27,
                    pady=5,
                    bg="aliceblue",
                    command=lambda:button_click("."))
button_dec['font'] = myFont

button_add = Button(frame_1,
                    text="+",
                    padx=25,
                    pady=5,
                    bg="aliceblue",
                    command=add)
button_add['font'] = myFont

button_sub = Button(frame_1,
                    text="-",
                    padx=27,
                    pady=5,
                    bg="aliceblue",
                    command=sub)
button_sub['font'] = myFont

button_mul = Button(frame_1,
                    text="×",
                    padx=23,
                    pady=5,
                    bg="aliceblue",
                    command=mul)
button_mul['font'] = myFont

button_div = Button(frame_1,
                    text="÷",
                    padx=24,
                    pady=5,
                    bg="aliceblue",
                    command=div)
button_div['font'] = myFont

button_equal = Button(frame_1,
                      text="=",
                      padx=23,
                      pady=5,
                      bg="aliceblue",
                      command=equal)
button_equal['font'] = myFont

button_clear = Button(root,
                      text="Clear",
                      width=49,
                      height=2,
                      bg="aliceblue",
                      command=clear)

button_sin = Button(frame_1,
                    text="sin",
                    padx=15,
                    pady=5,
                    bg="aliceblue",
                    command=button_sin)
button_sin['font'] = myFont

button_cos = Button(frame_1,
                    text="cos",
                    padx=12,
                    pady=5,bg="aliceblue",command=button_cos)
button_cos['font'] = myFont

button_tan = Button(frame_1,
                    text="tan",
                    padx=13,
                    pady=5,
                    bg="aliceblue",
                    command=button_tan)
button_tan['font'] = myFont

button_root = Button(frame_1,
                     text="√",
                     padx=24,
                     pady=5,
                     bg="aliceblue",
                     command=button_sqrt)
button_root['font'] = myFont

# Giving position to button

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_sub.grid(row=4,column=3)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_mul.grid(row=3,column=3)


button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_div.grid(row=2,column=3)

button_dec.grid(row=5,column=0)
button_0.grid(row=5,column=1)
button_add.grid(row=5,column=2)
button_equal.grid(row=5,column=3)

button_sin.grid(row=1,column=0)
button_cos.grid(row=1,column=1)
button_tan.grid(row=1,column=2)
button_root.grid(row=1,column=3)

button_clear.place(x=10,y=380)

# hold the screen
root.mainloop()
