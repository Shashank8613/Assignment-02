try:
    #taking input
    age = int(input("enter age: "))
    day_of_week = input("enter day of the week: ")
    number_of_tickets = int(input("enter number of tickets: "))

    #edge case
    if age<0:
        raise ValueError("age cannot be negative.")
    if number_of_tickets<=0:
        raise ValueError("number of tickets must be at least 1.")

    if age<3:
        base_price = 0
        category = "free"
    elif 3<=age <= 12:
        base_price = 150
        category = "child"
    elif 13<=age <= 59:
        base_price = 300
        category = "adult"
    else:
        base_price = 200
        category = "senior"

    total_base_price = base_price * number_of_tickets

    if day_of_week in ["friday", "saturday", "sunday"]:
        discount_percentage = 20
        discount_amount = (discount_percentage / 100) * total_base_price
    elif day_of_week in ["monday", "tuesday", "wednesday", "thursday"]:
        discount_percentage = 0
        discount_amount = 0
    else:
        raise ValueError("enter correct day")

    final_price = total_base_price - discount_amount

    #display
    print("Results: ")
    print("category:", category)
    print(f"base price per ticket: ₹{base_price}")
    print("number of tickets:", number_of_tickets)
    print(f"total base price: ₹{total_base_price}")

    if discount_percentage > 0:
        print(f"discount ({discount_percentage}%): ₹{discount_amount}")
    else:
        print("discount: ₹0.00")

    print(f"price after discount: ₹{final_price}")
    print(f"total amount to pay: ₹{final_price}")

#exception handling
except ValueError as ve:
    print("Error:", ve)

except Exception as e:
    print("Error:", e)