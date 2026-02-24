#1. factorial
def factorial(n):
    if n<0:
        return "factorial not defined for negative numbers"
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

#2. prime check
def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3, int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

#3. fibonacci (nth term)
def fibonacci(n):
    if n<0:
        return "Invalid input."
    if n==0:
        return 0
    if n==1:
        return 1
    a,b=0,1
    for _ in range(2,n+1):
        a,b=b,a+b
    return b

#4. sum of digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

#5. reverse number
def reverse_number(n):
    sign = -1 if n<0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign*reversed_num

#6. armstrong number check
def is_armstrong(n):
    digits = str(abs(n))
    power = len(digits)
    total = sum(int(digit)**power for digit in digits)
    return total==abs(n)

#7. GCD
def gcd(a, b):
    while b!=0:
        a,b = b,a%b
    return abs(a)

#8. LCM
def lcm(a,b):
    if a==0 or b==0:
        return 0
    return abs(a*b)//gcd(a,b)

#9. perfect number check
def is_perfect_number(n):
    if n<=1:
        return False
    divisors_sum = 0
    for i in range(1,n):
        if n%i == 0:
            divisors_sum += i
    return divisors_sum == n

#10. menu-driven function
def math_menu():
    while True:
        try:
            print("menu: ")
            print("1. Factorial")
            print("2. Prime Check")
            print("3. Fibonacci Number")
            print("4. Sum of Digits")
            print("5. Reverse Number")
            print("6. Armstrong Number Check")
            print("7. GCD")
            print("8. LCM")
            print("9. Perfect Number Check")
            print("10. Exit")

            choice = int(input("enter your choice (1-10): "))

            if choice == 10:
                print("exiting program")
                break

            elif choice == 1:
                n = int(input("enter number: "))
                print("factorial:", factorial(n))

            elif choice == 2:
                n = int(input("enter number: "))
                print("prime:" , "yes" if is_prime(n) else "No")

            elif choice == 3:
                n = int(input("enter term number: "))
                print("fibonacci:", fibonacci(n))

            elif choice == 4:
                n = int(input("enter number: "))
                print("sum of digits:", sum_of_digits(n))

            elif choice == 5:
                n = int(input("enter number: "))
                print("reversed number:", reverse_number(n))

            elif choice == 6:
                n = int(input("enter number: "))
                print("armstrong:", "yes" if is_armstrong(n) else "no")

            elif choice == 7:
                a = int(input("enter first number: "))
                b = int(input("enter second number: "))
                print("GCD:", gcd(a,b))

            elif choice == 8:
                a = int(input("enter first number: "))
                b = int(input("enter second number: "))
                print("LCM:", lcm(a,b))

            elif choice == 9:
                n = int(input("enter number: "))
                print("perfect Number:", "yes" if is_perfect_number(n) else "no")

            else:
                print("invalid choice")
        
        #exception handling
        except ValueError as ve:
            print("Error: ",ve)

        except Exception as e:
            print("Error: ", e)


math_menu()