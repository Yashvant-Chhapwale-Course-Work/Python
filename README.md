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
| 3. **Day 3 : : `if-elif-else` Statements                                                                                                                               | >> [CHECK CONTENT](#day-3)                 |
| 4. **Day 4 : : Introduction to Python with `print()` Function**<br>                                                                                                    | >> [CHECK CONTENT](#day-4)                 |
| 5. **Day 5 : : Introduction to Python with `print()` Function**<br>                                                                                                    | >> [CHECK CONTENT](#day-5)                 |
| 6. **Day 6 : : Introduction to Python with `print()` Function**<br>                                                                                                    | >> [CHECK CONTENT](#day-6)                 |
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

## Important Concepts
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

## Important Concepts
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
