mydict={}
while True:
    print("1. Insert : \n2. Update :\n3. Delete :\n4. Display :\n5. Exit : ")
    a=int(input("Enter your choice : "))
    if a==1:
        nam=input('Enter your name :')
        num=int(input("Enter your number : "))
        if nam in mydict :
            print('ALREADY EXIST')
        else:    
            mydict[nam]=num        
    elif a==2:
        print("1.Name updation.\n2.Phone Number updation.")
        choice=int(input("Enter your choice : "))
        if choice==1:
            nam=input("Enter your old name :")
            n=input("Enter your new name : ")
            if n not in mydict:
                mydict[n]=mydict.pop(nam)
            else:    
                print("Already Exist")  
        else:
            nam=input("Enter the name : ")
            phone=int(input("Enter your  new phone number : "))
            mydict[nam]=phone
    elif a==3:
        rem=input("Enter the name to remove : ")
        mydict.pop(rem)
    elif a==4:
        print("Details")
        print(mydict.items())
    elif a==5:
        exit()  
