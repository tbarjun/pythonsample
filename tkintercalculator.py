import parser
from tkinter import *
root = Tk()
root.title("Calculator")

display = Entry(root)
display.grid(row=1,columnspan=7)

i=0
def get_variable(num):
    global i
    display.insert(i,num)
    i+=1

def clear_all():
    display.delete(0,END)

def backspace():
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"invalid")

def get_operation(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i+=length

def calculate():
    entire_string=display.get()
    try:
        a=parser.expr(entire_string).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"error")




Button(root,text="1",command=lambda :get_variable(1)).grid(row=2,column=1)
Button(root,text="2",command=lambda :get_variable(2)).grid(row=2,column=2)
Button(root,text="3",command=lambda :get_variable(3)).grid(row=2,column=3)
Button(root,text="4",command=lambda :get_variable(4)).grid(row=3,column=1)
Button(root,text="5",command=lambda :get_variable(5)).grid(row=3,column=2)
Button(root,text="6",command=lambda :get_variable(6)).grid(row=3,column=3)
Button(root,text="7",command=lambda :get_variable(7)).grid(row=4,column=1)
Button(root,text="8",command=lambda :get_variable(8)).grid(row=4,column=2)
Button(root,text="9",command=lambda :get_variable(9)).grid(row=4,column=3)
Button(root,text="0",command=lambda :get_variable(0)).grid(row=5,column=2)
Button(root,text="=",command=lambda :calculate()).grid(row=5,column=3)
Button(root,text="<-",bg="black",fg="white",command=lambda :backspace()).grid(row=5,column=1)
Button(root,text="+",command=lambda :get_operation("+")).grid(row=2,column=4)
Button(root,text="-",command=lambda :get_operation("-")).grid(row=3,column=4)
Button(root,text="*",command=lambda :get_operation("*")).grid(row=4,column=4)
Button(root,text="/",command=lambda :get_operation("/")).grid(row=5,column=4)
Button(root,text="^2",command=lambda :get_operation("**2")).grid(row=2,column=5)
Button(root,text="^x",command=lambda :get_operation("**")).grid(row=3,column=5)
Button(root,text="(",command=lambda :get_operation("(")).grid(row=4,column=5)
Button(root,text=")",command=lambda :get_operation(")")).grid(row=5,column=5)
Button(root,text="!").grid(row=2,column=6)
Button(root,text="pi",command=lambda :get_operation("*3.14")).grid(row=3,column=6)
Button(root,text="%",command=lambda :get_operation("%")).grid(row=4,column=6)
Button(root,text="AC",bg="red",fg="white",command=lambda :clear_all()).grid(row=5,column=6)





root.mainloop()