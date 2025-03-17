print("Enter ten numbers:")

numbers = []  
duplicates = set()  

for num in range(10):  
    number = int(input(f"Enter number {num+1}: ")) 
    numbers.append(number)

for num in numbers:
    if numbers.count(num) > 1:
        duplicates.add(num)

no_duplicates = [num for num in numbers if num not in duplicates]

print("You entered:", numbers)

if duplicates:
    print("Duplicate numbers:", duplicates)
else:
    print("There are no duplicates.")

print("Numbers without duplicates:", no_duplicates)
