from tkinter import *
from SE_LookUp import LookUp
#code for receipt number
def updateInventory(itemName,quantity, addSub):
    fh = open("Inventory.txt", 'r')
    nF=open("Side_Inventory.txt", 'w')
    lines = fh.readlines()
    for line in lines:
        lineList=line.split(" ")
        if lineList[0]!="\n":
            if lineList[1]!=str(itemName):
                nF.write(line)
            else:
                if addSub=="sub":
                    lineList[3]=str(round(float(lineList[3])-float(quantity),2))
                else:
                    lineList[3]=str(round(float(lineList[3])+float(quantity),2))
                lineList=" ".join(lineList)
                nF.write(str(lineList))
    fh.close()
    nF.close()
    fh = open("Inventory.txt", 'w')
    nF=open("Side_Inventory.txt", 'r')
    lines = nF.readlines()
    for line in lines:
        fh.write(line)
    fh.close()
    nF.close()
def Remove():
    TAX=0.07
    grab=receipt.get(ACTIVE)
    grabList=grab.split(" ")
    #print(grabList[-2])
    grabCost=float(grabList[-2])
    fS=float(eFinalSale.get())
    tC=float(eTotalCost.get())
    eFinalSale.delete(0, 'end')
    if grabList[0]=="Can_deposit:":
        Dep=float(eDeposit.get())
        eDeposit.delete(0,"end")
        eDeposit.insert(0,round(Dep-grabCost,2))
        fS=round(fS-Dep,2)
        eFinalSale.insert(0, fS)
        fh = open("Sales.txt", 'a')
        fh.write("Removed: "+grab)
        fh.close()
    elif grabList[0]=="Discount":
        monSav=eMoneySaved.get()
        eMoneySaved.delete(0,"end")
        eMoneySaved.insert(0,round(float(monSav)-grabCost,2))
        eFinalSale.insert(0, round(fS+grabCost,2))
        fh = open("Sales.txt", 'a')
        fh.write("Removed: "+grab)
        fh.close()
    else:
        f = open('Inventory.txt', "r")
        for line in f:
            itemList=line.split(" ")
            #itemWord=itemList[1].split("-")
            for words in itemList:
                if grabList[0].lower()==words.lower() :
                    if itemList[4]=="yes":
                        tX=float(eTax.get())
                        tXLoss=round(grabCost*TAX,2)
                        print(tXLoss)
                        eTax.delete(0, 'end')
                        eTax.insert(0, round(tX-tXLoss,2))
                    else:
                        tXLoss=0
        fh = open("Sales.txt", 'a')
        fh.write("Removed: "+grab)
        fh.close()
        tC=float(eTotalCost.get())
        eTotalCost.delete(0, 'end')
        eTotalCost.insert(0, round(tC-grabCost,2))
        eFinalSale.insert(0, round(fS-grabCost-tXLoss,2))
        itemName=grabList[0]
        quantity=grabList[1]
        update=updateInventory(itemName,quantity, "add")
        
    
    
    
    
    deleted=receipt.delete(ACTIVE)
def AddfromSearch():
    eAddItem.delete(0,"end")
    AfS = open('searchItem.txt', "r")
    for line in AfS:
        itemList=line.split(" ")
        itemCode=itemList[0]
    AfS.close()
    eAddItem.insert(0,itemCode)
def AddtoList():
    try:
        CANDEP=0.05
        if eAddItem.get()!="":
            TAX=float(0.07)
            tC=float(eTotalCost.get())
            tX=float(eTax.get())
            mS=float(eMoneySaved.get())
            fS=float(eFinalSale.get())
            itemCode=eAddItem.get()
            f = open('Inventory.txt', "r")
            for line in f:
                itemList=line.split(" ")
                if itemCode==itemList[0]:
                    itemName=itemList[1]
                    itemCost=float(itemList[2])
                    quant=eQuantity.get()
                    weight=eWeight.get()
                    cD=eCans.get()
                    ifTax=itemList[4]
                    canDeposit=itemList[5]
                    cD=eCans.get()
                    Dep=eDeposit.get()
                    #order of errors may cause problems     
                    if quant!="" and weight=="":
                        quant=float(eQuantity.get())
                        if canDeposit=="yes":
                            totDep=round(int(cD)*CANDEP*quant,2)
                            eDeposit.delete(0,"end")
                            eDeposit.insert(0,round(totDep+float(Dep),2))
                            eCans.delete(0,"end")
                            fh = open("Sales.txt", 'a')
                            fh.write("Can deposit "+str(totDep)+" \n")
                            fh.close()
                        Dep=float(eDeposit.get())
                        toCo=tC+round(quant*itemCost,2)
                        receipt.insert(END, itemName + " "+ str(quant)+" $ " + str(quant*itemCost)+" \n")
                        if canDeposit=="yes":
                            receipt.insert(END, "Can_deposit: $ "+str(round(totDep,2))+" \n")
                        Dep=float(eDeposit.get())
                        eTotalCost.delete(0, 'end')
                        eTotalCost.insert(0, toCo)
                        if ifTax=="yes":
                            tX=round(tX+TAX*(round(quant*itemCost,2)),2)
                            eTax.delete(0, 'end')
                            eTax.insert(0,tX)
                        eFinalSale.delete(0, 'end')
                        eFinalSale.insert(0, round(toCo+tX+Dep,2))
                        fh = open("Sales.txt", 'a')
                        fh.write("Item: "+itemName+" quantity: "+str(quant)+" Cost: "+str(toCo)+" \n")
                        fh.close()
                        update=updateInventory(itemName,quant, "sub")
                    elif weight!="" and quant=="":
                        weight=float(eWeight.get())
                        if canDeposit=="yes":
                            totDep=round(int(cD)*CANDEP*weight,2)
                            eDeposit.delete(0,"end")
                            eDeposit.insert(0,round(totDep+float(Dep),2))
                            eCans.delete(0,"end")
                            fh = open("Sales.txt", 'a')
                            fh.write("Can deposit "+str(totDep)+" \n")
                            fh.close()
                        Dep=float(eDeposit.get())
                        receipt.insert(END, itemName + " "+ str(weight)+" $ " + str(round(weight*itemCost,2))+" \n")
                        if canDeposit=="yes":
                            receipt.insert(END, "Can_deposit: $ "+str(round(totDep,2))+" \n")
                        Dep=round(float(eDeposit.get()),2)
                        toCo=tC+round(weight*itemCost,2)
                        eTotalCost.delete(0, 'end')
                        eTotalCost.insert(0, toCo)
                        if ifTax=="yes":
                            tX=tX+round(TAX*(weight*itemCost),2)
                            eTax.delete(0, 'end')
                            eTax.insert(0,tX)
                            tX=round(tX+TAX*(weight*itemCost),2)
                        eFinalSale.delete(0, 'end')
                        eFinalSale.insert(0, round(toCo+tX+Dep,2))
                        fh = open("Sales.txt", 'a')
                        fh.write("Item: "+itemName+" weight: "+str(weight)+" Cost: "+str(toCo))
                        fh.close()
                        update=updateInventory(itemName,weight, "sub")
                        
                    else:
                        error= Tk()
                        Mid = Text(error)
                        Mid.insert(INSERT,"Quantity of items or weight of items not inputed or both inputed.")
                        Mid.pack()
                        return("")
                    break
            f.close()
            #if product not in list
            if itemCode!=itemList[0]:
                error= Tk()
                Mid = Text(error)
                Mid.insert(INSERT,"Incorrect product code.")
                Mid.pack()
                return("")
            eWeight.delete(0, 'end')
            eQuantity.delete(0, 'end')
            eAddItem.delete(0, 'end')
    except:
        error= Tk()
        Mid = Text(error)
        Mid.insert(INSERT,"An input is missing or wrong one placed.")
        Mid.pack()
def OpenSearch():
    
    use=LookUp()

def AddToItems(data):
    eAddItem.insert(0, data)
    
def GotoPay():
    try:
        CurTot=open("CurrentTotal.txt", 'w')
        CurTot.write(eFinalSale.get())
        CurTot.close()
        import SE_Pay
    except:
        error= Tk()
        Mid = Text(error)
        Mid.insert(INSERT,"CurrentTotal.txt or SE_Pay is missing or renamed")
        Mid.pack()
    
def GoToCoupon():
    try:
        grab=receipt.get(ACTIVE)
        grabList=grab.split(" ")
        total=grabList[3]
        number=grabList[1]
        #gCC can be more than letters
        gCC=egiftCardCode.get()
        gCD=egiftCardDiscount.get()
        perDol=gCD.split(" ")
        if perDol[0]=="$":
            disAmount=round(float(perDol[1])*float(grabList[1]),2)
        elif perDol[-1]=="%":
            disAmount=round(round(float(perDol[0])/100,2)*float(grabList[3]),2)
        else:
            error= Tk()
            Mid = Text(error)
            Mid.insert(INSERT,"There needs to be an $ space discount or number space %.")
            Mid.pack()
            return("")
            
        receipt.insert(END, "Discount "+gCC+" on "+grabList[0]+": $ "+str(disAmount)+" \n")
        monSave=float(eMoneySaved.get())
        newDis=round(monSave+disAmount,2)
        eMoneySaved.delete(0, "end")
        eMoneySaved.insert(0, newDis)
        toCo=float(eFinalSale.get())
        eFinalSale.delete(0, 'end')
        eFinalSale.insert(0, round(toCo-disAmount,2))
        egiftCardCode.delete(0,"end")
        egiftCardDiscount.delete(0,"end")
        fh = open("Sales.txt", 'a')
        fh.write("Discount of "+str(disAmount)+" on "+grabList[0]+" \n")
        fh.close()
    except:
        error= Tk()
        Mid = Text(error)
        Mid.insert(INSERT,"An input may be missing or an incorrect item was selected.")
        Mid.pack()
    
def GoToCancel():
    eWeight.delete(0, 'end')
    eQuantity.delete(0, 'end')
    eAddItem.delete(0, 'end')
    eTotalCost.delete(0, 'end')
    eTax.delete(0, 'end')
    eMoneySaved.delete(0, 'end')
    eFinalSale.delete(0, 'end')
    receipt.delete(0,'end')
    eTotalCost.insert(0,0)
    eTax.insert(0,0)
    eMoneySaved.insert(0,0)
    eFinalSale.insert(0,0)
    eDeposit.delete(0,"end")
    eDeposit.insert(0,0)
    fh = open("Sales.txt", 'a')
    fh.write("Sale Canceled"+" \n"+" \n")
    fh.close()
window = Tk()
TOTAL=0
#To be edited to get current
TOTCOST=0
TAX=0
MONSAVE=0
FINALSALE=0
zero=0
DEPOSIT=0
'''Scroll Box'''
LeftFrame = Frame(window)
LeftFrame.pack(side=LEFT, fill=Y)
scrollV = Scrollbar(LeftFrame, orient=VERTICAL, )
scrollH = Scrollbar(LeftFrame, orient=HORIZONTAL, )
receipt = Listbox(LeftFrame, yscrollcommand=scrollV.set)

scrollV.pack(side=RIGHT, fill=Y)
scrollH.pack(side=BOTTOM, fill=X)
receipt.pack(expand=True)

'''Side Buttons'''
bSearch = Button(text="Search", command=OpenSearch)
bAddCoupon = Button(text="Add Coupon", command=GoToCoupon)
bPay = Button(text="Pay", command=GotoPay)
bAdd = Button(text= "Add", command=AddtoList)
bAddSearch = Button(text= "Add from search", command=AddfromSearch)
bRemove = Button(text= "Remove", command=Remove)
bCancel = Button(text= "Cancel", command=GoToCancel)

bSearch.pack(fill=X)
bAddCoupon.pack(fill=X)
bPay.pack(fill=X)
bAdd.pack(fill=X)
bAddSearch.pack(fill=X)
bRemove.pack(fill=X)
bCancel.pack(fill=X)


'''Bottom Entries'''
BottomFrame = Frame(window)
BottomFrame.pack(side=BOTTOM)

Weight = Label(BottomFrame, text="Weight")
Quantity = Label(BottomFrame, text="Quantity")
AddItem = Label(BottomFrame, text="Add Item")
Cans = Label(BottomFrame, text="Number of Cans or Bottles per bundle")
giftCardCode = Label(BottomFrame, text="Gift Card Code")
giftCardDiscount = Label(BottomFrame, text="Gift Card Discount on highlighted per item")
eWeight = Entry(BottomFrame)
eQuantity = Entry(BottomFrame)
eAddItem = Entry(BottomFrame)
eCans = Entry(BottomFrame)
egiftCardCode = Entry(BottomFrame)
egiftCardDiscount = Entry(BottomFrame)

TotalCost = Label(BottomFrame, text="Total Cost")
Tax = Label(BottomFrame, text="Tax")
Deposit = Label(BottomFrame, text="Deposit")
MoneySaved = Label(BottomFrame, text="Money Saved")
FinalSale = Label(BottomFrame, text="Final Sale")
eTotalCost = Entry(BottomFrame)
eTax = Entry(BottomFrame)
eDeposit = Entry(BottomFrame)
eMoneySaved = Entry(BottomFrame)
eFinalSale = Entry(BottomFrame)
eTotalCost.insert(0, TOTCOST)
eTax.insert(0, TAX)
eMoneySaved.insert(0, MONSAVE)
eFinalSale.insert(0, FINALSALE)
eDeposit.insert(0, DEPOSIT)


Weight.grid(row=0,column=0)
Quantity.grid(row=1,column=0)
AddItem.grid(row=2,column=0)
Cans.grid(row=3,column=0)
giftCardCode.grid(row=4,column=0)
giftCardDiscount.grid(row=5,column=0)
eWeight.grid(row=0,column=1)
eQuantity.grid(row=1,column=1)
eAddItem.grid(row=2,column=1)
eCans.grid(row=3,column=1)
egiftCardCode.grid(row=4,column=1)
egiftCardDiscount.grid(row=5,column=1)

TotalCost.grid(row=0,column=3)
Tax.grid(row=1, column=3)
Deposit.grid(row=2, column=3)
MoneySaved.grid(row=3, column=3)
FinalSale.grid(row=4, column=3)
eTotalCost.grid(row=0, column=4)
eTax.grid(row=1, column=4)
eDeposit.grid(row=2, column=4)
eMoneySaved.grid(row=3, column=4)
eFinalSale.grid(row=4, column=4)



window.mainloop()
