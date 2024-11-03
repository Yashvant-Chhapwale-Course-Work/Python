def print_dictionary(dictionary): #Function To Print Dictionary Content In 'Key : Value' Format
    for key, value in dictionary.items():
        print(f'{key}: {value}')

def grade(student_scores):        #Grading_Logic (//As Per Indian Education System//)
    student_grades = {}           #Creating Empty Dictionary For Returning Grade Output

    for student, score in student_scores.items():
        if 90 <= score <= 100:
            student_grades[student] = "Outstanding"
        elif 75 <= score <= 89:
            student_grades[student] = "Distinction"
        elif 60 <= score <= 74:
            student_grades[student] = "First Class"
        elif 50 <= score <= 59:
            student_grades[student] = "Second Class"
        elif 35 <= score <= 49:
            student_grades[student] = "Passed"
        else:
            student_grades[student] = "Failed"

    print(": :Student_Grades: :")
    print_dictionary(student_grades) 

#-----------------------------------------------------------------------------------------------------------------------------------------------#
start_grading = input("Would you like to begin assessing student grades? (Y/N): ")
continue_grading = True

while continue_grading:
    if start_grading.lower() in ['yes','y']:
        student_scores = {}            #Creating Empty Dictionary For Taking Score Input

        print("Type 'STOP' to conclude data entry!")
        print(" ")

        while True:
            student = input("Enter Student's Name: ")
            marks = input("Enter Student's Marks: ")
            if any(input.lower() == 'stop' for input in [student, marks]): #Logic For Exiting Inner Loop
                print(" ")
                print(": :Student Scores: :")
                print_dictionary(student_scores)
                print(" ")
                grade(student_scores)
                print(" ")
                break
            else :
                student_scores [student.capitalize()] = int(marks)         #Storing User Input Into Dictionary In Key_Value Pairs
                print(" ")

        while True:
            start_grading = input ("Continue Grading? (Y/N): ")
            if start_grading.lower() in ['no','n']:
                print("Thank you for using the grading system. Exiting the program now.")
                continue_grading = False
                break
            elif start_grading.lower() in ['yes','y']:
                break
            else :
                print("Invalid Input :// Enter 'Yes' or 'No' ::")
                start_grading = input ("Continue Grading? (Y/N): ")
    elif start_grading.lower() in ['no','n']:
        print("We Hope To See You Soon!")
        break
    else:
        print("Invalid Input :// Enter 'Yes' or 'No' ::")
        start_grading = input("Would you like to begin assessing student grades? (Y/N): ")
        
        