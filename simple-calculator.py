try:
    #asking for inputs
    first_number = float(input("enter your first number: "))
    second_number = float(input("enter your second number: "))
    
    print("Results:")
    #addition
    print(f"{first_number} + {second_number} = {first_number+second_number}")

    #subtraction
    print(f"{first_number} - {second_number} = {first_number-second_number}")
    
    #multiplication
    print(f"{first_number} * {second_number} = {first_number*second_number}")
    
    #division
    if second_number != 0:
        print(f"{first_number} / {second_number} = {first_number/second_number}")
    else:
        print("cannot divide by 0")
    
    #modulus
    if second_number != 0:
        print(f"{first_number} % {second_number} = {first_number%second_number}")
    else:
        print("cannot apply modulus to 0")
    
    #exponentiation
    print(f"{first_number} ** {second_number} = {first_number**second_number}")

except ValueError as ve:
    print("error: ",ve)

except Exception as e:
    print("error: ",e)