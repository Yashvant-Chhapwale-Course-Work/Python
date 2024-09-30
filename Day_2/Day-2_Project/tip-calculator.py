print("Welcome to the 'Tip Calculator'.")
print(" ")

total_bill = int(input("Enter Total Bill Amount:\n"))                         #The 'int()' Function is used to convert any data type to Integer Type.
tip = int(input("Enter Tip Amount:\n"))
no_of_people = int(input("Enter The Number Of People To Split The Bill:\n"))
bill_split = str((total_bill + tip)/no_of_people)                             #The 'str()' Function is used to convert any data type to String Type.
print(" ")

print("Each Person Should Pay: ₹" + bill_split)


