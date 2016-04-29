from tkinter import *
def cashPaid():
    try:
        cP=float(eGiftCardAmount.get())
        APaid=float(AmountPaid.get())
        amNe=float(AmountNeeded.get())
        AmountPaid.delete(0, 'end')
        eGiftCardAmount.delete(0, 'end')
        AmountPaid.insert(0,round(cP+APaid,2))
        AmountNeeded.delete(0, 'end')
        AmountNeeded.insert(0,amNe-cP)

        if float(AmountNeeded.get())<=int(0):
            Change.insert(0,int(-1)*float(AmountNeeded.get()))
    except:
        error= Tk()
        Mid = Text(error)
        Mid.insert(INSERT,"Incorrect input into Cash amount.")
        Mid.pack()
def addCard():
    try:
        amNe=float(AmountNeeded.get())
        cardCode=int(eCardNumber.get())
        cardAmount=float(eCardAmount.get())
        eCardNumber.delete(0, 'end')
        eCardAmount.delete(0, 'end')
        APaid=float(AmountPaid.get())
        AmountPaid.delete(0, 'end')
        AmountPaid.insert(0,cardAmount+APaid)
        AmountNeeded.delete(0, 'end')
        AmountNeeded.insert(0,amNe-cardAmount)
        
        if float(AmountNeeded.get())<=int(0):
            Change.insert(0,int(-1)*float(AmountNeeded.get()))
        
        fh = open("Sales.txt", 'a')
        fh.write("Credit_or_Debit_Card_number: "+str(cardCode)+" Amount: "+str(cardAmount)+"\n")
        fh.close()
                            
    except:
        error= Tk()
        Mid = Text(error)
        Mid.insert(INSERT,"Incorrect input into debit/credit card code or amount.")
        Mid.pack()
def finishSale():
    root.destroy()
def cancelSale():
    fh = open("Sales.txt", 'a')
    fh.write("Sale Canceled"+" \n"+" \n")
    fh.close()
    root.destroy()
    
def addGift():

    try:
        amNe=float(AmountNeeded.get())
        cardCode=int(eGiftCardCode.get())
        cardAmount=float(eGiftCardAmount.get())
        fh = open("Gift_Cards.txt", 'r')
        for line in fh:
            GiftList=line.split(" ")
            if GiftList[0]!="\n":
                if int(GiftList[1])==cardCode:
                    newGift=float(GiftList[3])-cardAmount
                    if amNe<cardAmount:
                            cardAmount=amNe
                            newGift=float(GiftList[3])-cardAmount
                    if newGift<0:
                        error= Tk()
                        Mid = Text(error)
                        Mid.insert(INSERT,"Not enough on card for ammount needed. Rest of balance on card will be taken out. ")
                        Mid.pack()
                        cardAmount=float(GiftList[3])
                        
                    
                    
        #fh.write(str(cardCode)+" "+str(cardAmount)+"\n")
        fh.close()
        fh = open("Sales.txt", 'a')
        fh.write("Gift_Card_number: "+str(cardCode)+" Amount:$ "+str(cardAmount)+" \n")
        fh.close()
        eGiftCardCode.delete(0, 'end')
        eGiftCardAmount.delete(0, 'end')
        fh = open("Gift_Cards.txt", 'r')
        nF=open("Side_Gift_Cards.txt", 'w')
        lines = fh.readlines()
        for line in lines:
            lineList=line.split(" ")
            print(lineList)
            if lineList[0]!="\n":
                if lineList[1]!=str(cardCode):
                    nF.write(line)
        if newGift>0:
            nF.write("Gift_Card_number: "+str(cardCode)+" Amount:$ "+str(newGift)+" \n")  
        fh.close()
        nF.close()
        fh = open("Gift_Cards.txt", 'w')
        nF=open("Side_Gift_Cards.txt", 'r')
        lines = nF.readlines()
        for line in lines:
            fh.write(line)
        fh.close()
        nF.close()

        APaid=float(AmountPaid.get())
        AmountPaid.delete(0, 'end')
        AmountPaid.insert(0,cardAmount+APaid)
        AmountNeeded.delete(0, 'end')
        AmountNeeded.insert(0,amNe-cardAmount)
        
        if float(AmountNeeded.get())<=int(0):
            Change.insert(0,int(-1)*float(AmountNeeded.get()))
        
    except:
        error= Tk()
        Mid = Text(error)
        Mid.insert(INSERT,"Incorrect input into code or amount. Card may have no balance.")
        Mid.pack()

def addNewGift():
    try:
        cardCode=int(eGiftCardCode.get())
        cardAmount=float(eGiftCardAmount.get())
        amNe=float(AmountNeeded.get())
        fh = open("Gift_Cards.txt", 'a')
        fh.write("Gift_Card_number: "+str(cardCode)+" Amount:$ "+str(cardAmount)+" \n")
        fh.close()
        eGiftCardCode.delete(0, 'end')
        eGiftCardAmount.delete(0, 'end')
        AmountNeeded.delete(0, 'end')
        AmountNeeded.insert(0,amNe+cardAmount)
    except:
        error= Tk()
        Mid = Text(error)
        Mid.insert(INSERT,"Incorrect input into code or amount.")
        Mid.pack()
    
    
root = Tk()

'''Framez boiii'''
LeftFrame = Frame(root)
LeftFrame.pack(side=LEFT)
BottomFrame = Frame(root, pady=20)
BottomFrame.pack(side=BOTTOM)
RightFrame = Frame(root, padx=40, pady=5)
RightFrame.pack(side=RIGHT)

'''Buttonz boiii'''
CreditDebit = Button(LeftFrame, text="Credit/Debit Card", height=3, width = 15, command = addCard)
GiftCard = Button(LeftFrame, text="Gift Card", height=3, width=15,command = addGift)
NewGiftCard = Button(LeftFrame, text="Add New Gift Card", height=3, width=15,command = addNewGift)
Cash = Button(LeftFrame, text="Cash", height=3, width=15, command = cashPaid)
Done = Button(LeftFrame, text="Done", height=3, width=15, command = finishSale)
Cancel = Button(LeftFrame, text="Cancel", height=3, width=15, command = cancelSale)

CreditDebit.grid(row=0, column=0)
GiftCard.grid(row=0, column=1)
NewGiftCard.grid(row=1, column=0)
Cash.grid(row=1, column=1)
Done.grid(row=2, column=0)
Cancel.grid(row=2, column=1)

'''Entries boiii'''
lCardNumber = Label(RightFrame, text="Enter Credit/Debit Card Number")
lCardAmount = Label(RightFrame, text="Enter Credit/Debit Card Amount")
lGiftCardCode = Label(RightFrame, text="Enter Gift Card Code")
lGiftCardAmount = Label(RightFrame, text="Enter Gift Card or Cash amount")
eCardNumber = Entry(RightFrame)
eCardAmount = Entry(RightFrame)
eGiftCardCode = Entry(RightFrame)
eGiftCardAmount = Entry(RightFrame)


lCardNumber.pack()
eCardNumber.pack()
lCardAmount.pack()
eCardAmount.pack()
lGiftCardCode.pack()
eGiftCardCode.pack()
lGiftCardAmount.pack()
eGiftCardAmount.pack()

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

cT=open("CurrentTotal.txt","r")
CurTot=cT.readline()
AmountNeeded.insert(0,CurTot)
AmountPaid.insert(0,"0")
cT.close()
open("CurrentTotal.txt", 'w').close()
                            


