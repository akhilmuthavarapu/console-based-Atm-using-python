#account creation:
print("Welcome to the Codegnan Bank  ")
print("⭐"*40)
n=int(input("No of Customers: "))
l=[]
acc=1001
for i in range(1,n+1):
    print(f"Account Number: {acc}")
    name=input(f"Enter Customer {i} name : ")
    dob=input(f"Enter Customer {i} dob[dd-mm-yy]: ")   
    try:
        bal=float(input(f"enter the customer {i} balance:"))
        
    except:
        print("\"MINIMUM BALANCE IS REQUIRED TO OPEN A BANK ACCOUNT\"")
        bal=float(input(f"Enter the customer {i} balance:"))
    
    try:
        pin=int(input(f"Enter Customer {i} pin:"))
    except:
        pin=None
    l.append([name,dob,bal,pin])
    print(f"-----Customer {i} Details Saved Successfully -----")
    print("⭐"*40)
    acc+=1
accounts={}
acc=1001
for i in l:
    accounts[acc]=i
    acc+=1
#operations
while True:
    print("⭐"*40)
    print("Welcome to the Atm :")
    print("1. WITHDRAW")
    print("2. DEPOSIT")
    print("3. PIN GENERATION / RESET PIN")
    print("4. MINI STATEMENT")
    print("5. EXIT")
    print("⭐"*40)
    ch=int(input("Enter Your Choice:"))
    if ch!=5 and ch<5:
        ano=int(input("Enter the Account No [like 1001]:"))
        if ano not in accounts:
            print("\"Invalid Account Number \"")
            print("⭐"*40)
            continue
    if ch==1:
        if ano not in accounts:
            print("Invalid Account Number:")
        else:
            print("Dear Customer!! Here is your With Draw Window")
            try:
                pin=int(input("Enter the pin :"))
            except:
                agree=input("your account has NO PIN so we are redirecting you to the pin generation: Do you agree [yes(y)/no(n)]: ")
                if agree.lower()in ["yes","y"]:
                    print("you are redirecting to main page........")
                    continue
                else:
                    print("you are disagreed so we can't provide this account details.....back to main page")
                    continue
            if accounts[ano][-1]==None:
                print("Your pin is not generated go for pin generation")
            elif accounts[ano][-1]!=pin:
                print("Invalid Pin !!")
            else:
                amt=float(input("Enter your amount:"))
                if amt<=accounts[ano][-2]:
                    print(" ---- Withdraw Successful !!!! ----")
                    accounts[ano][-2]-=amt
                    print("Current Balance: ",accounts[ano][-2])
                else:
                    print("\"Insufficient Funds Sir\"")
        print("..Exiting from the With-draw Window ...")
        
        print("⭐"*40)
    elif ch==2:
        deposit=float(input("Enter the deposit amount:"))
        accounts[ano][-2]+=deposit
        print("---- Deposit Successful !!! ----")
        print("Current Balance: ",accounts[ano][-2])
        print("..Exiting from the Deposit Window ...")
        print("⭐"*40)
    elif ch==3:
        print("Dear Customer !! Welcome to Pin Generation: ")
        print("your acc no: ",ano)
        if accounts[ano][-1]==None:
            pin =int(input(f"Enter Your New pin {accounts[ano][0]} :"))
            accounts[ano][-1]=pin
            print("Pin is generated successfully")
            print("...Exiting from the Pin generation window......")
        else:
            decide=input("Pin is avaliable Do you want to change your password/reset password [y/n]: ")
            if decide.lower()=="y":
                old_pin =int(input("Enter your old pin:"))
                if accounts[ano][-1]==old_pin:
                    print("\"Confirmed Old Pin\"")
                    pin=int(input("Enter New Pin Now: "))
                    accounts[ano][-1]=pin
                    print("Pin is generated successfully")
                    print(".. Exiting from the pin generation ...")
                    
                else:
                    print("..you entered wrong old pin so Exiting from the pin generation ...")
            else:
                print("You disagreee to change the pin so back to main window ......")
                
        print("⭐"*40)
    elif ch==4:
        print("Dear Customer!! Here is your Mini Statement")
        try:
            pin=int(input("Enter the pin :"))
        except:
            agree=input("your account has NO PIN so we are redirecting you to the pin generation: Do you agree [yes(y)/no(n)]: ")
            if agree.lower()in ["yes","y"]:
                print("you are redirecting to main page........")
                continue
            else:
                print("you are disagreed so we can't provide this account details.....back to main page")
                continue
            
                
        if accounts[ano][-1]==None:
            print("Your pin is not generated go for pin generation")
        elif accounts[ano][-1]!=pin:
            print("Invalid Pin !!")
        else:
            print("Account No: ",ano)
            print(f"Name : {accounts[ano][0]}")
            month={1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"sep",10:"oct",11:"Nov",12:"dec"}
            dob=accounts[ano][1].split("-")
            dob[1]=month[int(dob[1])]
            dob="-".join(dob)
            print(f"Date of Birth: {dob}")
            print(f"Balance: {accounts[ano][2]}")
        print("..Exiting from the Mini Statement window ...")
        print("⭐"*40)
    elif ch>5:
        print("Invalid choice ")
        print("back to main window")
    else:
        print("Exiting from the ATM Thank you!!  Dear Customer visit again!!")
        print("⭐"*40)
        break

            
        
        
                    
                
    


  
