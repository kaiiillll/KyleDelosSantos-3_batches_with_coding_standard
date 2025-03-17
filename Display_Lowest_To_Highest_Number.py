print("Please Enter numbers: ")

numbers = []  
count = 0

while True:  # Loop continues until the input is invalid
    user_input = input("Enter a number: ")
    
    try:
        number = int(user_input)  
        numbers.append(number)  
        count += 1  
    except:
        print("That is Invalid!!!!") 
        break  # Stop when the input is invalid

sorted_numbers = sorted(numbers)  # Sort from lowest to highest
print("Numbers sorted from lowest to highest:", sorted_numbers)
