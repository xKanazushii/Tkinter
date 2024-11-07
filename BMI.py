from tkinter import *

root = Tk()
root.title("BMI TEST")
root.iconbitmap()
root.geometry("400x500")
root.resizable(0,0)

#frame
titleFrame = LabelFrame(root)
displayFrame = Frame(root)
titleFrame.pack()
displayFrame.pack()

#option
smallFont = ("Arial","35")
infoFont = ("Arial","18")

#function

#label
title = Label(titleFrame,text="วัดค่า BMI",font=smallFont,pady=10,border=0)
title.pack()

#input
firstinfo = Entry(displayFrame,width=10,font=infoFont,bg="white",border=5,justify=RIGHT)
firstinfo.pack()


root.mainloop()