from tkinter import *

root = Tk()
root.title("Order Form Submission")

'''Frames'''
LeftFrame = Frame(root)
LeftFrame.pack(side=LEFT)
RightFrame = Frame(root)
RightFrame.pack(side=RIGHT,padx=10)

'''Listbox'''
Scroll = Scrollbar(RightFrame, orient=VERTICAL)
CurrentOrder = Listbox(RightFrame, yscrollcommand=Scroll.set)

Scroll.pack(side=RIGHT, fill=Y)
CurrentOrder.pack(fill=Y)

Submit = Button(RightFrame, text="Submit Order")
Submit.pack(side=BOTTOM,pady=10)

'''RightFrame Junk'''
lItem = Label(LeftFrame, text="Item")
eItem = Entry(LeftFrame)
lQuantity = Label(LeftFrame, text="Quantity")
eQuantity = Entry(LeftFrame)
lCost = Label(LeftFrame, text="Cost")
eCost = Entry(LeftFrame)
Add = Button(LeftFrame, text="Add")

lItem.grid(row=0,column=0)
eItem.grid(row=0,column=1)
lQuantity.grid(row=1,column=0)
eQuantity.grid(row=1,column=1)
lCost.grid(row=2,column=0)
eCost.grid(row=2,column=1)
Add.grid(row=3,column=1,pady=10)
