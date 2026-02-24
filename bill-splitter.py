try:
    #taking inputs
    total_bill = float(input("Enter total bill: "))
    number_of_people = int(input("Number of people: "))
    tax_percentage = float(input("Tax percentage: "))
    tip_percentage = float(input("Tip percentage: "))

    # edge case handling
    if total_bill <= 0:
        raise ValueError("input correct bill")
    if number_of_people <= 0:
        raise ValueError("input correct number of people")

    #calculation
    subtotal = total_bill
    tax_amount = (tax_percentage/100)*subtotal
    bill_after_tax = subtotal+tax_amount
    tip_amount = (tip_percentage/100)*bill_after_tax
    total_bill = bill_after_tax+tip_amount
    amount_per_person = total_bill/number_of_people

    #display
    print("Results: ")
    print(f"Subtotal : ₹{subtotal}")
    print(f"Tax ({tax_percentage}%) : ₹{tax_amount}")
    print(f"After tax : ₹{bill_after_tax}")
    print(f"Tip ({tip_percentage}%) : ₹{tip_amount}")
    print(f"Total : ₹{total_bill}")
    print(f"Per person : ₹{amount_per_person}")

#exceptions
except ValueError as ve:
    print("Error:", ve)

except Exception as e:
    print("Error: ", e)