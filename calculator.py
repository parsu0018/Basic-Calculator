# Here we create the Calculator 

# take the  fist user input here
number1=int(input("Enter the fisrt value :"))

#  here we are crate the operetins for values
opertion=(input("Enter the Operation for the values :"))

# take the second user input here
number2=int(input("Enter the second value :"))

# addition=(number1+number2)
# substraction=(number1-number2)
# division=(number1//number2)
# multiplication=(number1*number2)


# Here we write the code for conditions

if opertion == '+' :
    print(" The Addition is :",number1+number2)
elif opertion == '-':
    print(" The Substraction is :",number1-number2)
elif opertion == '/':
    print(" The Division is :",number1/number2)
elif opertion == '*':
    print(" The Multiplication is :",number1*number2)
else:
    print("Please enter the correct Operation")
