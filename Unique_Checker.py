print("Please Enter numbers:")

numbers = []  
seen = set()  

while True:  
    user_input = input("Enter a number: ")

    if user_input.isdigit():  
        number = int(user_input)
        numbers.append(number)  
    
        if number in seen:  
            print("Duplicate")  
        else:
            seen.add(number)  
            print("Unique")  
    else:
        print("That is Invalid!!!!") 
        break  

print("You entered:", numbers)
