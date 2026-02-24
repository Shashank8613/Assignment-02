try:
    #taking input
    year = int(input("enter a year: "))
    
    #checkimg if leap year
    if year%400 == 0:
        is_leap_year = True
        reason = "divisible by 400"

    elif year%100 == 0:
        is_leap_year = False
        reason = "divisible by 100 but not by 400"

    elif year%4 == 0:
        is_leap_year = True
        reason = "divisible by 4 and not divisible by 100"

    else:
        is_leap_year = False
        reason = "not divisible by 4"

    #display
    print("Results: ")
    print("year: ", year)

    if is_leap_year:
        print("leap year")
    else:
        print("not a leap year")
    print("reason:", reason)

#exception handling
except ValueError as ve:
    print("Error: ",ve)

except Exception as e:
    print("Error: ",e)