try:
    #taking input
    number = int(input("enter a number: "))

    if number < 0:
        print("factorial is not defined for negative numbers")

    elif number == 0:
        print("0! = 1")
        print("Factorial of 0 is defined as 1")

    else:
        factorial_result = 1
        calculation_steps = []

        for i in range(number, 0, -1):
            factorial_result *= i
            calculation_steps.append(str(i))

        steps_display = " × ".join(calculation_steps)
        print(f"{number}! = {steps_display} = {factorial_result}")

#exception handling
except ValueError as ve:
    print("Error: ",ve)

except Exception as e:
    print("Error: ", e)