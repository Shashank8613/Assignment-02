try:
    #taking input
    user_input = input("enter word/number: ")

    if not user_input:
        raise ValueError("input cannot be empty")

    original_value = user_input

    normalized_value = str(user_input).lower()

    reversed_value = normalized_value[::-1]

    print("\nOriginal:", original_value)
    print("Reversed:", original_value[::-1])

    #checking palindrome condition
    if normalized_value == reversed_value:
        print("result: PALINDROME")
    else:
        print("result: NOT a palindrome")

#exception handling
except ValueError as ve:
    print("Error: ", ve)

except Exception as e:
    print("Error: ", e)