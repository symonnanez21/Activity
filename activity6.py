password = "12345678"

mypassword = input("Enter password: ")

if password == mypassword:
    print("Welcome to conditional statements")


elif mypassword == "987654321":
    print("Granted access!!") 

elif mypassword == "edipogitayo":
    print("You still have an access")

else:
    print("Access Denied")
