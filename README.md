# Python Assignments

A Record Of Assignments Under Python Course Work From Udemy.

---

<div align="center">
 <h1>Table of Contents</h1>
</div>

<div align="center">

| TITLE                                                                                                                                                                  | SECTION_LINK                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| 1. **Day 1 : : Introduction to Python with `print()` Function**                                                                                                        | >> [CHECK CONTENT](#day-1)                 |
| 2. **Day 2 : : An Overview On Data Types, Type Casting in Python with<br> `int()`, `float()` & `str()` Function, Using `input()` Function <br>   To Take User Inputs** | >> [CHECK CONTENT](#day-2)                 |     
| 3. **Day 3 : : `if-elif-else` Statements**                                                                                                                             | >> [CHECK CONTENT](#day-3)                 |
| 4. **Day 4 : : `List` and `Loops` with Python**                                                                                                                        | >> [CHECK CONTENT](#day-4)                 |
| 5. **Day 5 : : Fun with `range()` Function**                                                                                                                           | >> [CHECK CONTENT](#day-5)                 |
| 6. **Day 6 : : `Python Functions` with `Reeborg Maze Challenge`**                                                                                                      | >> [CHECK CONTENT](#day-6)                 |
| 7. **Day 7 : : `Python Modules`, `The Hangman` Game**                                                                                                                  | >> [CHECK CONTENT](#day-7)                 |
| 8. **Day 8 : : `Parameterized Functions`, Implementing `Caesar Cipher`**                                                                                               | >> [CHECK CONTENT](#day-8)                 |
| 8. **Day 9 : : `Python Dictionaries`**                                                                                                                                 | >> [CHECK CONTENT](#day-9)                 |
</div>
 
---

## Day 1
### Coding_Exercise-1
 - Using `print()` Statement write a `Python Program` which gives the following Output: 
```
1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
2. Knead the dough for 10 minutes.
3. Add 3g of Salt.
4. Leave to rise for 2 hours.
5. Bake at 200 degrees C for 30 minutes.
```
### Coding_Exercise-2
 - Debug the following program to Print the Output without any Errors:
```
print(Notes from Day 1")
  print("The print statement is used to output strings")                 
print("Strings are strings of characters"                                  
priint("String Concatenation is done with the + sign")                     
print(("New lines can be created with a \ and the letter n")
```
### Coding_Exercise-3
 - `Swap` the values in the variables below without manually changing their values (Hint: Use A Third Variable `temp` As A Temporary Carrier Variable For The Process):
```
glass1 = "milk"
glass2 = "juice"
```
### Day-1_Project
 - Write A Program to create a `Band-Name Generator` which takes the user's `city` and `pet` as Input and `Concatenates` them to generate the Band-Name.

<div align = "center">
 _______________________________________________
</div>

## Important Concepts
 - The `print()` Function in Python is a Built-In Function used to Output Data to the Console or Standard Output Device.
 - The `" "` or `' '` are used for indicating the `String` Data Type.
 - The `+` Operator can be used for `Concatenation` of two or more Strings.
 - In Python, `Variables` are used to Store Data Values. They Act as Containers for Information that you can Use and Manipulate throughout your Program.
 - You can pass the value of variables inside the print function by using `F-strings`:<br>
   - `F-Strings` or `Formatted String Literals` are one of the most popular ways to include variables directly inside strings in Python.
   - An F-String is denoted with a `f` symbol at the start of a string.
     ```
     user = "Yashvant"
     print(f"Hi! My name is {user}.")
     ```

---

## Day 2
### Coding_Exercise-4
 - Write A Program to create a `BMI-calculator` which calculates the BMI for a Person by taking `Weight` & `Height` as inputs from User and Processing the formula:
   ```
   bmi = weight / (height ^ 2)
   ```
### Day-2_Project
 - Write A Program to create a `Tip-calculator` which takes the `total-bill`, `tipping-amount` & `number-of-persons-splitting-the-bill` as Input and calculates how much Amount Each Person    should Pay.

<div align = "center">
 _______________________________________________
</div>

<div align="center">
 <h2>Important Concepts</h2>
</div>

 - The `input()` Function in Python is used to take Input from the User. It reads a line from Standard Input (Typically From The Keyboard) and Returns it as a String.
   ```
    Syntax:
   <variable_name> = input("String To Be Displayed To User:")
   ```
 - **Primitive Data Types in Python:**
   - Number Type:
     - `int`: Represents Integer Values, which can be Positive, Negative, or Zero.
     - `float`: Represents floating-point numbers, which are numbers that have a decimal point.
   - Sequence Type:
     - `str`: Represents strings, which are sequences of characters.
   - Boolean Type:
     - `bool`: Represents Boolean values, which can be either True or False.
   - None Type:
     - `none type`: Represents the absence of a value.  
 - **Type Casting:**
    - In Python, `Type Casting` (or `Type Conversion`) is the Process of Converting One Data Type into Another.
    - `int()`: You can convert a Float or a String to an Integer using the 'int()' Function.
      ```
      num_str = "42"
      num_int_from_str = int(num_str) 
      ```
    - `float()`: You can convert a Float or a String to an Integer using the 'int()' Function.
      ```
      num_int = 5
      num_float = float(num_int)
      ``` 
    - `str()`: You can convert any Primitive Data Type to a String using the 'str()' Function.
      ```
      is_active = True
      str_from_bool = str(is_active)
      ```
    - `bool()`: You can convert any Primitive Data Type to a Boolean using the 'bool()' Function.
      ```
      none_value = None
      bool_from_none = bool(none_value)  # Result: False
      ```
    - The NoneType in Python represents the absence of a value. You can't "cast" other types to NoneType.

---

## Day 3
### Coding_Exercise-5
 - In the `BMI-calculator` add an `if-elif-else` block which if `bmi < 18` prints `Underweight!` , if `bmi >= 18 and bmi <25` prints `Healthy!`, else `bmi > 25` prints `Overweight!`.
### Day-3_Project
 - Write A Program to create a `Treasure-Hunter-Game`.

<div align = "center">
 _______________________________________________
</div>

<div align="center">
 <h2>Important Concepts</h2>
</div>

 - In Python, The `if`, `elif`, and `else` Statements are used for Conditional Execution of Code Blocks.
   ```
   Syntax:
   if condition1:
    # Code to execute if condition1 is True
   elif condition2:
    # Code to execute if condition2 is True
   else:
    # Code to execute if neither condition1 nor condition2 is True
   ```
 - `Nested if-elif-else` Statements in Python allow you to Check Multiple Conditions at Different Levels.
   ```
   Syntax:
   if condition1:
    # Code block for condition1
    if nested_condition1:
      # Code block for nested_condition1
    elif nested_condition2:
      # Code block for nested_condition2
    else:
      # Code block if nested_condition1 and nested_condition2 are false
   elif condition2:
    # Code block for condition2
   else:
    # Code block if all previous conditions are false
   ```
 - In Python, `"\n"` is a Special Escape Sequence that represents a Newline Character.
 - In Python, `"\"` can be used to Ignore any `'` or `"` within a String.
 - In Python, Triple Quotes (`'''` or `"""`) are used to create Multiline Strings.
 - `capitalize()` : Capitalizes the first character of the string and makes all other characters lowercase.
   ```
   text = "hello world!"
   capitalized_text = text.capitalize()
   print(capitalized_text)  # Output: "Hello world!"
   ``` 
- `upper()` : Converts all characters in the string to uppercase.
   ```
   text = "hello world!"
   uppercase_text = text.upper()
   print(uppercase_text)  # Output: "HELLO WORLD!"
   ```
- `lower()` : Converts all characters in the string to lowercase.
  ```
   text = "HELLO WORLD!"
   lowercase_text = text.lower()
   print(lowercase_text)  # Output: "hello world!"
   ```
- `title()` : Capitalizes the first letter of each word in the string.
   ```
   text = "hello world!"
   title_text = text.title()
   print(title_text)  # Output: "Hello World!"
   ```
   
---

## Day 4
### Day-4_Project
 - Write A Program to create a `Rock-Paper-Scissors-Game` which also keeps track of Player's `Winning-Streak` & `Losing-Streak`.

<div align = "center">
 _______________________________________________
</div>

<div align="center">
 <h2>Important Concepts</h2>
</div>

 - In Python, a `List` is a Versatile and Mutable (Changeable) Data Structure that can hold an Ordered Collection of Items. You can Create A List by Enclosing Elements in Square Brackets  `[]`, Separated by Commas.
   ```
   Syntax:
   <list_name> = [element_1, element_2, . . ., element_n]
   ```
 - In Python, the `random` mModule provides a Suite Of Functions to generate Random Numbers and perform Random Operations.
   - Before using the Functions in the `random` Module, you need to `import` it:
     ```
     import random  #The 'import' statements must always be declared at the start of a file before any code block.
     ```
   - `random.random()`: Returns a random float between 0.0 to 1.0.
     ```
     random_float = random.random()
     print(random_float)  # Example output: 0.37444887175646646
     ```
   - `random.uniform(a, b)`: Returns a random float between a and b.
     ```
     random_float = random.uniform(1, 10)
     print(random_float)  # Example output: 5.249982325624578
     ```
   - `random.randint(a, b)`: Returns a random integer between a and b, inclusive.
     ```
     random_int = random.randint(1, 100)
     print(random_int)  # Example output: 42
     ```
   - `random.choice(sequence`): Returns a randomly selected element from a non-empty sequence (like a list or a string).
     ```
     colors = ["red", "green", "blue", "yellow"]
     random_color = random.choice(colors)
     print(random_color)  # Example output: "blue"
     ```
   - `random.shuffle(x)`: Shuffles the sequence in place.
     ```
     deck = [1, 2, 3, 4, 5]
     random.shuffle(deck)
     print(deck)  # Example output: [3, 1, 5, 2, 4]
     ```   
 - In Python, `Loops` are used to execute a block of code repeatedly.
    - `for` Loop: A 'for' loop is used to iterate over a sequence (like a list, tuple, string, or range).
      ```
      Syntax:
      for variable in sequence:
         # Code to execute for each item
      ```
    - `while` Loop: A 'while' loop continues to execute as long as a specified condition is True.
      ```
      Syntax:
      while condition:
         # Code to execute as long as condition is True
      ```
    - `do-while` Loop: In Python, there isn't a built-in 'do-while' loop, but you can simulate a 'do-while' loop using a 'while' loop by ensuring that the loop's body is executed at least once. 
      ```
      Syntax:
      while True:     #This ensures that code is executed at least once before encountering the 'break' condition.
         # Code to execute
         # ...

         if not condition:
            break  # Exit the loop if the condition is False
      ```
    - `continue` Statement: The 'continue' statement skips the current iteration and moves to the next one.
      ```
      for i in range(5):
          if i == 2:
             continue  # Skip when i is 2
           print(i)
      ```
     - `break` Statement: The break statement is used to exit a loop prematurely.
       ```
       for i in range(10):
          if i == 5:
             break  # Exit the loop when i is 5
          print(i)
       ```
   
---

## Day 5
### Coding_Exercise-5
 - Write A Program to create a `FizzBuzz-Game` which prints `Fizz` if number is divisible by 3, `Bizz` if number is divisible by 5 & `FizzBuzz` if number is divisible by both 3 and 5.
### Day-5_Project
 - Write A Program to create a `Password-Generator` which takes `number-of-letter`, `number-of-digits` & `number-of-symbols` to be included in password, as input from User & genrates a Randomized String as Password, Accordingly. 

<div align = "center">
 _______________________________________________
</div>

<div align="center">
 <h2>Important Concepts</h2>
</div>

 - The `range()` Function in Python is a built-in function that generates a sequence of numbers.<br>
   It generally takes 3 parameters:
    - `start` : Defines starting value for the sequence. (included in sequence)
    -  `stop` : Defines endpoint for the sequence. (excluded from sequence)
    -  `step` : Defines the amount to increment the value by in the sequence.
   ```
   for i in range(10, 0, -2):
    print(i)

   Output:
   10
   8
   6
   4
   2
   ```
 - In Python, the `list()` Function is used to create a list from an iterable (like a string, tuple, or range). It can also be used to create an empty list.
     ```
     my_list = list("hello")
     print(my_list)  # Output: ['h', 'e', 'l', 'l', 'o']
     ```
 - The `string` module in Python provides a variety of functions and constants that are useful for string manipulation.
    - `string.ascii_letters`: A string containing all ASCII letters (both lowercase and uppercase).
      ```
      import string
      print(string.ascii_letters)  # Output: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
      ```
    - `string.ascii_lowercase`: A string of all lowercase ASCII letters.
      ```
      import string
      print(string.ascii_lowercase)  # Output: 'abcdefghijklmnopqrstuvwxyz'
      ```
    - `string.ascii_uppercase`: A string of all uppercase ASCII letters. 
      ```
      import string
      print(string.ascii_uppercase)  # Output: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      ```
    - `string.digits`: A string of digit characters (0-9).
      ```
      import string
      print(string.digits)  # Output: '0123456789'
      ```
     - `string.punctuation`: A string of all punctuation characters.
       ```
       import string
       print(string.punctuation)  # Output: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
       ```
   
---

## Day 6
### Day-6_Project
 - Write A Program for the `Reeborg-Robot`to solve any `Maze`. 

<div align = "center">
 _______________________________________________
</div>

<div align="center">
 <h2>Important Concepts</h2>
</div>

 - **Reeborg's World:**
   - `Reeborg's World` is an online platform designed for learning programming and computational thinking through fun and interactive challenges.
   - It uses a Robot named `Reeborg`, which can be controlled through simple programming commands in Python (or Reeborg’s native language) to solve puzzles.
   - You can access Reeborg’s World Maze at [Reeborg Maze](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)
   - Solution For Maze is given in [Day-6 Project](https://github.com/Yashvant-Chhapwale-Course-Work/Python/blob/main/Day_6/Day-6_Project/reeborg-maze.py). Copy this Code into the Reeborg's-Python-Terminal and Observe as 'The Robot' solves 'The Maze' from Different Starting Points.
<br>

 - **Python Functions:**
   - A function in Python is a block of organized, reusable code that is used to perform a single, related action.
   - Functions help in breaking the program into smaller and modular chunks, making the code easier to understand, debug, and maintain.
     ```
     Syntax:

     def <function_name>(parameters):
         # Function body
         # Code to be executed
     return result
     ```
   - You can execute a Function in Python by calling it using the <function_name>.
     ```
     <function_name>(parameter_values)
     ```
   - Python also provides `Built-In Functions` such as:
     - I/O Functions:
       - `print()`: Outputs data to the console.
       - `input()`: Accepts input from the user.
     - Type-Conversion Functions:
       - `int()`: Converts a value to an integer.
       - `float()`: Converts a value to a floating-point number.
       - `str()`: Converts a value to a string.
       - `list()`: Converts an iterable to a list.
       - `dict()`: Converts a sequence of key-value pairs into a dictionary.
     - Mathematical Functions:
       - `abs()`: Returns the absolute value of a number.
       - `min()`: Returns the smallest item in an iterable or the smallest of two or more arguments.
       - `max()`: Returns the largest item in an iterable or the largest of two or more arguments.
       - `sum()`: Returns the sum of all items in an iterable.
       - `pow()`: Returns the value of x raised to the power y (i.e., x ** y).
       - `round()`: Rounds a number to a given precision.
     - Iterating and Enumerating Functions:
       - `range()`: Returns a sequence of numbers, typically used for loops.
       - `enumerate()`: Returns an iterator that produces index-value pairs from a sequence.
         ```
         for index, value in enumerate(["a", "b", "c"]):
             print(index, value)
         # Output: 
         # 0 a
         # 1 b
         # 2 c
         ```
       - `filter()`: Filters elements from an iterable that satisfy a given function.
         ```
         def is_even(n):
             return n % 2 == 0
         
         result = filter(is_even, [1, 2, 3, 4])
         print(list(result))  # Output: [2, 4]
         ```
       - `map()`: Applies a function to every item in an iterable and returns an iterator.
         ```
         result = map(lambda x: x * 2, [1, 2, 3])
         print(list(result))  # Output: [2, 4, 6]
         ```
<div align = "center">
 _______________________________________________
</div>

<div align="center">
 <h2>Resources</h2>
</div>

- Reeborg's World Maze >> [CLICK HERE](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)
- Learn More About Reeborg's World >> [CLICK HERE](https://reeborg.ca/docs/en/reference/tour.html)
- Reeborg's Maze Solution >> [CLICK HERE](https://github.com/Yashvant-Chhapwale-Course-Work/Python/blob/main/Day_6/Day-6_Project/reeborg-maze.py)
  
---

## Day 7
### Day-7_Project
 - Write A Program to create The `Hangman-Game`.

<div align = "center">
 _______________________________________________
</div>

<div align="center">
 <h2>Important Concepts</h2>
</div>

 - What is the `Hangman-Game`?
    - Hangman is a classic word-guessing game that has been enjoyed by players of all ages.
    - The objective is to guess a hidden word, one letter at a time, before a "man" is fully drawn hanging from a noose.
    - The game is both educational and entertaining, often used to improve vocabulary and spelling skills.
 - **GamePlay Mchanics:**
    - Word Selection:
       - One player (or the computer) selects a word or phrase, keeping it hidden from the guesser.
       - The number of blanks or dashes represents the number of letters in the word.
    - Guessing::
       - The other player guesses one letter at a time, trying to figure out the hidden word.
       - If the letter is correct, it is revealed in its appropriate place(s) in the word.
       - If the letter is incorrect, a part of the hangman figure (typically a head, body, arms, and legs) is drawn on the gallows.
    - Winning:
       - The guesser wins if they can figure out the entire word before the hangman figure is completely drawn.
    - Losing:
       - The guesser loses if the entire hangman figure is drawn before they can guess the word.
<br>

 - **Python Modules:**
    - In Python, A `Module` is simply a `Python-File (with a .py extension)` that contains definitions (like functions, classes, or variables) which you can import and use in other Python scripts.
    - A Python Module can be `Built-In` Or `User-Defined`:
      - `Built-In Modules`:
         - Built-in Modules are pre-installed with Python and come as part of the Python-Standard-Library.
         - These modules provide ready-to-use functions, classes, and variables that cover common programming needs like mathematical operations, system operations, handling files, and much more.
         - Examples:
            - `math`: This Module provides `mathematical functions` like sqrt, sin, cos, etc.
              ```
              import math
              
              print(math.sqrt(16))  # Output: 4.0
              ```
            - `os`: This Module allows Python to `interact with the Operating System`, providing functions for file and directory management, environment variables, and more.
              ```
              import os

              # Get the current working directory
              current_directory = os.getcwd()
              print("Current Working Directory:", current_directory)

              # List files and directories in the current directory
              items = os.listdir()
              print("Files and Directories:", items)

              # Create a new directory
              os.mkdir("test_directory")
              
              # Remove the created directory
              os.rmdir("test_directory")
              ```
            - `random`: Used to `Generate Random Numbers and Selections`.
              ```
              import random
              
              print(random.randint(1, 10))  # Output: Random number between 1 and 10
              ```
            - `sys`: Gives `Access to System-Specific Parameters and Functions` (e.g., command-line arguments).
              ```
              import sys

              # Exit the program with a custom message
              print("Exiting program...")
              sys.exit(0)  # 0 indicates a clean exit

              # Add a new directory to the module search path
              sys.path.append("/path/to/directory")

              # Show the current module search paths
              print("Current sys.path:", sys.path
              ```
            - `datetime`: Handles `Date and Time Manipulation`.
              ```
              import datetime

              # Get the current date and time
              now = datetime.now()
              print("Current Date and Time:", now)

              # Define two dates
              date1 = datetime(2023, 1, 1)
              date2 = datetime(2024, 1, 1)

              # Calculate the difference between the two dates
              difference = date2 - date1
              print("Difference:", difference.days, "days")

              # Get the current date and time
              now = datetime.now()
              
              # Add 10 days to the current date
              future_date = now + timedelta(days=10)
              print("Future Date:", future_date)
              
              # Subtract 5 hours from the current time
              past_time = now - timedelta(hours=5)
              print("Past Time:", past_time)
              ```
      - `User-Defined Modules`:
         - User-defined modules are custom Python files created by the user, containing specific code like functions, classes, or variables that can be reused across different programs.
 - **Importing A Python Module:**
   - In Python, You can Import A Module using the `import` Keyword.
     ```
     import <module_name>
     ```
   - Importing Specific Functions/Classes:<br>
     Instead of importing the entire module, you can import specific functions or classes directly.
     ```
     from <module_name> import <function_name>, <class_name>
     ```
   - Importing a Module with an Alias:<br>
     You can also assign an `alias` to a Module to shorten the name you use in your code.
     ```
     import <module_name> as <alias>
     ```
   - Importing Everything from a Module:<br>
     ```
     from <module_name> import *
     ```
   
--- 

## Day 8
### Coding_Exercise-7
 - Write A Program to create a `life-in-weeks Calculator` which returns the number of weeks or years a person has left assuming that the maximum life expectancy of a person is 100 years. (**Note:** 1 year = 52 weeks)
### Coding_Exercise-8
 - Write A Program to create a `Cupid's Calculator` which calculates the match percentage for a couple. (Use any appropriate logic for the calculator function which must accept two strings as Input.)
### Day-8_Project
 - Write A Program to implement The `Caesar-Cipher`.

<div align = "center">
 _______________________________________________
</div>

<div align="center">
 <h2>Important Concepts</h2>
</div>

 - What is the `Caesar-Cipher`?
    - The **Caesar Cipher** is a basic encryption technique where each letter in a message is shifted by a fixed number of positions in the alphabet. 
    - In a Caesar Cipher, each letter in the plaintext is shifted right (or left) by a specific number, known as the **key** or shift.
    - This **key** or shift is used for both encoding and decoding.
      - `Encryption`: Shift each letter in the plaintext forward by the key.
      - `Decryption`: Shift each letter in the ciphertext backward by the key.
    - For example, with a shift of 3 **(Key = 3)**:
      - A becomes D
      - B becomes E
      - C becomes F
      - And so on . . .
<br>

 - **Parameterized Function:**
    - A `Parameter` is simply a variable in a function definition that accepts `values (arguments)` when the function is called, allowing the function to perform operations based on those inputs.
    - A Python Function can have single or multiple parameters as shown in the syntax ahead:
       ```
       def function_name(parameter1, parameter2, parameter3, ...., parameter n ):
          # Function Body: 'Code To Execute'
          return value   # Optional return statement
       ```
 - **Name Shadowing:**
    - `Name Shadowing` or `Variable Shadowing` occurs when a variable in a particular scope (like within a function or class) has the same name as a variable in an outer scope, "shadowing" or hiding the outer variable.
      ```
      x = 10  # Global variable

      def example():
          x = 5     # Local variable, shadows the global `x`.
          print(x)  # Prints 5, not the global `x` (10).

      example()
      
      print(x)  # Prints 10, as the global `x` remains unaffected.
      ```
--- 

## Day 9
### Coding_Exercise-9
 - Write A Program to create a `Student_Grading_System` which returns the number of weeks or years a person has left assuming that the maximum life expectancy of a person is 100 years. 
### Coding_Exercise-8
 - Write A Program to create a `Cupid's Calculator` which calculates the match percentage for a couple. (Use any appropriate logic for the calculator function which must accept two strings as Input.)
### Day-8_Project
 - Write A Program to implement The `Caesar-Cipher`.

<div align = "center">
 _______________________________________________
</div>

<div align="center">
 <h2>Important Concepts</h2>
</div>

 - What is the `Caesar-Cipher`?
    - The **Caesar Cipher** is a basic encryption technique where each letter in a message is shifted by a fixed number of positions in the alphabet. 
    - In a Caesar Cipher, each letter in the plaintext is shifted right (or left) by a specific number, known as the **key** or shift.
    - This **key** or shift is used for both encoding and decoding.
      - `Encryption`: Shift each letter in the plaintext forward by the key.
      - `Decryption`: Shift each letter in the ciphertext backward by the key.
    - For example, with a shift of 3 **(Key = 3)**:
      - A becomes D
      - B becomes E
      - C becomes F
      - And so on . . .
<br>

 - **Parameterized Function:**
    - A `Parameter` is simply a variable in a function definition that accepts `values (arguments)` when the function is called, allowing the function to perform operations based on those inputs.
    - A Python Function can have single or multiple parameters as shown in the syntax ahead:
       ```
       def function_name(parameter1, parameter2, parameter3, ...., parameter n ):
          # Function Body: 'Code To Execute'
          return value   # Optional return statement
       ```
 - **Name Shadowing:**
    - `Name Shadowing` or `Variable Shadowing` occurs when a variable in a particular scope (like within a function or class) has the same name as a variable in an outer scope, "shadowing" or hiding the outer variable.
      ```
      x = 10  # Global variable

      def example():
          x = 5     # Local variable, shadows the global `x`.
          print(x)  # Prints 5, not the global `x` (10).

      example()
      
      print(x)  # Prints 10, as the global `x` remains unaffected.
      ```
      
---
  
