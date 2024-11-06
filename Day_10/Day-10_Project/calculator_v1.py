import inspect

#Operation_Logic------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def addition(Operand_1, Operand_2):
    try:
        return Operand_1 + Operand_2
    except Exception as e :
        err = str(e)
        print(f"Error! {err.title()}")
        return None

def subtraction(Operand_1, Operand_2):
    try:
        return Operand_1 - Operand_2
    except Exception as e :
        err = str(e)
        print(f"Error! {err.title()}")
        return None
    
def multiplication(Operand_1, Operand_2):
    try:
        return Operand_1 * Operand_2
    except Exception as e :
        err = str(e)
        print(f"Error! {err.title()}")
        return None
    
def division(Operand_1, Operand_2):
    try:
        return Operand_1 / Operand_2
    except Exception as e :
        err = str(e)
        print(f"Error! {err.title()}")
        return None

def mod(Operand_1, Operand_2):
    try:
        return Operand_1 % Operand_2
    except Exception as e :
        err = str(e)
        print(f"Error! {err.title()}")
        return None

def power(Operand_1, Operand_2):
    try:
        return Operand_1 ** Operand_2
    except Exception as e:
        err = str(e)
        print(f"Error! {err.title()}")

def fact(Operand):
    try:
        if Operand == 1 or Operand == 0:  # Handle fact(0) case
            return 1
        else:
            return Operand * fact(Operand - 1)
    except Exception as e:
        err = str(e)
        print(f"Error! {err.title()}")

def fibonacci(Operand_1, Operand_2, Limit):
    try:
        fib_seq = [Operand_1, Operand_2]
        while Limit != 0:
            next_value = Operand_1 + Operand_2
            Operand_1 = Operand_2
            Operand_2 = next_value
            fib_seq.append(next_value)
            Limit -= 1
    
        return fib_seq
    except Exception as e:
        err = str(e)
        print(f"Error! {err.title()}")

def greatest_common_divisor(Operand_1, Operand_2):
    try:
        while Operand_2 != 0:
          Operand_1, Operand_2 = Operand_2, Operand_1 % Operand_2
        return Operand_1
    except Exception as e:
        err = str(e)
        print(f"Error! {err.title()}")

def decimal_to_fraction(Decimal_Value):
    try:
        decimal_str = str(Decimal_Value)      # Converting Decimal to a String to Handle Number Of Decimal Places.

        if '.' in decimal_str: # If Decimal Point '.' is encountered, i.e value is of 'Float' Type.
            decimal_places = len(decimal_str.split('.')[1]) #The 'decimal_str.split('.')[1]' line gives the fractional part after the decimal point.
            denominator = 10 ** decimal_places              #The 'len(decimal_str.split('.')[1])' line counts the number of digits in the fractional part.
            numerator = int(Decimal_Value * denominator)
        else: # No Decimal Point, i.e value is of 'Integer' Type.
            numerator = int(Decimal_Value)
            denominator = 1

        # Simplify the fraction
        divisor = greatest_common_divisor(numerator, denominator)
        numerator /= divisor
        denominator /= divisor
        return (f"{int(numerator)} / {int(denominator)}")
    except Exception as e:
        err = str(e)
        print(f"Error! {err.title()}")

def fraction_to_decimal(Fraction_Value):
    try:
        if '/' not in Fraction_Value:
            print("Syntax Error! '/' Not Found ")
            return None
        else:
            numerator = Fraction_Value.split('/')[0]
            denominator = Fraction_Value.split('/')[1]
            return (int(numerator) / int(denominator))
    except Exception as e:
        err = str(e)
        print(f"Error! {err.title()}")

def sine(Angle):
    try:
        radians = Angle * (3.141592653589793 / 180)
        radians = radians % (2 * 3.141592653589793)
        if radians > 3.141592653589793:
            radians -= 2 * 3.141592653589793
        return round((radians - (radians ** 3) / 6 + (radians ** 5) / 120 - (radians ** 7) / 5040),1)
    except Exception as e:
        err = str(e)
        print(f"Error! {err.title()}")

def cosine(Angle):
    try:
        radians = Angle * (3.141592653589793 / 180)
        radians = radians % (2 * 3.141592653589793)
        if radians > 3.141592653589793:
            radians -= 2 * 3.141592653589793
        return round((1 - (radians ** 2) / 2 + (radians ** 4) / 24 - (radians ** 6) / 720), 1) 
    except Exception as e:
        err = str(e)
        print(f"Error! {err.title()}")  

def tangent(Angle):
    try:
        sin_val = sine(Angle)
        cos_val = cosine(Angle)
        if cos_val == 0:
            return 'Not Defined'  
        return round(sin_val / cos_val, 1)
    except Exception as e:
        err = str(e)
        print(f"Error! {err.title()}")

def secant(Angle):
    try:
        cos_val = cosine(Angle)
        if cos_val == 0:
            return 'Not Defined'  
        return round(1/cos_val)
    except Exception as e:
        err = str(e)
        print(f"Error! {err.title()}")

def cosecant(Angle):
    try:
        sin_val = sine(Angle)
        if sin_val == 0:
            return 'Not Defined'  
        return round(1/sin_val)
    except Exception as e:
        err = str(e)
        print(f"Error! {err.title()}")

def cotangent(Angle):
    try:
        sin_val = sine(Angle)
        cos_val = cosine(Angle)
        if sin_val == 0:
            return 'Not Defined'  
        return round( cos_val / sin_val, 1)
    except Exception as e:
        err = str(e)
        print(f"Error! {err.title()}")  
    
#Calculator_Logic------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def arithmetic_calculator(previous_result = None):
    """
    A Simple Calculator that performs basic Arithmetic Operations: Addition, Subtraction,
    Multiplication, Division, and others.

    This Function prompts the User to Input two numeric values and choose an arithmetic
    operation. Based on the selected operation, it computes the result and displays it to the user.

    The Function Returns a List consisting of ["result","variables","operator"]:
        - "result" = Operation Result.
        - "variables" = List Of Variable_Values/Inputs.
        - "operator" = Operator for the Operation Expression.
    """
    operation = {
        '+': addition,
        '-': subtraction,
        '*': multiplication,
        '/': division,
        '%': mod,
        '^': power,
        '**': power,
        '!': fact,
        'd=>f':decimal_to_fraction,
        'f=>d':fraction_to_decimal,
        'fib': fibonacci,
        'gcd':greatest_common_divisor,
        'sin':sine,
        'cos':cosine,
        'tan':tangent,
        'sec':secant,
        'cosec':cosecant,
        'cot':cotangent
    }
    result = 0

        
    while True: #While Loop For Taking 'Operation_Input'
        operator = input("Choose Operation ( * | / | % | ^ | + | - | ! | GCD | Fib | F=>D | D=>F | Sin | Cos | Tan | Sec | Cosec | Cot ) or 'Exit' to Quit: ")
        if operator.lower() in ['exit','/e','e','quit','/q','q']:
            result = '@'
            break #Exit While Loop for 'Exit' Condition 
        elif operator.lower() in operation: # Exit While Loop for Valid__Operation
            break
        else:
            print("Not A Valid Operation :// Please Try Again : :")
            print(" ")

    if result == '@': #Exit Condition For 'Early_Exit'
        output = {"result": result, "variables": 0, "operator": 0}
        return output   
    else:
        #Getting List Of Parameters for a specific Operation:
        signature = inspect.signature(operation[operator.lower()])
        parameters = signature.parameters

        #Getting Valid Inputs For The Parameters in 'parameters'-------------------------------------------------------------------------------------------------------------------#
        inputs = {}

        for parameter in parameters: #'For' Loop for Iterating the 'parameters' List and taking Inputs for Each Parameter:
            while True: #Outer 'While' Loop for 'Re-initializing / Re-entering' Operand_Value if 'Invalid_Input' is Triggered
                if previous_result is not None and parameter in ['Operand','Operand_1','Angle','Fraction_Value','Decimal_Value']:
                    var = input(f"Use Previous Result: '{previous_result}' as Operand_1? (Y/N): ")
                    while True:
                        if var.lower() in ['yes', 'y']:
                            # Assign 'previous_result'
                            inputs[parameter] = int(previous_result) if operator == '!' else str(previous_result) if operator.lower() == 'f=>d' else previous_result
                            break  # Exit both inner and outer 'While' loops

                        elif var.lower() in ['no', 'n']:
                            while True:# Inner-Inner 'While' loop for entering a new valid value
                                var = input(f"Enter {parameter}: ")
                                try:
                                    # Convert Operand_Value based on the Operator_Type
                                    value = int(var) if operator == '!' else str(var) if operator.lower() == 'f=>d' else float(var)
                                    inputs[parameter] = value
                                    break  # Exit the Inner-Inner 'While' loop after valid input
                                except ValueError:
                                    print("Invalid Operand Value :// Please Try Again : : ")
                            break # Exit the Inner 'While' loop after valid input
                        
                        else:
                            print("Invalid Input :// Please Try Again : : ")
                            var = input(f"Use Previous Result: '{previous_result}' as Operand_1? (Y/N): ")
                    break # Exit the Outer 'While' Loop after valid 'Operand_1' value              
            
                var = input(f"Enter {parameter}: ")
                try:
                    value = int(var) if operator == '!' else str(var) if operator.lower() == 'f=>d' else float(var)
                    inputs[parameter] = value
                    break # Exit the Outer 'While' Loop after valid 'Operand_Value' 
                except ValueError:
                    print("Invalid Operand Value :// Please Try Again : : ")
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    result = operation[operator.lower()](**inputs)
    previous_result = result

    output = {"result": result, "variables": list(inputs.values()), "operator": operator}
    return output
        