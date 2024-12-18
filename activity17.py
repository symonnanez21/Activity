tuloy = True

while tuloy:
    print("-------------------------------")
    print("WELCOME TO MY COMPILATION PROGRAM")

    print("PLEASE SELECT FROM THE OPTIONS BELOW")
    print("1 -- RIGHT TRIANGLE")
    print("2 -- FACTORIAL")
    print("3 -- GREET SOMEONE")
    print("4 -- EXIT")

    choice = eval(input("Which program would you like to run (1,2,3,4) -- > "))

    if choice == 1:
        print("THIS IS A PROGRAM THAT WILL SHOW YOU A RIGHT TRIANGLE MADE FROM PYTHON")
        right_Triangle()
        continue
    elif choice == 2:
        print("THIS IS A PROGRAM THAT CALCULATES FACTORIAL")
        number = eval(input("enter a number "))
        factorial(number)
        continue
    elif choice == 3:
        greet_Someone()
        continue
    elif choice == 4:
        print("Program Terminated")
        break
    else:
        print("INVALID CHOICE")
        continue
