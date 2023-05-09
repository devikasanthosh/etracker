etracker={}
intial=1000
while True:
    print("1.Add Expenteture :\n2.Add Balance :\n3.View Expendeture :\n4.Exit : ")
    choice=int(input("Enter your choice : "))
    if  choice==1:
        num=input("Enter your expendeture : ")
        amt=int(input("Enter the cost : "))
        if amt<=intial:
            intial=intial-amt
            if num  not in etracker:
                etracker[num]=amt
            else:
                etracker[num]=etracker[num]+amt
        else:
            print("*****INSUFFICIENT BALANCE******")           
                
    if choice==2:
        credit=int(input("Amount to be credited : "))
        intial=intial+credit
        print("The total amount : ",intial)        
    if choice==3:
        print(etracker.items())
        if intial>0:
            print("printBALANCE :",intial)  
        
    if choice==4:
        exit()    
