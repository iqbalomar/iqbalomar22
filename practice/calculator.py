from tkinter import*
me = Tk()
me.geometry("360x460")
me.title("Calculator")
melabel= Label(me,text="Calculator",font=("Courier New",30,'bold'))
melabel.pack(side=TOP)
textin = StringVar()
operator =""

def clickbut(numbers):
    global operator
    operator=operator+str(numbers)
    textin.set(operator)
def equalbut():
    global operator
    add=str(eval(operator))
    textin.set(add)
    operator=''
def equalbut():
    global operator
    sub=str(eval(operator))
    textin.set(sub)
    operator=''
def equalbut():
    global operator
    mul=str(eval(operator))
    textin.set(mul)
    operator=''
def equalbut():
    global operator
    div=str(eval(operator))
    textin.set(div)
    operator=''
