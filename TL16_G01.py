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

# login system | login or register
# returns "login"/"register"
def logOrReg():
    option = input("Would you like to login or register? \n\n").lower();
    return option;

# login system | login/registration
# called by loginSys() and returns (username, password, status)
def logReg(option):
    #user registration
    if option == "register":
        username = input("\nEnter your desired username: ");

        if(isSameUsername(username)):
            print("\nSame username exists within our database. Please register with another name.")
            print(f"Suggested usernames: {username}123, 123{username}\n");
            print("Redirecting to first screen...\n")
            time.sleep(3)
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
                        time.sleep(3);
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

# login system | registration
# opens registry.txt text file and registers user/admin credentials
# redirects to loginSys()
def register(username, password, status):
    file = open("registry.txt", "a");
    
    file.write(f"{username} | {password} | {status}\n");

    if(status == "ADMIN"):
        print(f"\nAdministrator Registration Success! Welcome, {username}!");
    else:
        print(f"\nMember Registration Success! Welcome, {username}!");
    
    file.close();

    print("Redirecting to first screen...\n");
    time.sleep(3);
    loginSys();
    
# login system | check for username duplicate
# returns True if contains same username in registry database; returns False if else
def isSameUsername(username):
    file = open("registry.txt", "r");

    for info in file:
        a = info.split(" | ")[0];
        if(username == a):
            return True;

    file.close();
    return False;

# login system | login
# opens "registry.txt" and cross checks for registered user credentials.
# redirects to loginSys() if credentials are false
# logins as admin if credentials are correct and user status = "ADMIN"; logins as user if status = "MEMBER"
# displays BANNED message to any banned users and redirects to loginSys()
def login(username, password, status):
    flag = True;
    file = open("registry.txt", "r")
    for info in file:
        a, b, c = info.split(" | ");
        b = b.strip();
        c = c.strip();

        if(username == a and password == b):
            if(c == "ADMIN"):
                print("Admin Login Attempt Successful! Navigating to Administrative Menu...\n");
                time.sleep(2);
                admin(username, password, status);
                flag = False;

            elif(c == "MEMBER"):
                print(f"Login Successful! Welcome {username}!");
                time.sleep(2);
                app(username, password, status);
                flag = False;

            elif(c == "BANNED"):
                print(f"User {username} Has Been Banned From Using Our Services. Thank You for Understanding.\n");
                print("Redirecting to First Screen...");
                time.sleep(3);
                loginSys();
                flag = False;

    if(flag):
        if(username == "admin"):
            print("Admin Login Attempt Unsuccessful. Redirecting to First Screen...");
            time.sleep(4);
            loginSys();
        else:
            print("Invalid username or password.\nRedirecting to first screen...");
            time.sleep(4);
            loginSys();
    file.close()

#login system END

#app START

#app | normal user START

# app | User Credential Change Master Function
# user detail change master function; asks for input and redirects to specialized functions
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

# app | user function #1 - Change user username
# prompts user to enter new username
# opens "registry.txt" as write mode and rewrites the line with previous user username
# replaces the line with previous user username with new username
def loginChangeUsername(username, password):
    clear();
    print("What would you like to change your username to?\n");
    print(f"Current Username: {username}");
    newUsername = input("New Username: ");

    if(isSameUsername(newUsername)):
        print("User With That Name Already Exists! Please Enter Another Name.\n");
        print("Redirecting Back to Previous Screen...\n");
        time.sleep(3);
        userDetailChange(username, password);

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
    time.sleep(3)
    loginSys();

# app | user function #2 - Change user password function
# same strategy with loginChangeUsername but changes password instead
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
                    time.sleep(3);
                    app(username, password);
                else:
                    print("\nInvalid input. Please try a valid input.\n");

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
        time.sleep(3);
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
                time.sleep(3);
                app(username, password);
            else:
                print("Invalid input. Please try again!\n");

# app | user function #3 - Viewing Retail Store
# displays all items for sale in format (Quantity | Name | Price) !All items are edit-able in admin menu
# asks user for input and redirects to either [1] - add items to cart; [2] - viewCart function; [3] - Redirects to user menu
# add items to cart by manipulating and appending cart items to current user in usersCart.txt
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

# app | user function #4 - Adding Items to Cart
# called by viewStore() function; Appends Cart Items to "usersCart.txt"
# using data in variable (cartItems) obtained in viewStore() function,
# appends items/"values" in cartItems to user cart in "usersCart.txt"
# if user already has existing cart in "usersCart.txt", simply append item to existing cart.
# if user does not have existing cart, create new line with format (username ||| cartItems);
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

# app | user function #5 - Viewing Items in Cart
# call-able by app() and viewStore() function
# opens "usersCart.txt" and displays items in format (QUANTITY | NAME | PRICE);
# prompts user for input for action which redirects to: [1] - checkOut() function, [2] - manageCart() function, [3] - viewStore() function, [4] - User menu     
def viewCart(username, password):
    clear();
    file = open("usersCart.txt", "r");
    totalPrice = 0.00;
    count = 0;
    
    file.seek(0);
    if(file.read() == ""):
        print(f"Your Cart is Empty. There is Nothing To Empty.\n");
        opt = input("Enter Any Input to Return to User Menu.\n");
        print("Redirecting to User Menu...\n");
        file.close();
        time.sleep(3);
        app(username, password, "MEMBER");

    else:
        file.close();
        print(f"Hello, {username}\n");
        print("Displaying Your Cart...\n");

        file = open("usersCart.txt", "r");
        for info in file:
            a, b = info.split(" ||| ");
            a = a.strip();
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
                        count += 1;
                        print(f"{count} | {name} | Price: RM{price}");

                    totalPrice = round(totalPrice, 2);
                    print(f"\n\nTotal Items: {count}   |   Total Price: RM{totalPrice}");
                    option = input("[1] - Check Out\n[2] - Empty Cart\n[3] - View Store\n[4] - Return to User Menu\n\n");

                    funcDict = {
                        '2' : emptyCart,
                        '3' : viewStore,
                    };

                    if(option == '1'):
                        count = 1;
                        totalPrice = 0.00;

                        print("Proceeding with Checkout...\n");
                        print("Total Billable Items: \n");
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
                        totalPrice = round(totalPrice, 2);
                        print(f"Total Price of Cart: RM{totalPrice}");

                        opt = input("\nConfirm Checkout?\n[1] - Confirm Order\n[2] - Cancel Checkout\n\n"); 

                        if(opt == '1'):
                            checkOut(username, password, totalPrice);
                        elif(opt == '2'):
                            print("Redirecting to User Menu...\n");
                            time.sleep(3);
                            app(username, password, "MEMBER");
                        else:
                            print("Invalid Input. Operation Cancelled.\n");
                            print("Redirecting to User Menu...\n");
                            time.sleep(3);
                            app(username, password, "MEMBER");

                    elif(option == '4'):
                        print("Redirecting to User Menu...\n");
                        time.sleep(3);
                        app(username, password, "MEMBER");

                    else:
                        funcDict[option](username, password);
            else:
                print(f"Your Cart is Empty. There is Nothing To Empty.\n");
                opt = input("Enter Any Input to Return to User Menu.\n");
                print("Redirecting to User Menu...\n");
                time.sleep(3);
                app(username, password, "MEMBER");

# app | user function #6 - Check out Items in Cart;
# asks user for confirmation
# if confirmed, empties cart and displays total price to be paid in physical outlet.
def checkOut(username, password, totalPrice):
    clear();
    file = open("usersCart.txt", "r");
    lines = file.readlines();
    file.close();

    file = open("usersCart.txt", "w");

    for line in lines:
        name = line.split(" ||| ")[0];
        if(name != username):
            file.write(line);

        print(f"Order Confirmed. Your Cart has Been Emptied.\nPlease Collect Your Items and Pay Cash of Amount [ RM{totalPrice} ] at Our Physical Outlet!");
        print("\nThank You for Shopping at ADHL Fashion Boutique. Please Visit Again!");
        x = input("Enter Any Key to Return to User Menu: ");
        app(username, password, "MEMBER");       

    file.close();

# app | user function #6 - Empty all user items in cart;
# asks user for confirmation
# if confirmed, removes user data and cart in "uesrsCart.txt"
def emptyCart(username, password):
    clear();
    file = open("usersCart.txt", "r");
    totalPrice = 0.00;
    count = 0;
    
    file.seek(0);
    if(file.read() == ""):
        print(f"Your Cart is Empty. There is Nothing To Display.\n");
        opt = input("Enter Any Input to Return to User Menu.\n");
        print("Redirecting to User Menu...\n");
        file.close();
        time.sleep(3);
        app(username, password, "MEMBER");

    else:
        file.close();
        file = open("usersCart.txt", "r");
        for info in file:
            a, b = info.split(" ||| ");
            a = a.strip();
            b = b.strip();

            if(username in a):
                print("Displaying Your Cart...\n");
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
                        count += 1;
                        print(f"{count} | {name} | Price: RM{price}");
                    opt = input("\nAre You Sure You Want to Empty Your Cart? [ Y / N ]\n").lower();

                    if(opt == 'y'):
                        file = open("usersCart.txt", "r");
                        lines = file.readlines();
                        file.close();

                        file = open("usersCart.txt", "w");
                        for line in lines:
                            info = line.split(" ||| ");
                            if(info[0] != username):
                                file.write(line);
                        file.close();

                        print("Your Cart has Been Successfully Emptied!\n");
                        print("Redirecting to User Menu...");
                        time.sleep(3);
                        app(username, password, "MEMBER");

                    else:
                        print("Cancelling Function...");
                        print("Redireciting to User Menu...\n");
                        time.sleep(3);
                        app(username, password, "MEMBER");

#app END

#admin START

# admin | admin function #1 - Manage Members
# displays all registered users, incl. admins.
# asks user for input to remove/ban/(return to admin menu)
# asks user for confirmation if selected option == "remove/ban" user
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
        time.sleep(3);
        adminManageMember(username, password);

# admin | admin function #2 - Removing Registered Member
# opens (registry.txt) and removes specified user credentials.
# removed user credentials no longer exists in database; unable to log in.
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
    time.sleep(3);
    admin(username, password);

# admin | admin function #3 - Banning Registered Member
# opens (registry.txt) and changes specified user status from "MEMBER" to "BANNED";
# banned user is no longer able to log in using their credentials.
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
    time.sleep(3);

    admin(username, password);

# admin | Editing Store Menu Master Function
# not done
def adminEditMenu(username, password):
    clear();
    print("Displaying Administrator Menu Editing Interface\n");
    print("Current Store Menu:\n");
    file = open("storeMenu.txt", "r");
    lines = file.readlines();
    file.close();

    file = open("storeMenu.txt", "r");
    totalPrice = 0.00;
    count = 0;
    
    for info in file:
        a, name, price = info.split(" | ");
        a = a.strip();
        name = name.strip();
        price = price.strip();
        print(f"{a} | Product: {name} | Price: RM{price}");
        count += 1;
        totalPrice += float(price);
        totalPrice = round(totalPrice, 2);
    print(f"\nTotal Item Count: {count}  |  Total Item Price: {totalPrice}");

    option = input("What Would You Like to Do?\n[1] - Add Items\n[2] - Remove Items\n[3] - Return to Administrator Menu\n\n");

    funcDict = {
        '1' : adminAddItem,
        '2' : adminRemoveItem,
    };

    if(option == '3'):
        funcDict[option](username, password, "ADMIN");
    else:
        funcDict[option](username, password);

#admin | Admin Function #4 - Adding New Items to Menu
def adminAddItem(username, password):
    clear();
    print("Option Selected: Adding Item to Menu\n");
    itemName = input("Enter New Item Name: ");
    itemPrice = float(input("Enter Price of New Item, (in 2 d.p.): "));
    count = 1;

    file = open("storeMenu.txt", "r");
    for info in file:
        count += 1;
    file.close();
    
    file = open("storeMenu.txt", "a");
    file.write(f"{count} | {itemName} | {itemPrice}\n");
    file.close();

    print("Item Has Been Successfully Added.\n");
    print("Showing New Menu...\n");
    file = open("storeMenu.txt", "r");
    for info in file:
        a = info.split(" | ");
        print(f"{a[0]} | Name: {a[1]} | Price: RM{a[2]}", end='');

    print("Redirecting Back to Administrator Menu...\n");
    time.sleep(3);
    admin(username, password, "ADMIN");

#admin | Admin Function #5 - Removng Items from Menu
def adminRemoveItem(username, password):
    clear();
    print("Displaying Store Menu...\n");
    file = open("storeMenu.txt", "r");
    totalPrice = 0.00;
    count = 0;
    
    for info in file:
        a, name, price = info.split(" | ");
        a = a.strip();
        name = name.strip();
        price = price.strip();
        print(f"{a} | Product: {name} | Price: RM{price}");
        count += 1;
        totalPrice += float(price);
        totalPrice = round(totalPrice, 2);
    print(f"\nTotal Item Count: {count}  |  Total Item Price: {totalPrice}");
    file.close();

    file = open("storeMenu.txt", "r");
    lines = file.readlines();
    file.close();

    option = input("\nEnter The Number of The Item You Want to Remove (Enter a Letter to Cancel): ");
    if(option.isdigit()):
        file = open("storeMenu.txt", "w");
        for line in lines:
            info = line.split(" | ");
            if(info[0] != option):
                file.write(line);
        file.close();

        count = 1;
        file = open("storeMenu.txt", "r");
        lines = file.readlines();
        file.close();

        file = open("storeMenu.txt", "w");
        for line in lines:
            info = line.split(" | ");
            info[0] = str(count);
            count += 1;
            file.write(" | ".join(info));
        file.close();

        print("Item Successfully Removed.\n");
        print("Displaying New Menu...\n");

        file = open("storeMenu.txt", "r");
        for info in file:
            a = info.split(" | ");
            print(f"{a[0]} | Name: {a[1]} | Price: RM{a[2]}");
        file.close();

        print("Redirecting Back to Administrator Menu...\n");
        time.sleep(3);
        admin(username, password, "ADMIN");

    else:
        print("Operation Cancelled. Returning to Administrator Menu...");
        time.sleep(3);
        admin(username, password, "ADMIN");

# admin | admin function #6 - Editing Administrator Accounts
# displays all registered administrator accounts
# prompts user for input to (create new account)/ (remove existing admin account)/ (return to admin menu)
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

# General function - Exits Program and Displays Exit Message c:
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
# First function to run in program.
# Prompts user to register/login
# Contains function dictionary to redirect to specified functions easily.
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
# Normal Member User Interface Master Function
# Contains Function Dictionary to Redirect User To Specific User Functions
def app(username, password, status):
    clear();
    print("_____________________________________________\n")
    print("Welcome to ADHL Fashion Boutique!");
    print(f"We are pleased to have you, {username}!");

    print("What would you like to do?\n");
    option = input("[1] - Edit Username/Password\n[2] - View Our Store\n[3] - View Cart\n[4] - Return to Login Menu\n[5] - Exit Program\n\n");
    while not(option.isdigit() and int(option) < 6 and int(option) > 1):
        print("\nInvalid Input Detected. Please Enter a Valid Prompt.\n");
        print("Redirecting to User Interface...\n");
        time.sleep(2);
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
# Admin User Interface Master Function
# Contains Function Dictionary to Redirect Admin to Specific Admin Functions
def admin(username, password, status):
    clear();
    print(f"Welcome back, {username}!");
    print("\nAdministrative Menu");
    print(f"What would you like to do, {username}?\n");

    option = input("[1] - Change Administrator Password\n[2] - Manage Registered Member List\n[3] - Manage Administrator Accounts\n[4] - Edit Store Menu\n[5] - Return to Login Menu\n[6] - Exit Program\n\n");
    while not(option.isdigit() and int(option) < 7 and int(option) > 0):
        print("\nInvalid Input Detected. Please Enter a Valid Prompt.\n");
        print("Redirecting to User Interface...\n");
        time.sleep(2);
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

# Initial Function Call
loginSys();