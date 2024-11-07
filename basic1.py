#สร้างหน้าจอ
from tkinter import *

#Section Option RootWindow
root = Tk()
root.title("Calculator")
root.geometry("350x400")
root.resizable(0,0)
root.iconbitmap("icon/cal.ico")
root.config(bg="#212121")

#settings
Opcolor = "#424242"
Numcolor ="#616161"
displayFont = ("Arial",35)
btnFont = ("Arial",19)

#frame
displayFrame  = Frame(root)
buttomFrame = LabelFrame(root)
displayFrame.pack(padx=2,pady=5)
buttomFrame.pack(pady=2)

#function
def shownumber(number):
    display.insert(END,number)
    if "." in display.get():
        btnDecimal.config(state=DISABLED)

def equal():
    if operator=="add":
        result = float(firstNumber) + float(display.get())
    elif operator=="subtract":
        result = float(firstNumber) - float(display.get())
    elif operator=="miltiply":
        result = float(firstNumber) * float(display.get())
    elif operator=="divide":
        if display.get()=="0":
            result = "ERROR"
        else:
            result = float(firstNumber) / float(display.get())
    elif operator=="exponent":
        result = float(firstNumber) ** float(display.get())
    display.delete(0,END)
    display.insert(0,result)


def oparetion(value):
    global firstNumber
    global operator
    print(value)
    operator = value
    firstNumber = display.get()

    #reset state
    btnDecimal.config(state=NORMAL)
    display.delete(0,END)

    #disable operator btn
    btnAdd.config(state=DISABLED)
    btnSubtract.config(state=DISABLED)
    btnMultiply.config(state=DISABLED)
    btnDivide.config(state=DISABLED)
    btnExponent.config(state=DISABLED)
    btnSquare.config(state=DISABLED)
    btnInvert.config(state=DISABLED)



#display Frame >>
display = Entry(displayFrame,width=30,font=displayFont,bg="white",border=5,justify=RIGHT)
display.pack(padx=5,pady=5)

#operator button 13
btnDelete = Button(buttomFrame,text="<",font=btnFont,bg="orange",fg="white")
btnPersen = Button(buttomFrame,text="%",font=btnFont,bg=Opcolor,fg="white")
btnClear = Button(buttomFrame,text="Clear",font=btnFont,bg="orange",fg="white")
btnQuit = Button(buttomFrame,text="Quit",font=btnFont,bg="orange",fg="white",command=root.destroy)
btnInvert = Button(buttomFrame,text="1/x",font=btnFont,bg=Opcolor,fg="white")
btnSquare = Button(buttomFrame,text="x^2",font=btnFont,bg=Opcolor,fg="white")
btnExponent = Button(buttomFrame,text="x^n",font=btnFont,bg=Opcolor,fg="white",command=lambda:oparetion("exponent"))
btnDivide = Button(buttomFrame,text="/",font=btnFont,bg=Opcolor,fg="white",command=lambda:oparetion("divide"))
btnMultiply = Button(buttomFrame,text="*",font=btnFont,bg=Opcolor,fg="white",command=lambda:oparetion("multiply"))
btnSubtract = Button(buttomFrame,text="-",font=btnFont,bg=Opcolor,fg="white",command=lambda:oparetion("subtract"))
btnAdd = Button(buttomFrame,text="+",font=btnFont,bg=Opcolor,fg="white",command=lambda:oparetion("add"))
btnEqual = Button(buttomFrame,text="=",font=btnFont,bg=Opcolor,fg="white",command=equal)
btnDecimal = Button(buttomFrame,text=".",font=btnFont,bg=Opcolor,fg="white",command=lambda:shownumber("."))
btnNegate = Button(buttomFrame,text="+/-",font=btnFont,bg=Opcolor,fg="white")

#number button
btn0 = Button(buttomFrame,text="0",font=btnFont,bg=Numcolor,fg="white",command=lambda:shownumber(0))
btn1 = Button(buttomFrame,text="1",font=btnFont,bg=Numcolor,fg="white",command=lambda:shownumber(1))
btn2 = Button(buttomFrame,text="2",font=btnFont,bg=Numcolor,fg="white",command=lambda:shownumber(2))
btn3 = Button(buttomFrame,text="3",font=btnFont,bg=Numcolor,fg="white",command=lambda:shownumber(3))
btn4 = Button(buttomFrame,text="4",font=btnFont,bg=Numcolor,fg="white",command=lambda:shownumber(4))
btn5 = Button(buttomFrame,text="5",font=btnFont,bg=Numcolor,fg="white",command=lambda:shownumber(5))
btn6 = Button(buttomFrame,text="6",font=btnFont,bg=Numcolor,fg="white",command=lambda:shownumber(6))
btn7 = Button(buttomFrame,text="7",font=btnFont,bg=Numcolor,fg="white",command=lambda:shownumber(7))
btn8 = Button(buttomFrame,text="8",font=btnFont,bg=Numcolor,fg="white",command=lambda:shownumber(8))
btn9 = Button(buttomFrame,text="9",font=btnFont,bg=Numcolor,fg="white",command=lambda:shownumber(9))

#btn row 0
btnPersen.grid(row=0,column=0,padx=1,ipadx=10,sticky="WE")
btnClear.grid(row=0,column=1,padx=1,ipadx=10,sticky="WE")
btnQuit.grid(row=0,column=2,padx=1,ipadx=10,sticky="WE")
btnDelete.grid(row=0,column=3,padx=1,ipadx=10,sticky="WE")

#btn row 1
btnInvert.grid(row=1,column=0,padx=1,ipadx=10,sticky="WE")
btnSquare.grid(row=1,column=1,padx=1,ipadx=10,sticky="WE")
btnExponent.grid(row=1,column=2,padx=1,ipadx=10,sticky="WE")
btnDivide.grid(row=1,column=3,padx=1,ipadx=10,sticky="WE")

#btn row 2
btn7.grid(row=2,column=0,padx=1,ipadx=10,sticky="WE")
btn8.grid(row=2,column=1,padx=1,ipadx=10,sticky="WE")
btn9.grid(row=2,column=2,padx=1,ipadx=10,sticky="WE")
btnMultiply.grid(row=2,column=3,padx=1,ipadx=10,sticky="WE")

#btn row3
btn4.grid(row=3,column=0,padx=1,ipadx=10,sticky="WE")
btn5.grid(row=3,column=1,padx=1,ipadx=10,sticky="WE")
btn6.grid(row=3,column=2,padx=1,ipadx=10,sticky="WE")
btnSubtract.grid(row=3,column=3,padx=1,ipadx=10,sticky="WE")

#btn row4
btn1.grid(row=4,column=0,padx=1,ipadx=10,sticky="WE")
btn2.grid(row=4,column=1,padx=1,ipadx=10,sticky="WE")
btn3.grid(row=4,column=2,padx=1,ipadx=10,sticky="WE")
btnAdd.grid(row=4,column=3,padx=1,ipadx=10,sticky="WE")

#btn row5
btnNegate.grid(row=5,column=0,padx=1,ipadx=10,sticky="WE")
btn0.grid(row=5,column=1,padx=1,ipadx=10,sticky="WE")
btnDecimal.grid(row=5,column=2,padx=1,ipadx=10,sticky="WE")
btnEqual.grid(row=5,column=3,padx=1,ipadx=10,sticky="WE")

root.mainloop()