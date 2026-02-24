#functions
def celsius_to_fahrenheit(celsius):
    return (celsius*9/5)+32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

def celsius_to_kelvin(celsius):
    return celsius+273.15

def kelvin_to_celsius(kelvin):
    return kelvin-273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit-32)*5/9+273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin-273.15)*9/5+32

#menu
while True:
    try:
        print("Menu")
        print("1.Celsius to Fahrenheit")
        print("2.Fahrenheit to Celsius")
        print("3.Celsius to Kelvin")
        print("4.Kelvin to Celsius")
        print("5.Fahrenheit to Kelvin")
        print("6.Kelvin to Fahrenheit")
        print("7.Exit")

        choice = int(input("enter your choice : "))

        if choice == 7:
            break

        temperature_value = float(input("enter temperature value : "))
        
        #choose and convert
        if choice == 1:
            result = celsius_to_fahrenheit(temperature_value)
            print(f"{temperature_value} °C = {result} °F")

        elif choice == 2:
            result = fahrenheit_to_celsius(temperature_value)
            print(f"{temperature_value} °F = {result} °C")

        elif choice == 3:
            result = celsius_to_kelvin(temperature_value)
            print(f"{temperature_value} °C = {result} K")

        elif choice == 4:
            result = kelvin_to_celsius(temperature_value)
            print(f"{temperature_value} K = {result} °C")

        elif choice == 5:
            result = fahrenheit_to_kelvin(temperature_value)
            print(f"{temperature_value} °F = {result} K")

        elif choice == 6:
            result = kelvin_to_fahrenheit(temperature_value)
            print(f"{temperature_value} K = {result} °F")

        else:
            print("invalid choice")
    
    #exception handling
    except ValueError as ve:
        print("Error: ",ve)

    except Exception as e:
        print("Error: ", e)