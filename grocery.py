GroceryList={

}

counter=1

while True:
    try:
        item=input()
    except EOFError:
        break
    if item in GroceryList:
        counter=GroceryList[item]+1
    else:
        counter=1
    GroceryList[item]=counter


SortedList=sorted(GroceryList)


for itm in SortedList:
    print(GroceryList[itm] , itm.upper())