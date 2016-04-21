from tkinter import *
def LookUp():
    def searchList():
        searchItem=eSearch.get()
        f = open('Inventory.txt', "r")
        for line in f:
            itemList=line.split(" ")
            itemWord=itemList[1].split("-")
            for words in itemWord:
                if searchItem.lower()==words.lower():
                    Inventory.insert(END, itemList[0]+" "+ itemList[1] )
    def AddSale():
        active=Inventory.get(ACTIVE)
        activeList=active.split(" ")
        #Inventory.insert(END,  activeList[1])
        eAddItem.insert(0, activeList[0])

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
    bDone = Button(TopFrame,text="Done")

    bAddToSale.pack(pady=20)
    bDone.pack(side=BOTTOM, pady=20)
