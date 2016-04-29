from tkinter import *
#from SE_Register import AddToItems
#import SE_Register
def LookUp():
    def searchList():
        try:
            searchItem=eSearch.get()
            f = open('Inventory.txt', "r")
            for line in f:
                itemList=line.split(" ")
                itemWord=itemList[1].split("-")
                for words in itemWord:
                    if searchItem.lower()==words.lower():
                        Inventory.insert(END, itemList[0]+" "+ itemList[1] )
        except:
            error= Tk()
            Mid = Text(error)
            Mid.insert(INSERT,"Something is wrong with the Inventory.")
            Mid.pack()
##    def CouponSearchList():
##        searchItem=eSearch.get()
##        f = open('Coupons.txt', "r")
##        for line in f:
##            itemList=line.split(" ")
##            itemWord=itemList[1].split("-")
##            for words in itemWord:
##                if searchItem.lower()==words.lower():
##                    Inventory.insert(END, itemList[0]+" "+ itemList[1] )
    def AddSale():
        active=Inventory.get(ACTIVE)
        activeList=active.split(" ")
        eAddToSale.insert(0,  activeList[0])
        fW = open('searchItem.txt','w')
        fW.write(activeList[0]) # python will convert \n to os.linesep
        fW.close()
        #eAddItem.insert(0, activeList[0])
        rt.destroy()
    def destroyWindow():
        rt.destroy()

    rt = Tk()

    '''Frames boiiii'''
    LeftFrame = Frame(rt)
    LeftFrame.pack(side=LEFT)

    TopFrame = Frame(rt)
    TopFrame.pack(side=TOP, fill=X)

    '''Inventory Display boiiii'''
    Scroll = Scrollbar(LeftFrame, orient=VERTICAL)
    scrollH = Scrollbar(LeftFrame, orient=HORIZONTAL, )
    Inventory = Listbox(LeftFrame, yscrollcommand=Scroll.set)

    Scroll.pack(side=RIGHT, fill=Y)
    scrollH.pack(side=BOTTOM, fill=X)
    Inventory.pack()

    '''Search Bar'''
    bSearch = Button(TopFrame, text="Search", command=searchList)
    eSearch = Entry(TopFrame)

    bSearch.pack(side=TOP, pady=5, )
    eSearch.pack(side=TOP)

    '''Buttonszz boiii'''
    bAddToSale = Button(TopFrame,text="Add To Sale", command=AddSale)
    eAddToSale = Entry(TopFrame)
    bDone = Button(TopFrame,text="Done", command=destroyWindow)

    bAddToSale.pack(pady=20)
    eAddToSale.pack(side=TOP)
    bDone.pack(side=BOTTOM, pady=20)
