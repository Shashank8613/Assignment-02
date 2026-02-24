try:
    #taking input
    number = int(input("enter number: "))
    table_range = int(input("enter range (end): "))

    if table_range <= 0:
        raise ValueError("range must be a positive number")

    print(f"multiplication Table of {number}")

    #generating table
    for multiplier in range(1, table_range + 1):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")

#exception handling
except ValueError as ve:
    print("Error: ", ve)

except Exception as e:
    print("Error: ", e)