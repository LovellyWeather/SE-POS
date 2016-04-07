from tkinter import *

root = Tk()

'''Framez boiii'''
LeftFrame = Frame(root)
LeftFrame.pack(side=LEFT)
BottomFrame = Frame(root, pady=20)
BottomFrame.pack(side=BOTTOM)
RightFrame = Frame(root, padx=40, pady=5)
RightFrame.pack(side=RIGHT)

'''Buttonz boiii'''
CreditDebit = Button(LeftFrame, text="Credit/Debit Card", height=3, width = 15)
GiftCard = Button(LeftFrame, text="Gift Card", height=3, width=15)
Cheque = Button(LeftFrame, text="Cheque", height=3, width=15)
Cash = Button(LeftFrame, text="Cash", height=3, width=15)

CreditDebit.grid(row=0, column=0)
GiftCard.grid(row=0, column=1)
Cheque.grid(row=1, column=0)
Cash.grid(row=1, column=1)

'''Entries boiii'''
lCardNumber = Label(RightFrame, text="Enter Credit/Debit Card Number")
lGiftCardCode = Label(RightFrame, text="Enter Gift Card Code")
eCardNumber = Entry(RightFrame)
eGiftCardCode = Entry(RightFrame)

lCardNumber.pack()
eCardNumber.pack()
lGiftCardCode.pack()
eGiftCardCode.pack()

'''Data Displayed boiii'''
lAmountPaid = Label(BottomFrame, text="Amount Paid")
lAmountNeeded = Label(BottomFrame, text="Amount Needed")
lChange = Label(BottomFrame, text="Change")

AmountPaid = Entry(BottomFrame)
AmountNeeded = Entry(BottomFrame)
Change = Entry(BottomFrame)

lAmountPaid.grid(row=0,column=0)
AmountPaid.grid(row=0,column=1)
lAmountNeeded.grid(row=1,column=0)
AmountNeeded.grid(row=1,column=1)
lChange.grid(row=2,column=0)
Change.grid(row=2,column=1)

