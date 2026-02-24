try:
    #taking input
    total_numbers = int(input("input how many numbers: "))

    if total_numbers <= 0:
        raise ValueError("number count must be greater than zero")

    numbers_list = []

    for i in range(1, total_numbers + 1):
        number = float(input(f"enter number {i}: "))
        numbers_list.append(number)

    total_sum = sum(numbers_list)
    average_value = total_sum / total_numbers
    maximum_number = max(numbers_list)
    minimum_number = min(numbers_list)

    #diaply
    print("Results:")
    print("Sum:", total_sum)
    print("Average:", average_value)
    print("Maximum:", maximum_number)
    print("Minimum:", minimum_number)

#exception handling
except ValueError as ve:
    print("Error: ", ve)

except Exception as e:
    print("Error: ", e)