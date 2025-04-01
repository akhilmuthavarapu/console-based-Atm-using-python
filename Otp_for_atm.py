#---------------------------------------------------Acquired the OTP Validation file-----------------------------
from otp_validation import *

def otp_valid():
    print("your account has NO pin so you will receive a otp to your mail for login")
    ot=otp(accounts[ano][1])
    if ot== "OTP Verification Success":
        print("OTP verification success!!!\n")
        pin =int(input(f"Enter Your New pin {accounts[ano][0]} :"))
        accounts[ano][-1]=pin
        print()
        print("Pin is generated successfully")
    else:
        print("\nYou entered wrong OTP")

#---------------------------------------------------ACCOUNT CREATION ------------------------------------------------------------


print("Welcome to the Codegnan Bank ...\n ")
print("⭐"*40)
n=int(input("\nNo of Customers: "))
l=[]
acc=1001
for i in range(1,n+1):
    print(f"Account Number: {acc}")
    name=input(f"Enter Customer {i} name : ")
    email=input(f"Enter Customer {i} Email Address: ")
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
    l.append([name,email,dob,bal,pin])
    print(f"-----Customer {i} Details Saved Successfully -----")
    print(".........Exiting from the Account Creation..........")
    print("⭐"*40)
    
    acc+=1
accounts={}
transaction_history={}
acc=1001
for i in l:
    accounts[acc]=i
    transaction_history[acc]=[]
    acc+=1
    
#------------------------------------------------OPERATIONS-----------------------------------------------------

while True:
#-----------------------------------------ATM CONSOLE -----------------------------------------------------
    print("⭐"*40)
    print("\nWelcome to the Atm :\n")
    print("1. WITHDRAW")
    print("2. DEPOSIT")
    print("3. PIN GENERATION / RESET PIN")
    print("4. MINI STATEMENT")
    print("5. Transaction History")
    print("6. EXIT\n")
    print("⭐"*40)
#---------------------CHOICE-------------------------------------------------------------------------
    ch=int(input("\nEnter Your Choice:"))
    if ch!=6 and ch<6:
        ano=int(input("Enter the Account No [like 1001]:"))
        if ano not in accounts:
            print("\"Invalid Account Number \"")
            print("⭐"*40)
            print()
            continue
#---------------------WITHDRAW WINDOW-----------------------------------------------------------------
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
                    print()
                    continue
                else:
                    print("you are disagreed so we can't provide this account details.....back to main page")
                    print()
                    continue
            if accounts[ano][-1]==None:
                print("Your pin is not generated go for pin generation")
                    
            elif accounts[ano][-1]!=pin:
                print("Invalid Pin !!")
            else:
                
                amt=float(input("Enter your amount:"))
                if amt<=accounts[ano][-2]:
                    print()
                    print(" ---- Withdraw Successful !!!! ----\n")

                    print(f"Amount before withdraw : {accounts[ano][-2]}")
                    transaction_history[ano].append("Amount before withdraw :"+str(accounts[ano][-2]))
                    print(f"Amount Withdrawn: {amt}")
                    transaction_history[ano].append("Amount Withdrawn:"+str(amt))
                    accounts[ano][-2]-=amt
                    print("Current Balance: ",accounts[ano][-2])
                    transaction_history[ano].append("Balance: "+str(accounts[ano][-2]))
                    
                else:
                    print("\"Insufficient Funds Sir\"")
        print("..Exiting from the With-draw Window ...")
        
        print("⭐"*40)
#----------------------DEPOSIT WINDOW---------------------------------------------------------------------------------
        
    elif ch==2:
        deposit=float(input("Enter the deposit amount:"))
        print()
        print("---- Deposit Successful !!! ----\n")
        print(f"Amount: {accounts[ano][-2]}")
        transaction_history[ano].append("Amount: "+str(accounts[ano][-2]))
        accounts[ano][-2]+=deposit
        print("Deposited Amount: ",deposit)
        transaction_history[ano].append("Deposited Amount : "+str(deposit))
        print("Current Balance: ",accounts[ano][-2])
        transaction_history[ano].append("Balance : "+str(accounts[ano][-2]))
        print("..Exiting from the Deposit Window ...")
        print("⭐"*40)

#-----------------------PIN GENERATION & RESET WINDOW--------------------------------------------------------------
    
    elif ch==3:
        print("Dear Customer !! Welcome to Pin Generation: ")
        print()
        print("your acc no: ",ano)
        print(accounts[ano][1])
        if accounts[ano][-1]==None:
            otp_valid()
            print("...Exiting from the Pin generation window......")
        else:
            decide=input("Pin is avaliable Do you want to change your password/reset password [y/n]: ")
            if decide.lower()=="y":
                old_pin =int(input("Enter your old pin:"))
                if accounts[ano][-1]==old_pin:
                    print("\"Confirmed Old Pin\"")
                    pin=int(input("Enter New Pin Now: "))
                    accounts[ano][-1]=pin
                    print()
                    print("Pin is generated successfully")
                    print(".. Exiting from the pin generation ...")
                    
                else:
                    
                    print("\n..you entered wrong old pin so Exiting from the pin generation ...")
            else:
                
                print("\nYou disagreee to change the pin so back to main window ......")
                
        print("⭐"*40)

#------------------------MINI STATEMENT WINDOW-------------------------------------------------------------------
        
    elif ch==4:
        print("Dear Customer!! Here is your Mini Statement....\n")
        try:
            pin=int(input("Enter the pin :"))
        except:
            agree=input("your account has NO PIN so we are redirecting you to the pin generation: Do you agree [yes(y)/no(n)]: ")
            if agree.lower()in ["yes","y"]:
                print("\nyou are redirecting to main page........")
                continue
            else:
                
                print("\nyou are disagreed so we can't provide this account details.....back to main page")
                continue
            
                
        if accounts[ano][-1]==None:
            print("\nYour pin is not generated go for pin generation") 
        elif accounts[ano][-1]!=pin:
            print("\nInvalid Pin !!")
        else:
            print("Account No: ",ano)
            print(f"Name : {accounts[ano][0]}")
            month={1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"sep",10:"oct",11:"Nov",12:"dec"}
            dob=accounts[ano][2].split("-")
            dob[1]=month[int(dob[1])]
            dob="-".join(dob)
            print(f"Email - id: {accounts[ano][1]}")
            print(f"Date of Birth: {dob}")
            print(f"Balance: {accounts[ano][3]}")
        print("..Exiting from the Mini Statement window ...")
        print("⭐"*40)

#-----------------------TRANSACTION HISTORY WINDOW----------------------------------------------------------------------------------
        
    elif ch==5:
        print("Dear Customer!! Welcome to the Transaction History")
        
        if len(transaction_history[ano])==0:
            print("\n----No Transactions Made-------")
        else:
            for i in transaction_history[ano]:
                print(i)
                
        print("..Exiting the Transaction History ....")
        print("⭐"*40)
        
#-----------------------EXITING WINDOW --------------------------------------------------------------------------------------------
        
    elif ch>6:
        print("Invalid choice ")
        print("back to main window")
    else:
        print("\nExiting from the ATM Thank you!!  Dear Customer visit again!!")
        print("⭐"*40)
        break
    print()

            
        
        
                    
                
    


  
