print("Welcome to the 'Body Mass Index (BMI) Calculator'.")
print(" ")

weight = input("Enter Your Weight in Kilograms:\n")
height = input("Enter Your Height in Meters:\n")
bmi = float(weight)/(float(height) ** 2)

if bmi < 18.5:                                                    # In Python, 'if', 'elif', and 'else' statements are used for conditional execution of code blocks. They allow you to control the flow of the program by executing different code based on certain conditions.
    print("BMI: " + str(bmi) + "\n")                              # Syntax:
    print("Alert! Your are Underweight!")                                 #if condition1:                                                              
elif bmi >= 18.5 and bmi < 25:                                              #Block of code to execute if condition1 is True                                                              
    print("BMI: " + str(bmi) + "\n")                                      #elif condition2:                                                             
    print("Smile You are Healthy!")                                         # Block of code to execute if condition2 is True                                                                 
elif bmi >= 25 and bmi < 30:                                              #else:                                      
    print("BMI: " + str(bmi) + "\n")                                        # Block of code to execute if none of the above conditions are True
    print("Alert! Your are Overweight!") 
else:
    print("Alert! Visit a Doctor!") 