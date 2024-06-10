def print_logo():
   logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
   print(logo)

def add(num1, num2):
    return num1 + num2

def subtract(num1 , num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
 num1 = float(input("What is the first number? : "))

 for Symbol in operations:
    print(Symbol)
 Should_continue = True
 while Should_continue:
  operation_symbol = input("Pick an operation from the line above: ")
  num2 = float(input("What is the next number? : "))
  calculation_function = operations[operation_symbol]
  fanswer = calculation_function(num1,num2)
  print(f"{num1} {operation_symbol} {num2} = {fanswer} ")
  Continue = input(f"Type 'y' to continue calculating with {fanswer} or type 'n' to exit ").lower()

  if Continue == "y":
    num1 = fanswer
  else:
    Should_continue = False
    calculator()

print_logo()
calculator()