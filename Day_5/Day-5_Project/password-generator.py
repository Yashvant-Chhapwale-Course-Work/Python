import random
import string

print(r'''
                             .--------.
                            / .------. \
                           / /        \ \
                           | |        | |
                          _| |________| |_
                        .' |_|        |_| '.
                        '._____ ____ _____.'
                        |     .'____'.     |
                        '.__.'.'    '.'.__.'    
                        '.__  |      |  __.'
                        |   '.'.____.'.'   |
                        '.____'.____.'____.'
                        '.________________.'
      
******************************************************************
      ''')



letters_range = int(input("State The Number Of Letters You Wish To Include In The Password:"))
numbers_range = int(input("State The Number Of Digits You Wish To Include In The Password:"))
symbols_range = int(input("State The Number Of Special Characters You Wish To Include In The Password:"))
print(" ")

#Creating a 'password_generator()' Function.
def password_generator(letters_range, numbers_range, symbols_range):
    letters = list(string.ascii_letters) 
    numbers = list(range(10))
    symbols = list(string.punctuation)

    password_list = []
    password = ""
    print("Generating Password ", end="")
    for i in range(letters_range):
        password_list.append(str(random.choice(letters)))
        print(". ", end="")
    for i in range(numbers_range):
        password_list.append(str(random.choice(numbers)))
        print(". ", end="")
    for i in range(symbols_range):
        password_list.append(str(random.choice(symbols)))
        print(". ", end="")
    print(">>")

    random.shuffle(password_list)

    for char in password_list:
        password += char
    
    print ("Your Password Has Been Created: " + password)
    print(" ")

#Calling 'password_generator()' Function.
password_generator(letters_range, numbers_range, symbols_range)
    
#The 'string' module in Python provides a variety of useful constants and functions for working with strings.
#string.ascii_letters: A String Containing All ASCII Letters (Both Lowercase And Uppercase).
#string.digits: A String Containing All Decimal Digits (From 0-9).
#string.punctuation: A String Containing All Printable Punctuation Characters.

#The 'list()' Function In Python Is A Built-In Function Used To Create A List, Which Is A Versatile Data Structure That Can Hold An Ordered Collection Of Items.

#The 'def' Keyword Is Used To Define A Function In Python.A Function Is A Block Of Reusable Code That Performs A Specific Task.
#Syntax:
#def <function_name>(parameter_1, parameter_2, . . ., parameter_n):
#   return value
#To Call A Function, You Simply Use Its Name Followed By Parentheses
# <function_name>(parameter_1, parameter_2, . . ., parameter_n)