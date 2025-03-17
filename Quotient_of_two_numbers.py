# ask the user to input two numbers
print("please enter two numbers")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# check if the input is not equal to zero
if num2 != 0:
    Quotient = num1 / num2 # if not proceed with the operation
    print("the Quotient of the two numbers is" , Quotient) # print the results
else:
    print("cannot be")

