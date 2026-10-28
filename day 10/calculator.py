#calculator 

#add
def add(n1, n2):
    return n1 + n2
#subtract
def subtract(n1, n2):
    return n1 - n2
#multiply
def multiply(n1, n2):
    return n1 * n2
#divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

logo = r"""
   ❄                                       ❄
        *       .        *        .
   .        ❄       .         ❄         *

   ███████╗███╗   ██╗ ██████╗ ██╗    ██╗
   ██╔════╝████╗  ██║██╔═══██╗██║    ██║
   ███████╗██╔██╗ ██║██║   ██║██║ █╗ ██║
   ╚════██║██║╚██╗██║██║   ██║██║███╗██║
   ███████║██║ ╚████║╚██████╔╝╚███╔███╔╝
   ╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝

     C A L C U L A T O R   ❄   V 1.0

   +-----------------------------------+
   |  _______________________________  |
   | |                         0.00  | |
   | |_______________________________| |
   |                                   |
   |   [ 7 ]   [ 8 ]   [ 9 ]   [ / ]   |
   |                                   |
   |   [ 4 ]   [ 5 ]   [ 6 ]   [ * ]   |
   |                                   |
   |   [ 1 ]   [ 2 ]   [ 3 ]   [ - ]   |
   |                                   |
   |   [ C ]   [ 0 ]   [ = ]   [ + ]   |
   |                                   |
   +-----------------------------------+

       *  Keep Calm & Calculate  *

   ❄         Made with Python         ❄
"""
def calculator():
    print(logo)
    num1 = float(input("whats the first number? :"))

    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation :")
        num2 = float(input("whats the next number? :"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation :") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
    