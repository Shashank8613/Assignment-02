#function definitions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error: division by zero is not allowed"
    return a / b

def modulus(a, b):
    if b == 0:
        return "error: modulus by zero is not allowed"
    return a % b

def power(a, b):
    return a ** b


def calculator():
    while True:
        try:
            print("menu")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Modulus")
            print("6. Power")
            print("7. Exit")

            choice = int(input("enter your choice (1-7): "))

            if choice == 7:
                print("exiting calculator")
                break

            #taking input
            first_number = float(input("enter first number: "))
            second_number = float(input("enter second number: "))

            if choice == 1:
                result = add(first_number, second_number)
            elif choice == 2:
                result = subtract(first_number, second_number)
            elif choice == 3:
                result = multiply(first_number, second_number)
            elif choice == 4:
                result = divide(first_number, second_number)
            elif choice == 5:
                result = modulus(first_number, second_number)
            elif choice == 6:
                result = power(first_number, second_number)
            else:
                print("invalid choice")
                continue

            print("Result:", result)

        #exception handling
        except ValueError as ve:
            print("Error: ",ve)

        except Exception as e:
            print("Error: ", e)

calculator()