# *********************************************************
# Program: TLXV_GX.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Tutorial Section: TLX Group: GX
# Trimester: 2215
# Year: 2022/23 Trimester 1
# Member_1: 1211108266 | DARRANCE BEH HENG SHEK
# Member_2: 1221101417 | AIRIL BIN AZLAN
# Member_3: 1211107977 | HONG CHIA QIAN
# Member_4: 1211109799 | LEE MEI SHAN
# *********************************************************
# Task Distribution
# Member_1: 
# Member_2: 
# Member_3: 
# Member_4: 
# *********************************************************

import os;

#Clear Screen Function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#login system START

#login system | login or register
def logOrReg():
    option = input("Would you like to login or register? \n").lower()
    if option != "register" and option != "login":
        print("Please enter a valid input.\n")
        logOrReg()
    else:
        return option;

#login system | login/registration
def logReg(option):
    #user registration
    if option == "register":
        username = input("Enter your desired username: ")

        if(isSameUsername(username)):
            print("Same username exists within our database. Please register with another name!")
            print(f"Suggested usernames: {username}123, 123{username}\n");
            print("Redirecting to first screen...\n")
            loginSys();

        flag = True;
        while(flag):
            password = input("Enter your desired password: ")
            pwcheck = input("Please enter your password again: ")
            if(password == pwcheck):
                print(f"\nRegistration Success! Welcome, {username}!")
                return("regUser", username, password)
            else:
                rFlag = True;
                while(rFlag):
                    opt = input("\nPasswords do not match.\nWould you like to try again? [Y/N]\n").lower();
                    if(opt == 'n'):
                        rFlag = False;
                        print("Redirecting to first screen...\n")
                        loginSys();
                    elif(opt == 'y'):
                        rFlag = False;
    
    #user/admin login
    elif option == "login":
        username = input("Enter your username: ")
        if(username == "admin"):
            adminpass = "iamadmin1234";
            print("Admin Account Detected...")
            admintest = input("Please enter the administrative password: ")
            if(admintest == adminpass):
                print("Admin Password Accepted...\nRedirecting to administrative menu...")
                return("admin", username, admintest);
            else:
                print("Administrative Password Incorrect, Administrative Access Denied.\nRedirecting to login page...")
                logReg(login);
        else:
            password = input("Enter your password: ")
            return("logUser", username, password)

#login system | registration
def register(username,password):
    file = open("registry.txt", "a");
    file.write(username + " | " + password + "\n");
    file.close();

    print("Registration Successful! Redirecting to first screen...");
    loginSys();
    
#login system | check for username duplicate
def isSameUsername(username):
    file = open("registry.txt", "r");

    for info in file:
        a,b = info.split(" | ");
        b = b.strip();
        if(username == a):
            return True;

    file.close();
    return False;

#login system | login
def login(username,password):
    file = open("registry.txt", "r")
    for info in file:
        a,b = info.split(" | ")
        b = b.strip()
        if(a == username and b == password):
            print(f"Login successful! Welcome {username}!");
            app(username, password);
        else:
            print("Invalid username or password.\nRedirecting to first screen...")
            loginSys();
    file.close()


#login system MASTER FUNCTION
def loginSys():
    option = logOrReg();
    fType, username, password = logReg(option);

    funcDict = {
        "admin" : admin,
        "regUser" : register,
        "logUser" : login,
    }
    
    funcDict[fType](username, password);

#login system END

#app START

#app | normal user START

#app | user function #1 - Changing password
def userPassChange(username, password):
    print("hi")


#app | normal user master function
def app(username, password):
    print("Welcome to ADHL Fashion Boutique!")
    userPassChange(username, password);


#app | normal user END

#app admin page
def admin(username, password):
    print(username, password)

#app END

clear();
loginSys();