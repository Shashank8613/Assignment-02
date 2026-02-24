
try:
    #taking input
    birth_year = int(input("enter your birth year"))

    current_year = 2026

    if birth_year<0 or birth_year>=current_year:
        raise ValueError("enter correct birth year")
    
    current_age = current_year-birth_year

    # calculation
    age_in_months = current_age * 12
    age_in_days = current_age * 365          
    age_in_hours = age_in_days * 24
    age_in_minutes = age_in_hours * 60
    years_until_100 = 100 - current_age

    #display
    print("Results :")
    print("Current age:", current_age)
    print("Age in months:", age_in_months)
    print("Age in days (approx):", age_in_days)
    print("Age in hours:", age_in_hours)
    print("Age in minutes:", age_in_minutes)

    if years_until_100 > 0:
        print("Years until age 100:", years_until_100)
    else:
        print("You are already 100 years old or above")

#exception handling
except ValueError as ve:
    print("Error:", ve)

except Exception as e:
    print("Error: ", e)