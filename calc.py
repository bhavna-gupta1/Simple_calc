import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Calculator')
root .geometry('340x375')
root.resizable(False,False)
root.configure(bg='#17161b')
# equations

equation = " "

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
def clear():
    global equation
    equation=" "
    label_result.config(text=equation)
def calculate():
    global equation
    result=" "
    if equation !=" ":
       try:
            result = eval(equation)
       except:
           result = " "
           equation=" "
    label_result.config(text=result)


label_result=tk.Label(root,width=25,height=1,text=" ",font=('arial',30))
label_result.pack()
# button in 1st line
Button(root,text='c',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#3697f5',fg='#fff',command=lambda:clear()).place(x=8,y=60)
Button(root,text='/',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('/')).place(x=90,y=60)
Button(root,text='%',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('%')).place(x=172,y=60)
Button(root,text='*',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('*')).place(x=254,y=60)

# button in  2nd line
Button(root,text='7',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('7')).place(x=8,y=123)
Button(root,text='8',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('8')).place(x=90,y=123)
Button(root,text='9',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('9')).place(x=172,y=123)
Button(root,text='-',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('-')).place(x=254,y=123)

# button in  3rd line
Button(root,text='4',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('4')).place(x=8,y=186)
Button(root,text='5',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('5')).place(x=90,y=186)
Button(root,text='6',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('6')).place(x=172,y=186)
Button(root,text='+',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('+')).place(x=254,y=186)

# button in 4th line
Button(root,text='1',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('1')).place(x=8,y=249)
Button(root,text='2',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('2')).place(x=90,y=249)
Button(root,text='3',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('3')).place(x=172,y=249)

# button in  5th line
Button(root,text='0',width=9,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('0')).place(x=8,y=312)
Button(root,text='.',width=4,height=1,pady=1,font=('arial',20,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda:show('.')).place(x=172,y=312)

# = button
Button(root,text='=',width=4,height=3,pady=1,font=('arial',20,'bold'),bd=1,bg='#fe9037',fg='#fff',command=lambda:calculate()).place(x=253,y=249)

root.mainloop()