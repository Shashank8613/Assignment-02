def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False

    return True


try:
    user_number = int(input("enter a number: "))

    if is_prime(user_number):
        print(f"{user_number} is a prime number")
    else:
        print(f"{user_number} is not a prime number")

    start_range = int(input("enter start range: "))
    end_range = int(input("enter end range: "))

    if start_range > end_range:
        raise ValueError("start range must be less than or equal to end range")

    prime_numbers = []

    for num in range(start_range, end_range + 1):
        if is_prime(num):
            prime_numbers.append(str(num))

    if prime_numbers:
        print("Prime numbers:", ", ".join(prime_numbers))
    else:
        print("No prime numbers found in the given range.")

#exception handling
except ValueError as ve:
    print("Error: ", ve)

except Exception as e:
    print("Error: ", e)