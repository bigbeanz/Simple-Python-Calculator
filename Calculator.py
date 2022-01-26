



def main():
    
    global userSelection

    userSelection = input("Please select what calculations you would like to do: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n ")

    userSelection = int(userSelection) # how do I make it int or float depending on user input??




    #Some more complex stuff, I want to be able to select how many numbers I use, not just 2.
    
    
    #userNumberQuantity = input("How many numbers would you like to use?: ")

    #n = 0
    #userNumberList = []
    #while n != int(userNumberQuantity):
    #    n += 1
    #    userNumberList += [input("enter number " + str(n) + ": ")]

    
    
    global userNumber1
    global userNumber2

    userNumber1 = input("Please enter your first number: ")
    userNumber2 = input("Please enter your second number: ")

    userNumber1 = int(userNumber1)
    userNumber2 = int(userNumber2)

    if userSelection == 1:
        addition()
    elif userSelection == 2:
        subtraction()
    elif userSelection == 3:
        multiplication()
    elif userSelection == 4:
        divide()
    


def addition():
    addSum = int(userNumber1) + int(userNumber2)
    print("The sum of " + str(userNumber1) + " + " + str(userNumber2) + " is: " + str(addSum))

def subtraction():
    difference = int(userNumber1) - int(userNumber2)
    print("The difference of " + str(userNumber1) + " - " + str(userNumber2) + " is: " + str(difference))

def multiplication():
    product = int(userNumber1) * int(userNumber2)
    print("The product of " + str(userNumber1) + " * " + str(userNumber2) + " is: " + str(product))

def divide():
    quotient = int(userNumber1) / int(userNumber2)
    print("The quotient of " + str(userNumber1) + " / " + str(userNumber2) + " is: " + str(quotient))

main()

#Created by Benjamin Arroyo