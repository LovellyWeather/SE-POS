from tkinter import *

def addToOrder(Lbox, entry, entry1, entry2, entry3):
    e0 = entry.get()
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    fullLine = ""
    fullLine+=str(e0)
    fullLine+="  "
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
    entry.delete(0,END)
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

##Broken at the moment

def exportOrderToFile(Lbox):
    temp_list = list(CurrentOrder.get(0, END))
    temp_list = [line + '\n' for line in temp_list]
    fout = open("WeeklyOrder.txt", "w")
    fout.writelines(temp_list)
    fout.close()
    CurrentOrder.delete(0, END)

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
lNum = Label(LeftFrame, text="ID")
eNum = Entry(LeftFrame)
lItem = Label(LeftFrame, text="Item")
eItem = Entry(LeftFrame)
lQuantity = Label(LeftFrame, text="Quantity")
eQuantity = Entry(LeftFrame)
lCost = Label(LeftFrame, text="Cost")
eCost = Entry(LeftFrame)
Add = Button(LeftFrame, text="Add", command=lambda: addToOrder(CurrentOrder, eNum, eItem, eQuantity, eCost))

lNum.grid(row=0,column=0)
eNum.grid(row=0,column=1)
lItem.grid(row=1,column=0)
eItem.grid(row=1,column=1)
lQuantity.grid(row=2,column=0)
eQuantity.grid(row=2,column=1)
lCost.grid(row=3,column=0)
eCost.grid(row=3,column=1)
Add.grid(row=4,column=1,pady=10)
