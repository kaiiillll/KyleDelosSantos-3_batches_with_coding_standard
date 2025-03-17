print("Please enter numbers:")

while True:  
    user_input = input("Enter a number: ")  

    try:
        number = int(user_input)  
        print("First valid number entered:", number)
        break  # Stop after the first valid entry
    except:
        print("That is invalid!!!!")
        break  # Stop when input is invalid