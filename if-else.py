# name = input("Enter your name : ")
# password = int(input("Enter your password_interger : "))

# if name == "glay" and password == 2003:
#     print("Oh, my master, welcome back!")
# elif name == "glay" or password == 2003:
#     print("Something is wrong! Try again.")
# else:
#     print("You are not allowed")

name = input("Enter your name : ")
password = int(input("Enter your password : "))

if name == "glay" and password == 2003:
    print("You are allowed to enter!")
elif name == "glay" or password == 2003:
    print("Something went wrong!")
else:
    print("No, you are not allowed.")