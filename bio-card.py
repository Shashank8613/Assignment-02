try:
    #accepting user input for the required fields
    student_name = input("enter your name: ")
    student_age  = int(input("enter your age: "))
    student_course = input("enter your course name: ")
    student_college = input("enter your college name: ")
    student_email = input("enter your email address: ")
    
    #handling exception conditions
    if student_age<=0:
        raise ValueError

    if '@' not in student_email or '.' not in student_email:
        raise ValueError
    
    #printing the bio card
    print("="*45)
    print("BIO_CARD".center(45))
    print("="*45)

    print(f"Name    : {student_name}")
    print(f"Age     : {student_age}")
    print(f"Course  : {student_course}")
    print(f"College : {student_college}")
    print(f"Email   : {student_email}")

    print("="*45)

#exception handling
except ValueError as ve:
    print("input error: ",ve)

except Exception as e:
    print("error: ",e)
    

