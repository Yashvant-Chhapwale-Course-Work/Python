def arithmetic_calculator():
    """
    A Simple Calculator that evaluates Mathematical Expressions.
    This Function prompts the User to Input a Mathematical Expression and Returns a result using the 'eval()' Function.

    The Function Returns a List consisting of ["result","equation"].
    """

    equation = input("Enter The Equation: ")

    result = eval(equation)
    
    output = {"result":result,"equation":equation}
    return output

