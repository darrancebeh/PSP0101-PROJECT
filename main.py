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

def first():
    option = input("Would you like to login or register? \n").lower()
    if option != "register" and option != "login":
        first()
    else:
        second(option)

def second(option):
    if option == "register":
        username = input("Enter your desired username: ")
        while(True):
            password = input("Enter your desired password: ")
            pwcheck = input("Please enter your password again: ")
            if(password == pwcheck):
                print(f"\nRegistration Success! Welcome, {username}!")
                register(username,password);
                return False;
            else:
                print("\nPasswords do not match.\nRedirecting back to password data entry...\n")
    else:
        username = input("Enter your username: ")
        if(username == "admin"):
            adminpass = "iamadmin1234";
            print("Admin Account Detected...")
            admintest = input("Please enter the administrative password: ")
            if(admintest == adminpass):
                print("Admin Password Accepted...\nRedirecting to administrative menu...")
                admin();
            else:
                print("Administrative Password Incorrect, Administrative Access Denied.\nRedirecting to login page...")
        else:
            password = input("Enter your password: ")
            login(username,password)

def register(username,password):
    file = open("registry.txt", "a")
    file.write(username + " | " + password + "\n")
    file.close()
    
def login(username,password):
    file = open("registry.txt", "r")
    for info in file:
        a,b = info.split(" | ")
        b = b.strip()
        if(a == username and b == password):
            print("Login successful! Welcome " + username + "!")
            app()
        else:
            print("Invalid username or password.\n Redirecting to first screen...")
            first()
    file.close()

def app():
    print("Welcome to Darrance's Login System!")
    print("Success.")

def admin():
    pass;

first()