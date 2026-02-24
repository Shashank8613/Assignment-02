import random

while True:
    try:
        secret_number = random.randint(1, 100)
        max_attempts = 7
        attempts_used = 0

        print("number guessing game: ")
        print("i have selected a number between 1 and 100.")
        print("you have 7 attempts to guess it.")

        while attempts_used < max_attempts:
            guess = int(input("\nenter your guess: "))
            attempts_used += 1
            remaining_attempts = max_attempts - attempts_used

            if guess<secret_number:
                print("too low")
            elif guess>secret_number:
                print("too high")
            else:
                print(f"congratulations! You guessed the number in {attempts_used} attempts.")
                break

            print(f"attempts remaining: {remaining_attempts}")

        if guess!=secret_number:
            print(f"\nsorry! You've used all attempts.")
            print(f"the correct number was: {secret_number}")

        play_again = input("\ndo you want to play again? (yes/no): ")

        if play_again != "yes":
            print("thank you for playing! Goodbye.")
            break

#exceprion handling
    except ValueError as ve:
        print("Error: ",ve)

    except Exception as e:
        print("Error: ", e)