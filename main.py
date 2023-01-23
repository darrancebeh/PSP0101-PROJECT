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
    option = input("Would you like to login or register? \n\n").lower();
    return option;

#login system | login/registration
def logReg(option):
    #user registration
    if option == "register":
        username = input("\nEnter your desired username: ");

        if(isSameUsername(username)):
            print("\nSame username exists within our database. Please register with another name.")
            print(f"Suggested usernames: {username}123, 123{username}\n");
            print("Redirecting to first screen...\n")
            loginSys();

        flag = True;
        while(flag):
            password = input("Enter your desired password: ");
            pwcheck = input("Please enter your password again: ");
            if(password == pwcheck):
                if(username.lower() == "admin"):
                    return("regUser", username, password, "ADMIN");
                else:
                    return("regUser", username, password, "MEMBER");
            else:
                rFlag = True;
                while(rFlag):
                    opt = input("\nPasswords do not match.\nWould you like to try again? [ Y / N ]\n").lower();
                    if(opt == 'n'):
                        rFlag = False;
                        print("Redirecting to first screen...\n");
                        loginSys();
                    elif(opt == 'y'):
                        rFlag = False;
    
    #user/admin login
    elif option == "login":
        username = input("\nEnter your username: ")
        if(username == "admin"):
            print("\nAdmin Account Login Attempt Detected...");
            admintest = input("Please Enter the Administrator Password: ");
            return("logUser", username, admintest, "ADMIN");
        else:
            password = input("Enter your password: ")
            return("logUser", username, password, "MEMBER");

#login system | registration
def register(username, password, status):
    file = open("registry.txt", "a");
    
    file.write(f"{username} | {password} | {status}\n");

    if(status == "ADMIN"):
        print(f"\nAdministrator Registration Success! Welcome, {username}!");
    else:
        print(f"\nMember Registration Success! Welcome, {username}!");
    
    file.close();

    print("Redirecting to first screen...\n");
    time.sleep(1);
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
def login(username, password, status):
    flag = True;
    file = open("registry.txt", "r")
    for info in file:
        a, b, c = info.split(" | ")
        b = b.strip();
        c = c.strip();

        if(username == a and password == b):
            if(c == "ADMIN"):
                print("Admin Login Attempt Successful! Navigating to Administrative Menu...\n");
                admin(username, password, status);
                flag = False;

            elif(c == "MEMBER"):
                print(f"Login Successful! Welcome {username}!");
                app(username, password, status);
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
    clear();
    print("ADHL Fashion Store Catalogue: \n");
    file = open("storeMenu.txt", "r");

    for info in file:
        a, b, c = info.split(" | ");
        a = a.strip();
        b = b.strip();
        c = c.strip();

        print(f"{a} | Item: {b} | Price: RM{c}");
    file.close();

    option = input("\n\nWhat Would You Like to Do?\n\n[1] - Add Items To Cart\n[2] - View Cart\n[3] - Return to User Menu\n\n")

    funcDict = {
        '2' : viewCart,
        '3' : app,
    };

    if(option == '1'):
        clear();
        print("ADHL Fashion Store Catalogue:\n");
        flag = True;
        totalCart = [];

        file = open("storeMenu.txt", "r");

        for info in file:
            a, b, c = info.split(" | ");
            a = a.strip();
            b = b.strip();
            c = c.strip();

            print(f"{a} | Item: {b} | Price: RM{c}");

        while(True):
            aTCart = input("\n\nEnter The Item's Respective Number to Add Item to Cart: ");
            totalCart += aTCart;
            opt = input("Do You Want to Add More Items To Cart? [ Y / N ]\n").lower();
            
            if(opt != 'y' and opt != 'n'):
                while(flag):
                    print("Please Input a Valid Option");
                    opt = input("Do You Want to Add More Items To Cart? [ Y / N ]\n");
                    if(opt == 'y' or opt == 'n'):
                        flag = False;
            else:
                if(opt == 'y'):
                    pass;
                else:
                    addCart(username, password, totalCart);
                    break;

    else:
        funcDict[option](username, password);

def addCart(username, password, cartItems):
    file = open("usersCart.txt", "r");
    lines = file.readlines();
    file.close();

    cart = [];

    file = open("storeMenu.txt", "r");
    for info in file:
        for item in cartItems:
            a, b, c = info.split(" | ");
            a = a.strip(); 
            b = b.strip(); 
            c = c.strip();

            if(item == a):
                cart.append(f"{b} | {c}");

    file.close();

    nameList = [];
    for line in lines:
        name = line.split(" ||| ")[0];
        nameList.append(name);

    if(username not in nameList):
        file = open("usersCart.txt", "a");

        file.write(f"{username} ||| {cart}\n");

        file.close();

    else:
        file = open("usersCart.txt", "r");
        for info in file:
            a, b = line.split(" ||| ");
            a = a.strip();
            b = b.strip();

            if(a == username):
                cart.append(b[2:-2]);
        file.close();

        file = open("usersCart.txt", "w");
        for line in lines:
            info = line.split(" ||| ");
            if(info[0] == username):
                file.write(f"{username} ||| {cart}\n");
            else:
                file.write(line);
            
def viewCart(username, password):
    clear();
    print(f"Hello, {username}!\nDisplaying your Cart...\n");

    file = open("usersCart.txt", "r");
    totalPrice = 0.00;
    count = 1;

    for info in file:
        a, b = info.split(" ||| ");
        b = b.strip();
        if(username in a):
            if(a == username):
                items = b.split(", ");
                for item in items:
                    item = item.strip("'");
                    item = item.strip("[");
                    item = item.strip("]");
                    item = item.strip('"');
                    item = item.strip("['");

                    name, price = item.split(" | ");
                    name = name.strip();
                    price = price.strip();
                    price = float(price);
                    totalPrice += price;
                    print(f"{count} | {name} | Price: RM{price}");
                    count += 1;
                totalPrice = round(totalPrice, 3);
                print(f"\n\nTotal Items: {count}   |   Total Price: RM{totalPrice}");
                option = input("[1] - Check Out\n[2] - Remove Items from Cart\n[3] - View Store\n[4] - Return to User Menu\n\n");

                funcDict = {
                    '3' : viewStore,
                    '4' : app,
                };

                if(option == '3' or option == '4'):
                    funcDict[option](username, password);
                else:
                    if(option == '1'):
                        pass;
                        #YOU STOPPED HERE  ^
                        #KEYNOTE: CHECK OUT CART / REMOVE ITEMS FROM CART
                        #YOU STOPPED HERE  ^
                        #YOU STOPPED HERE  ^
                        #YOU STOPPED HERE  ^
                        #YOU STOPPED HERE  ^
                        #YOU STOPPED HERE  ^
                        #YOU STOPPED HERE  ^
                        #YOU STOPPED HERE  ^
                        
                
        else:
            print(f"Your Cart is Empty. There is Nothing To Display.\n");
            opt = input("Enter Any Input to Return to User Menu.\n");
            print("Redirecting to User Menu...\n");
            time.sleep(1);
            app(username, password, "MEMBER");

    file.close();

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

def adminManageAdmins(username, password):
    clear();
    print("Selected Option: New Administrator Account Creation\n");
    print("_____________________________________________________________\n");
    print("Registered Administrator Accounts:\n");

    file = open("registry.txt", "r");
    count = 1;

    for info in file:
        a, b, c = info.split(" | ");
        b = b.strip();
        c = c.strip();

        if(c == "ADMIN"):
            print(f"{count} | {a} | {b} | Status: {c}");

    file.close();
    
    option = input("What Would You Like to Do?\n\n[1] - Create New Administrator Account\n[2] - Remove Administrator Account\n[3] - Return to Administrative Menu\n\n");

    funcDict = {
        '1' : register,
        '2' : adminRemoveMember,
        '3' : admin,
    };

    if(option == '1'):
        newUsername = input("\nEnter Username for New Account: ");

        flag = True;
        while(flag):
            newPw = input("Enter your desired password: ");
            newPwCheck = input("Please enter your password again: ");
            if(newPwCheck == newPw):
                flag = False;
                register(newUsername, newPw, "ADMIN");
            else:
                print("Passwords Do Not Match. Please Try Again...\n");
    
    else:
        funcDict[option](username, password, "ADMIN");

#admin END

#GENERAL FUNCTIONS START

def exitProgram(username, password):
    clear();
    print(f"Thank You For Browsing ADHL Fashion Boutique!\n");
    print(f"We Hope You Enjoyed Your Stay, {username}!");
    print("Do Visit Us Again!\n\n");

    print("Exiting Program...");
    time.sleep(2);

#GENERAL FUNCTIONS END

#MASTER FUNCTIONS START

#LOGIN SYSTEM MASTER FUNCTION
def loginSys():
    clear();
    print("_____________________________________________________________\n");
    option = "";
    while(option != "register" or option != "login"):
        option = logOrReg();
        if(option == "register" or option == "login"):
            break;
        else:
            print("Please Enter a Valid Input. [ Login / Register ]\n");
    fType, username, password, status = logReg(option);

    funcDict = {
        "admin" : admin,
        "regUser" : register,
        "logUser" : login,
    }
    
    funcDict[fType](username, password, status);

#USER APP MASTER FUNCTION
def app(username, password, status):
    clear();
    print("_____________________________________________\n")
    print("Welcome to ADHL Fashion Boutique!");
    print(f"We are pleased to have you, {username}!");

    print("What would you like to do?\n");
    option = input("[1] - Edit Username/Password\n[2] - View Our Store\n[3] - View Cart\n[4] - Return to Login Menu\n[5] - Exit Program\n\n");

    appDict = {
        '1' : userDetailChange,
        '2' : viewStore,
        '3' : viewCart,
        '4' : loginSys,
        '5' : exitProgram,
    };

    if(option == '4'):
        loginSys();
    else:
        appDict[option](username, password);

#ADMIN APP MASTER FUNCTION
def admin(username, password, status):
    clear();
    print(f"Welcome back, {username}!");
    print("\nAdministrative Menu");
    print(f"What would you like to do, {username}?\n");

    option = input("[1] - Change Administrator Password\n[2] - Manage Registered Member List\n[3] - Manage Administrator Accounts\n[4] - Edit Store Menu\n[5] - Return to Login Menu\n[6] - Exit Program\n\n");

    appDict = {
        '1' : loginChangePassword,
        '2' : adminManageMember,
        '3' : adminManageAdmins,
        '4' : adminEditMenu,
        '6' : exitProgram,
    };

    if(option == '5'):
        loginSys();
    else:
        appDict[option](username, password);

#MASTER FUNCTIONS END

loginSys();