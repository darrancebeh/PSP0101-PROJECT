def first():
    option = input("Would you like to login or register? \n")[0].lower()
    if option != "register" and option != "login":
        first()
    else:
        second(option)

def second(option):
    if option == "register":
        username = input("Input your username: ")
        password = input("Input your password: ")
        register(username,password)
    else:
        username = input("Enter your username: ")
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




dglkffsjdfjdfoidsjfiosfirst()