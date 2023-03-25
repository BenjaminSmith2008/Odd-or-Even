print("Welcome")
#Welcomes the user and sets the valid input variable to true so the while loop runs
valid_input = True

print("What number are you thinking of? Make sure that it is between 1 and 1000?")

while valid_input == True:
    try:
    #will try their number input and if it is invalid like a letter for example this will accept it and get them to enter the number again
        # Provides a prompt before the user enters their number through the number variable
        number = int(input("Type your number here: "))
        # ask's the user to type in the number they are thinking of
        if 1 <= number <= 1000:
            # Checks if the number they entered is between 1 up to 1000
            if (number % 2) == 0: # This checks weather the number is even or not if it is odd you will get a remainder from this. for example 2
                print(str(number) + " is an even number.")
                break
                #if their number is even it will exit from the while loop
            else:
                print(str(number) + " is an odd number.")
                print("Have another go. ")
        else:
            print("Invalid input! Please try again but enter a number between 1 and 1000.")
        #if the user inputs a number beyond 1000 or less than 1 it will get the user to enter it again and repeat the process
    except ValueError:
        #checks that the user entered a number and will accept the error if they enter a letter for example - this is called a value error
        print("You entered an invalid input. Make sure that you enter a number.")


print("Thanks for playing! Hopefully you enjoyed it!")
