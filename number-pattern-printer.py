try:
    #menu
    print("choose a pattern:")
    print("1. Increasing number pattern")
    print("2. Repeated number pattern")
    print("3. Reverse decreasing pattern")
    print("4. Pyramid number pattern")

    pattern_choice = int(input("enter pattern number (1-4): "))
    height = int(input("enter height of the pattern: "))

    print("pattern")

    #pattern 1
    if pattern_choice == 1:
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    #pattern 2
    elif pattern_choice == 2:
        for i in range(1, height + 1):
            for j in range(i):
                print(i, end=" ")
            print()

    #pattern 3
    elif pattern_choice == 3:
        for i in range(height, 0, -1):
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()

    #pattern 4
    elif pattern_choice == 4:
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end="")
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()

    else:
        print("invalid pattern choice")

#exception handling
except ValueError as ve:
    print("Error: ", ve)

except Exception as e:
    print("Error: ", e)