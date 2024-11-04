def arithmetic_calculator():
        """
        A Simple Calculator that performs basic Arithmetic Operations: Addition, Subtraction,
        Multiplication, and Division.

        This Function prompts the User to Input two numeric values and choose an arithmetic
        operation. Based on the selected operation, it computes the result and displays it to the user.
        """
        operation = input("Choose Operation ( * | / | % | ^ | + | - ): ")

        while True:
            if operation in ['*', '/', '%', '^', '+', '-']:
                var_1 = int(input('Enter The First Operand: '))
                var_2 = int(input('Enter The Second Operand: '))
                break
            else:
                print("Not A Valid Input :// Please Try Again : :")
                operation = input("Choose Operation ( * | / | % | ^ | + | - ): ")

        result = 0
        if operation == '*':
            result = var_1 * var_2
        elif operation == '/':
            if var_2 == 0:
                print('Division By 0 is Prohibited!')
            else:
                result = var_1 / var_2
        elif operation == '%':
            if var_2 == 0:
                print('Division By 0 is Prohibited!')
            else:
                result = var_1 % var_2
        elif operation == '^':
            result = pow(var_1,var_2)
        elif operation == '+':
            result = var_1 + var_2
        elif operation == '-':
            result = var_1 - var_2
        elif operation == '-':
            result = var_1 - var_2
        else:
            result = 0
        
        if result == 0:
            return None
        else:
            output = {"result" : result, "var_1" : var_1, "var_2" : var_2, "operation" : operation}
            return output
