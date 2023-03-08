# Here we create the Calculator 

print(''' 
      1.select + for addition of numbers
      2.select - for substraction of numbers
      3.select * for multiplication of numbers
      4.select / for division of numbers
      Note: Use Appropriate operation on numbers
      ''')

# take the  fist user input here
number1=int(input("Enter the fisrt value :"))

#  here we are crate the operetins for values
opertion=(input("Enter the Operation for the values :"))

# take the second user input here
number2=int(input("Enter the second value :"))


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
