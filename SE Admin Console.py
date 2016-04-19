from tkinter import *
import os

def addEmployee(Lbox, entry1):
    e1 = entry1.get()
    Lbox.insert(END, e1)
    eAdd.delete(0, END)

def deleteEmployee(Lbox):
    Lbox.delete(ACTIVE)

def goToFile(inventoryFile):
    os.system(inventoryFile)

def saveEmployees():
    temp_list = list(EmployeeDirectoryList.get(0, END))
    temp_list = [line + '\n' for line in temp_list]
    fout = open("employees.txt", "w")
    fout.writelines(temp_list)
    fout.close()

root = Tk()
root.title("Admin Console")

'''Frames boiii'''
LeftFrame = Frame(root)
LeftFrame.grid(row = 0, column = 0)
RightFrame = Frame(root)
RightFrame.grid(row = 0, column = 1, padx=20, pady=20)
LowerLeftFrame = Frame(root)
LowerLeftFrame.grid(row = 1, column = 0, padx=20, pady=20)

LowerRightFrame = Frame(root)
LowerRightFrame.grid(row = 1, column = 1)

'''Labels'''
Inventory = Label(LeftFrame, text="Inventory")
EmployeeDirectory = Label(RightFrame, text="Employee Directory")

Inventory.pack()
EmployeeDirectory.pack()


'''ListBoxes'''
lScroll = Scrollbar(LeftFrame, orient=VERTICAL)
InventoryList = Listbox(LeftFrame, yscrollcommand=lScroll.set, width=30)
eScroll = Scrollbar(RightFrame, orient=VERTICAL)
EmployeeDirectoryList = Listbox(RightFrame, yscrollcommand=eScroll.set, width=30)

lScroll.pack(side=RIGHT, fill=Y)
InventoryList.pack(fill=BOTH)
eScroll.pack(side=RIGHT, fill=Y)
EmployeeDirectoryList.pack(fill=BOTH)

file = open("posinventory.txt", 'r')
for line in file:
    InventoryList.insert(END, line)
file.close()

file1 = open("employees.txt", 'r')
for line in file1:
    EmployeeDirectoryList.insert(END, line)
file1.close()

'''Buttons'''
CreateOrder = Button(LowerLeftFrame, text="Create Order", command=lambda: goToFile("SE Order.py"))
GetReports = Button(LowerLeftFrame, text="Get Report", command=lambda: goToFile("posinventory.txt"))

CreateOrder.pack(side=RIGHT, pady=5)
GetReports.pack(side=RIGHT, padx=5, pady=5)

Add = Button(LowerRightFrame, text="Add", command=lambda: addEmployee(EmployeeDirectoryList, eAdd))
Remove = Button(LowerRightFrame, text="Remove", command=lambda: deleteEmployee(EmployeeDirectoryList))
eAdd = Entry(LowerRightFrame)
SaveEmployees = Button(LowerRightFrame, text="Save", command=lambda: saveEmployees())

eAdd.pack(side=RIGHT, pady=5)
Add.pack(side=RIGHT, padx=5, pady=5)
Remove.pack(side=RIGHT, pady=5)
SaveEmployees.pack(side=RIGHT, pady=5)
