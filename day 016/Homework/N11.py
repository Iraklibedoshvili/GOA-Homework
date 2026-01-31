password1 = "goabest123"
password2 = input("enter your password: ")

while password2 != password1 : 
    password2 = input("enter your password: ")
    if password2 == password1:
        print("correct")
    else:
        password2 = input("enter your password: ")
    