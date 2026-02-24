try:
    #taking input
    subject1_marks = float(input("Enter marks for Subject 1: "))
    subject2_marks = float(input("Enter marks for Subject 2: "))
    subject3_marks = float(input("Enter marks for Subject 3: "))
    subject4_marks = float(input("Enter marks for Subject 4: "))
    subject5_marks = float(input("Enter marks for Subject 5: "))

    marks_list = [subject1_marks,subject2_marks,subject3_marks,subject4_marks,subject5_marks]

    #edge case
    for marks in marks_list:
        if marks<0 or marks>100:
            raise ValueError("Marks must be between 0 and 100.")

    total_marks = sum(marks_list)
    percentage = (total_marks/500)*100

    if percentage >= 90:
        grade = "A+ (Outstanding)"
    elif percentage >= 80:
        grade = "A (Excellent)"
    elif percentage >= 70:
        grade = "B (Good)"
    elif percentage >= 60:
        grade = "C (Average)"
    elif percentage >= 50:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"

    if all(marks>=40 for marks in marks_list):
        result = "Pass"
    else:
        result = "Fail"

    #display
    print("Results: ")
    print("marks in each subject:")
    print("Subject 1:",subject1_marks)
    print("Subject 2:",subject2_marks)
    print("Subject 3:",subject3_marks)
    print("Subject 4:",subject4_marks)
    print("Subject 5:",subject5_marks)

    print("total marks:", total_marks)
    print("percentage:",percentage)
    print("grade:", grade)
    print("result:", result)

#exception handling
except ValueError as ve:
    print("Error:",ve)

except Exception as e:
    print("Error:",e)