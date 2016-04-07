from tkinter import *

root = Tk()

'''Scroll Box'''
LeftFrame = Frame(root)
LeftFrame.pack(side=LEFT, fill=Y)
scroll = Scrollbar(LeftFrame, orient=VERTICAL, )
receipt = Listbox(LeftFrame, yscrollcommand=scroll.set)

scroll.pack(side=RIGHT, fill=Y)
receipt.pack(expand=True)

'''Side Buttons'''
bSearch = Button(text="Search")
bAddCoupon = Button(text="AddCoupon")
bPay = Button(text="Pay")

bSearch.pack(fill=X)
bAddCoupon.pack(fill=X)
bPay.pack(fill=X)

'''Bottom Entries'''
BottomFrame = Frame(root)
BottomFrame.pack(side=BOTTOM)

Weight = Label(BottomFrame, text="Weight")
Quantity = Label(BottomFrame, text="Quantity")
eWeight = Entry(BottomFrame)
eQuantity = Entry(BottomFrame)

TotalCost = Label(BottomFrame, text="Total Cost")
Tax = Label(BottomFrame, text="Tax")
MoneySaved = Label(BottomFrame, text="Money Saved")
FinalSale = Label(BottomFrame, text="Final Sale")
eTotalCost = Entry(BottomFrame)
eTax = Entry(BottomFrame)
eMoneySaved = Entry(BottomFrame)
eFinalSale = Entry(BottomFrame)

Weight.grid(row=0,column=0)
Quantity.grid(row=1,column=0)
eWeight.grid(row=0,column=1)
eQuantity.grid(row=1,column=1)

TotalCost.grid(row=0,column=3)
Tax.grid(row=1, column=3)
MoneySaved.grid(row=3, column=3)
FinalSale.grid(row=4, column=3)
eTotalCost.grid(row=0, column=4)
eTax.grid(row=1, column=4)
eMoneySaved.grid(row=3, column=4)
eFinalSale.grid(row=4, column=4)



root.mainloop()
