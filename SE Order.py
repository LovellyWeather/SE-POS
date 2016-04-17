from tkinter import *

def addToOrder(Lbox, entry1, entry2, entry3):
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    fullLine = ""
    fullLine+=str(e1)
    fullLine+="  "
    fullLine+=str(e2)
    fullLine+="  "
    fullLine+=str(e3)
    fullLine+="  "
    CurrentOrder.insert(END, str(fullLine))
    orderfile = open("WeeklyOrder.txt", 'a')
    orderfile.write(fullLine)
    orderfile.close()
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

##Broken at the moment

def exportOrderToFile(Lbox):
    '''
    orderfile = open("WeeklyOrder.txt", 'w')
    busString = ""
    busString += Lbox.get(0,END)
    orderfile.append(busString)
    orderfile.close()
    '''
    Lbox.delete(0,END)

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

Submit = Button(RightFrame, text="Submit Order", command=lambda: exportOrderToFile(CurrentOrder))
Submit.pack(side=BOTTOM,pady=10)

'''RightFrame Junk'''
lItem = Label(LeftFrame, text="Item")
eItem = Entry(LeftFrame)
lQuantity = Label(LeftFrame, text="Quantity")
eQuantity = Entry(LeftFrame)
lCost = Label(LeftFrame, text="Cost")
eCost = Entry(LeftFrame)
Add = Button(LeftFrame, text="Add", command=lambda: addToOrder(CurrentOrder, eItem, eQuantity, eCost))

lItem.grid(row=0,column=0)
eItem.grid(row=0,column=1)
lQuantity.grid(row=1,column=0)
eQuantity.grid(row=1,column=1)
lCost.grid(row=2,column=0)
eCost.grid(row=2,column=1)
Add.grid(row=3,column=1,pady=10)
