# *********************************************************
# Program: TL16L_G1.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Tutorial Section: TL16L Group: G1
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
import time;

#Clear Screen Function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear');

#login system START

#login system | login or register
def logOrReg():
    option = input("Would you like to login or register? \n").lower();
    return option;

#login system | login/registration
def logReg(option):
    #user registration
    if option == "register":
        username = input("Enter your desired username: ");

        if(isSameUsername(username)):
            print("\nSame username exists within our database. Please register with another name.")
            print(f"Suggested usernames: {username}123, 123{username}\n");
            print("Redirecting to first screen...\n")
            loginSys();

        flag = True;
        while(flag):
            password = input("Enter your desired password: ")
            pwcheck = input("Please enter your password again: ")
            if(password == pwcheck):
                return("regUser", username, password)
            else:
                rFlag = True;
                while(rFlag):
                    opt = input("\nPasswords do not match.\nWould you like to try again? [ Y / N ]\n").lower();
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
            print("\nAdmin Account Login Attempt Detected...");
            admintest = input("Please Enter the Administrator Password: ");
            return("logUser", username, admintest);
        else:
            password = input("Enter your password: ")
            return("logUser", username, password)

#login system | registration
def register(username,password):
    file = open("registry.txt", "a");
    
    if(username == "admin"):
        file.write(f"{username} | {password} | ADMIN\n");
        print(f"Administrator Registration Success! Welcome, {username}!");
    else:
        file.write(f"{username} | {password} | MEMBER\n");
        print(f"\nMember Registration Success! Welcome, {username}!");
    
    file.close();

    print("Redirecting to first screen...\n");
    loginSys();
    
#login system | check for username duplicate
def isSameUsername(username):
    file = open("registry.txt", "r");

    for info in file:
        a = info.split(" | ")[0];
        if(username == a):
            return True;

    file.close();
    return False;

#login system | login
def login(username,password):
    flag = True;
    file = open("registry.txt", "r")
    for info in file:
        a, b, c = info.split(" | ")
        b = b.strip();
        c = c.strip();

        if(username == a and password == b):
            if(c == "ADMIN"):
                print("Admin Login Attempt Successful! Navigating to Administrative Menu...\n");
                admin(username, password);
                flag = False;

            elif(c == "USER"):
                print(f"Login Successful! Welcome {username}!");
                app(username, password);
                flag = False;

            elif(c == "BANNED"):
                print(f"User {username} Has Been Banned From Using Our Services. Thank You for Understanding.\n");
                print("Redirecting to First Screen...");
                time.sleep(1);
                loginSys();
                flag = False;

    if(flag):
        if(username == "admin"):
            print("Admin Login Attempt Unsuccessful. Redirecting to First Screen...");
            loginSys();
        else:
            print("Invalid username or password.\nRedirecting to first screen...");
            loginSys();
    file.close()

#login system END

#app START

#app | normal user START

#app | user function #1 - Changing username/password
def userDetailChange(username, password):
    clear();
    print("Option Selected - [ Edit Username/Password ]\n");
    logDetOpt = input("What would you like to do? Input the respective number.\n[1] - Change Username\n[2] - Change Password\n[3] - Return to menu.\n\n");
    logDetDict = {
        '1' : loginChangeUsername,
        '2' : loginChangePassword,
        '3' : app,
    };

    logDetDict[logDetOpt](username, password);

def loginChangeUsername(username, password):
    clear();
    print("What would you like to change your username to?\n");
    print(f"Current Username: {username}");
    newUsername = input("New Username: ");

    file = open("registry.txt", "r");
    lines = file.readlines();
    file.close();

    file = open("registry.txt", "w");
    for line in lines:
        info = line.split(" | ");
        if info[0] == username:
            info[0] = newUsername;
            file.write(" | ".join(info));
        else:
            file.write(line);
    file.close();
    
    print("Username change successful! Please login again.");
    print("Redirecting to first screen...\n");
    loginSys();

def loginChangePassword(username, password):
    clear();
    flag = True;
    flag2 = True;
    print("Request to change password...");
    pw = input("Please enter your current password: ");
    if(pw == password):
        print(f"Username: {username}");
        print(f"Current password: {password}\n");
        while(flag):
            newPw = input("New Password: ");
            newPwCheck = input("Please input your new password again: ");
            
            if(newPwCheck != newPw):
                opt = input("\nPasswords do not match.\nWould you like to try again? [ Y / N ]\n").lower();
                if(opt == 'y'):
                    loginChangePassword(username, password);
                elif(opt == 'n'):
                    print("Redirecting to user menu...");
                    app(username, password);
                else:
                    print("Invalid input. Please try a valid input.\n");

            else:
                flag = False;

        file = open("registry.txt", "r");
        lines = file.readlines();
        file.close();

        file = open("registry.txt", "w");
        for line in lines:
            info = line.split(" | ");
            if info[0] == username:
                info[1] = newPw;
                file.write(" | ".join(info));
                file.write("\n");
            else:
                file.write(line);
        file.close();
        print("Password change successful! Please login again.");
        print("Redirecting to first screen...\n");
        loginSys();
        
    else:
        while(flag2):
            opt = input("Incorrect Password! Try again? [ Y / N ]\n").lower();
            if(opt == 'y'):
                flag = True;
                loginChangePassword(username, password);
            elif(opt == 'n'):
                flag = True;
                print("Redirecting to user menu...\n");
                app(username, password);
            else:
                print("Invalid input. Please try again!\n");

def viewStore(username, password):
    pass;

def viewCart(username, password):
    pass;


#app END

#admin START

def adminManageMember(username, password):
    clear();
    count = 1;
    print("Registered Members' List");
    print("[ Enter Username to View Actions ]\n");
    file = open("registry.txt", "r");
    for info in file:
        a, b, c = info.split(" | ");
        
        print(f"{count} | Username: {a} | Password: {b} | Privilege: {c}", end="");
        count += 1;
    file.close();

    prompt = input("\nEnter Member Username for More Actions: ");
    
    if(prompt in info):
        print(f"Selected Member: {prompt}\n");
        opt = input("What Would You Like to Do?\n[1] - Remove Member\n[2] - Ban Member\n[3] - Return to Member List\n[4] - Return to Administrative Menu\n\n");

        adminDict = {
            '1' : adminRemoveMember,
            '2' : adminBanMember,
        };

        if(opt == '3'):
            adminManageMember(username, password);
        elif(opt == '4'):
            admin(username, password);
        else:
            aOpt = input("Are You Sure You Want to Remove/Ban This Member? [ Y / N ]\nThis Action is IRREVERSIBLE.\n").lower();
            if(aOpt == "y"):
                adminDict[opt](username, password, prompt);
            elif(aOpt == "n"):
                print("Process Aborted. Redirecting to Member List...");
                adminManageMember(username, password);
            else:
                print("Invalid Input. Redirecting to Member List");
                adminManageMember(username, password);

    else:
        print("Invalid Input. Please Enter A Registered Member's Name.");
        time.sleep(1);
        adminManageMember(username, password);

def adminRemoveMember(username, password, member):
    file = open("registry.txt", "r");
    lines = file.readlines();
    file.close();

    file = open("registry.txt", "w");
    for line in lines:
        info = line.split(" | ");
        if(info[0] != member):
            file.write(line);
    file.close();

    print(f"{member} Has Been Successfully Removed.");
    print("Redirecting to Administrative Menu...");
    time.sleep(1);
    admin(username, password);

def adminBanMember(username, password, member):
    file = open("registry.txt", "r");
    lines = file.readlines();
    file.close();

    file = open("registry.txt", "w");
    for line in lines:
        info = line.split(" | ");

        if info[0] == member:
            info[2] = "BANNED\n";
            file.write(" | ".join(info));
        else:
            file.write(line);

    file.close();
    print("Member Successfully Banned.");
    print("Redirecting to Administrative Menu...");
    time.sleep(1);

    admin(username, password);
    

def adminEditMenu(username, password):
    pass;

#admin END

#MASTER FUNCTIONS START

#LOGIN SYSTEM MASTER FUNCTION
def loginSys():
    print("_____________________________________________________________\n")
    option = "";
    while(option != "register" or option != "login"):
        option = logOrReg();
        if(option == "register" or option == "login"):
            break;
        else:
            print("Please Enter a Valid Input. [ Login / Register ]\n");
    fType, username, password = logReg(option);

    funcDict = {
        "admin" : admin,
        "regUser" : register,
        "logUser" : login,
    }
    
    funcDict[fType](username, password);

#USER APP MASTER FUNCTION
def app(username, password):
    clear();
    print("_____________________________________________\n")
    print("Welcome to ADHL Fashion Boutique!");
    print(f"We are pleased to have you, {username}!");

    print("What would you like to do?\n");
    option = input("[1] - Edit Username/Password\n[2] - View Our Store\n[3] - View Cart\n[4] - Return to Login Menu\n\n");

    appDict = {
        '1' : userDetailChange,
        '2' : viewStore,
        '3' : viewCart,
        '4' : loginSys,
    };

    if(option == '4'):
        loginSys();
    else:
        appDict[option](username, password);


#ADMIN APP MASTER FUNCTION
def admin(username, password):
    clear();
    print(f"Welcome back, {username}!");
    print("\nAdministrative Menu");
    print(f"What would you like to do, {username}?\n");

    option = input("[1] - Change Administrator Password\n[2] - Manage Registered Member List\n[3] - Edit Store Menu\n[4] - Return to Login Menu\n\n");

    appDict = {
        '1' : loginChangePassword,
        '2' : adminManageMember,
        '3' : adminEditMenu,
    };

    if(option == '4'):
        loginSys();
    else:
        appDict[option](username, password);

#MASTER FUNCTIONS END

clear();
loginSys();