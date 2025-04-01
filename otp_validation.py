#----------------------------Modules Required----------------------------------------
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#--------------------------OTP Creation----------------------------------------------
def otp(receiver):
    otp=random.randint(1000,9999)
    msg = MIMEMultipart()

    text = f"OTP for Verification is {otp}"     #OTP message

    msg["From"] = "akhilmuthavarapu1@gmail.com " #sender email address
    msg["To"] = receiver      #Receiver  email address
    msg["Subject"] = "OTP For Validation"       #subject text
    msg.attach(MIMEText(text,"plain"))          #OTP Msg appended with type of plain text
    #-------------------------Server Execution------------------------------------------
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login("akhilmuthavarapu1@gmail.com","bbgu elqr qynh flib")
    server.send_message(msg)
    server.quit()
    cotp = int(input(f"Enter OTP Received by {receiver} : "))
    
    if cotp==otp:
        return "OTP Verification Success"
    else:
        return "OTP invalid"

#------------------------ User choice of Transfer------------------------------------------
def userchoice():
    while True:
        choice=input("Do you want to send otp for single person or multiple persons \n Enter \n \"single\" To Access Single Person Sharing Window \n \"multiple\" To  Multiple Person Sharing  window \n Enter your choice: ")
        if choice.lower()=="single":
            print("You have chosen the single person sharing option ......... ")
            otp()
        elif choice.lower()=="multiple":
            print("You have chosen the multiple person sharing option ......... ")
            l=list(map(str,input("enter multiple emails separated by comma: ").split(",")))
            for i in l:
                print(i)
                otp(i)
        else:
            print("  You entered wrong option of transfer")
            ch=input("do you want to exit [y/n]: ")
            if ch.lower()=="y":
                break
            else:
                continue

    



















#bbgu elqr qynh flib 

