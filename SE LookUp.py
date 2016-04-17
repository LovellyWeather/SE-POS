from tkinter import *

root = Tk()
root.title("Item Search")

'''Frames boiiii'''
LeftFrame = Frame(root)
LeftFrame.pack(side=LEFT)

TopFrame = Frame(root)
TopFrame.pack(side=TOP, fill=X)

'''Inventory Display boiiii'''
Scroll = Scrollbar(LeftFrame, orient=VERTICAL)
Inventory = Listbox(LeftFrame, yscrollcommand=Scroll.set)

Scroll.pack(side=RIGHT, fill=Y)
Inventory.pack()

'''Search Bar'''
Search = Label(TopFrame, text="Search")
eSearch = Entry(TopFrame)

Search.pack(side=TOP, pady=5, )
eSearch.pack(side=TOP)

'''Buttonszz boiii'''
AddToSale = Button(text="Add To Sale")
Done = Button(text="Done")

AddToSale.pack(pady=20)
Done.pack(side=BOTTOM, pady=20)
