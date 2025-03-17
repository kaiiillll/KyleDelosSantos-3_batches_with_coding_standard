# ask the user to input ten numbers
print("please enter ten numbers")

total = 0

# proceed with the operation of adding the ten numbers using loops
for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    total += num
    
# print the results
print("The sum of ten numbers is:", total)
