import math

welcome = """
*****************************************************************************************
Welcome to Calculator!
Our Operations:
0. Exit
1. Addition
2. Substraction
3. Multiplication
4. Division
5. Factorial
6. Exponentiation
7. Rooting

Note: If you want to see the operation's list again, please enter this keyword: 'list'
*****************************************************************************************
"""
print(welcome)

operations = ["0", "1", "2", "3", "4", "5", "6", "7", "list"]

def addition():
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    add = num1 + num2
    print(num1, "+", num2, "=", add)

def subtraction():
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    sub = num1 - num2
    print(num1, "-", num2, "=", sub)

def multiplication():
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    mul = num1 * num2
    print(num1, "*", num2, "=", mul)

def division():
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    div = num1 / num2
    print(num1, "/", num2, "=", div)

def factorial():
    number = int(input("Number: "))
    fact = math.factorial(number)
    print(f"{number}! = {fact}")

def exponentiation():
    num1 = int(input("Number: "))
    num2 = int(input("Exponentiate: "))
    expo = math.pow(num1, num2)
    print("Result: ", expo)

def rooting():
    number = int(input("Number: "))
    root = math.sqrt(number)
    print(f"The root of {number} is: {root}")

def calculate():
    while True:
        op = str(input("\nSelect an operation's number from the menu: "))
        if op == operations[0]:
            print("Have a nice day!")
            break
        elif op == operations[-1]:
            print(welcome)
        elif op == operations[1]:
            addition()
        elif op == operations[2]:
            subtraction()
        elif op == operations[3]:
            multiplication()
        elif op == operations[4]:
            division()
        elif op == operations[5]:
            factorial()
        elif op == operations[6]:
            exponentiation()
        elif op == operations[7]:
            rooting()
        else:
            print("[*] Invalid selection. Enter 'list' to see the list.")
calculate()
