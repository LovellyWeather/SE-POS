from tkinter import *
from SE_LookUp import LookUp

#import SE_LookUp
#Note create cancel button to reset register
#code for receipt number
def AddtoList():
    #receipt.insert(END, tC)
    
    #invFile=open("inventory.txt", "r")
    if eAddItem.get()!="":
        TAX=float(0.07)
        tC=float(eTotalCost.get())
        tX=float(eTax.get())
        mS=float(eMoneySaved.get())
        fS=float(eFinalSale.get())
        itemCode=eAddItem.get()
        f = open('Inventory.txt', "r")
        #line = f.readline()
        #itemList=line.split(" ")
        for line in f:
            #line = f.readline()
            itemList=line.split(" ")
            if itemCode==itemList[0]:
                itemName=itemList[1]
                itemCost=float(itemList[2])
                quant=eQuantity.get()
                weight=eWeight.get()
                ifTax=itemList[4]
                canDeposit=itemList[5]
                if quant!="" and weight=="":
                    quant=float(eQuantity.get())
                    receipt.insert(END, itemName + " "+ str(quant)+" $" + str(quant*itemCost))
                    eTotalCost.delete(0, 'end')
                    eTotalCost.insert(0, tC+(quant*itemCost))
                    if ifTax=="yes":
                        eTax.delete(0, 'end')
                        eTax.insert(0,round(tX+TAX*round((quant*itemCost)),2))
                    eFinalSale.delete(0, 'end')
                    eFinalSale.insert(0, toCo+tX)
                elif weight!="" and quant=="":
                    weight=float(eWeight.get())
                    receipt.insert(END, itemName + " "+ str(weight)+" $" + str(round(weight*itemCost,2)))
                    toCo=tC+round(weight*itemCost,2)
                    eTotalCost.delete(0, 'end')
                    eTotalCost.insert(0, toCo)
                    if ifTax=="yes":
                        eTax.delete(0, 'end')
                        eTax.insert(0,tX+round(TAX*(weight*itemCost),2))
                        tX=round(tX+TAX*(weight*itemCost),2)
                    eFinalSale.delete(0, 'end')
                    eFinalSale.insert(0, toCo+tX)
                else:
                    error= Tk()
                    Mid = Text(error)
                    Mid.insert(INSERT,"Quantity of items or weight of items not inputed.")
                    Mid.pack()
                    break
                break
            #line = f.readline()
            #itemList=line.split(" ")
        f.close()
        if itemCode!=itemList[0]:
            error= Tk()
            Mid = Text(error)
            Mid.insert(INSERT,"Incorrect product code.")
            Mid.pack()
            
        
        
        
        eWeight.delete(0, 'end')
        eQuantity.delete(0, 'end')
        eAddItem.delete(0, 'end')
    
def OpenSearch():
    
    use=LookUp()
    print(use)
    if use!=None:
        eAddItem.insert(0, activeList[0])
        print(use)
    
def GotoPay():
    import SE_Pay
def GoToCoupon():
    import SE_LookUp
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
window = Tk()
TOTAL=0
#To be edited to get current
TOTCOST=str(0)
TAX=str(0)
MONSAVE=str(0)
FINALSALE=str(0)
zero=0
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
bCancel = Button(text= "Cancel", command=GoToCancel)

bSearch.pack(fill=X)
bAddCoupon.pack(fill=X)
bPay.pack(fill=X)
bAdd.pack(fill=X)
bCancel.pack(fill=X)


'''Bottom Entries'''
BottomFrame = Frame(window)
BottomFrame.pack(side=BOTTOM)

Weight = Label(BottomFrame, text="Weight")
Quantity = Label(BottomFrame, text="Quantity")
AddItem = Label(BottomFrame, text="Add Item")
eWeight = Entry(BottomFrame)
eQuantity = Entry(BottomFrame)
eAddItem = Entry(BottomFrame)

TotalCost = Label(BottomFrame, text="Total Cost")
Tax = Label(BottomFrame, text="Tax")
MoneySaved = Label(BottomFrame, text="Money Saved")
FinalSale = Label(BottomFrame, text="Final Sale")
eTotalCost = Entry(BottomFrame)
eTax = Entry(BottomFrame)
eMoneySaved = Entry(BottomFrame)
eFinalSale = Entry(BottomFrame)
eTotalCost.insert(0, TOTCOST)
eTax.insert(0, TAX)
eMoneySaved.insert(0, MONSAVE)
eFinalSale.insert(0, FINALSALE)

Weight.grid(row=0,column=0)
Quantity.grid(row=1,column=0)
AddItem.grid(row=2,column=0)
eWeight.grid(row=0,column=1)
eQuantity.grid(row=1,column=1)
eAddItem.grid(row=2,column=1)

TotalCost.grid(row=0,column=3)
Tax.grid(row=1, column=3)
MoneySaved.grid(row=3, column=3)
FinalSale.grid(row=4, column=3)
eTotalCost.grid(row=0, column=4)
eTax.grid(row=1, column=4)
eMoneySaved.grid(row=3, column=4)
eFinalSale.grid(row=4, column=4)



window.mainloop()
