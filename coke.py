due=50

while True:

    taken=int(input("Insert coin :"))


    if taken==10 or taken==25 or taken==5:
        due=due-taken

    else:
        taken=0



    if due>0:
        print("Amount Due :" , due)
    else:
        print("Change Owed :" , -1*(due))
        break





