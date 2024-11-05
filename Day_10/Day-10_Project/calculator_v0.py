def arithmetic_calculator():
        """
        A Simple Calculator that performs basic Arithmetic Operations: Addition, Subtraction,
        Multiplication, and Division.

        This Function prompts the User to Input two numeric values and choose an arithmetic
        operation. Based on the selected operation, it computes the result and displays it to the user.

        The Function Returns a List consisting of ["result","var_1","var_2","operator"].
        """
        operator = input("Choose Operation ( * | / | % | ^ | + | - ): ")

        while True:
            if operator in ['*', '/', '%', '^', '+', '-']:
                var_1 = float(input('Enter The First Operand: '))
                var_2 = float(input('Enter The Second Operand: '))
                break
            else:
                print("Not A Valid Input :// Please Try Again : :")
                operator = input("Choose Operation ( * | / | % | ^ | + | - ): ")

        result = 0
        if operator == '*':
            result = var_1 * var_2
        elif operator == '/':
            if var_2 == 0:
                print('Division By 0 is Prohibited!')
            else:
                result = var_1 / var_2
        elif operator == '%':
            if var_2 == 0:
                print('Division By 0 is Prohibited!')
            else:
                result = var_1 % var_2
        elif operator == '^':
            result = pow(var_1,var_2)
        elif operator == '+':
            result = var_1 + var_2
        elif operator == '-':
            result = var_1 - var_2
        elif operator == '-':
            result = var_1 - var_2
        else:
            result = 0
        
        if result == 0:
            return None
        else:
            output = {"result" : result, "var_1" : var_1, "var_2" : var_2, "operator" : operator}
            return output
