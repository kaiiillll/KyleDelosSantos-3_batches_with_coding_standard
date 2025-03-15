print("please enter ten numbers")

even_count = 0

for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    if num % 2 == 0:
        even_count += 1
        
print(" The total even numbers are:", even_count)
