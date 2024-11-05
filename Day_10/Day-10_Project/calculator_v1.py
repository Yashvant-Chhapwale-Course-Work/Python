import inspect

def addition(Operand_1, Operand_2):
    return Operand_1 + Operand_2

def subtraction(Operand_1, Operand_2):
    return Operand_1 - Operand_2

def multiplication(Operand_1, Operand_2):
    return Operand_1 * Operand_2

def division(Operand_1, Operand_2):
    if Operand_2 == 0:
        print("Division by 0 is Prohibited!")
        return None
    else:
        return Operand_1 / Operand_2

def mod(Operand_1, Operand_2):
    if Operand_2 == 0:
        print("Division by 0 is Prohibited!")
        return None
    else:
        return Operand_1 % Operand_2

def power(Operand_1, Operand_2):
    return Operand_1 ** Operand_2

def fact(Operand_1):
    if Operand_1 == 1 or Operand_1 == 0:  # Handle fact(0) case
        return 1
    else:
        return Operand_1 * fact(Operand_1 - 1)

def fibonacci(Operand_1, Operand_2, Limit):
    fib_seq = [Operand_1, Operand_2]
    while Limit != 0:
        next_value = Operand_1 + Operand_2
        Operand_1 = Operand_2
        Operand_2 = next_value
        fib_seq.append(next_value)
        Limit -= 1
    
    return fib_seq

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
        'fib': fibonacci
    }
    result = 0

    while True:
        
        while True:
            operator = input("Choose Operation ( * | / | % | ^ | + | - | ! | fib ) or 'Exit' to Quit: ")
            if operator.lower() in ['exit','/e','e','quit','/q','q']:
                result = '@'
                break
            elif operator in operation:
                break
            else:
                print("Not A Valid Operation :// Please Try Again : :")
                print(" ")

        if result == '@':
            break

        signature = inspect.signature(operation[operator])
        parameters = signature.parameters

        inputs = {}
        for parameter in parameters:

            while True:
                if previous_result is not None and parameter == 'Operand_1':
                    var = input(f"Use Previous Result: '{previous_result}' as Operand_1? (Y/N): ")
                    while True:
                        if var.lower() in ['yes','y']:
                            if operator == '!':
                                inputs[parameter] = int(previous_result)
                            else:
                                inputs[parameter] = previous_result
                            break
                        elif var.lower() in ['no','n']:
                            var = input(f"Enter {parameter}: ")
                            if operator == '!':
                                 value = int(var)
                            else:
                                value = float(var)
                            inputs[parameter] = value
                            break
                        else:
                            print("Invalid Input :// Please Try Again : : ")
                            print(" ")
                            var = input(f"Use Previous Result: '{previous_result}' as Operand_1? (Y/N): ")
                    break                
            
                var = input(f"Enter {parameter}: ")
                try:
                    if operator == '!':
                        value = int(var)
                    else:
                        value = float(var)
                    inputs[parameter] = value
                    break
                except ValueError:
                    print("Invalid Operand Value :// Please Try Again : : ")

        result = operation[operator](**inputs)
        previous_result = result
        break

    if result == '@':
        output = {"result": result, "variables": 0, "operator": 0}
        return output   
    else:
        output = {"result": result, "variables": list(inputs.values()), "operator": operator}
        return output
