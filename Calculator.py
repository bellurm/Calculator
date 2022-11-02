# blog-cyberworm.com
# calculator.py updated for the education in my web site.

import math

welcome = """
*****************************************************************************************
Welcome to the Cyber Worm's Calculator!
Our Operations:
99. Exit
1. Addition
2. Substraction
3. Multiplication
4. Division
5. Factorial
6. Exponentiation
7. Rooting
Note: If you want to see the operations list again, please enter this keyword: 'list'
*****************************************************************************************
"""
print(welcome)

operations = ["99", "1", "2", "3", "4", "5", "6", "7", "list"]

# Toplama işlemi
def addition():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print(f"{num1} + {num2} = {num1 + num2}")

# Çıkarma işlemi
def subtraction():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print(f"{num1} - {num2} = {num1 - num2}")

# Çarpma işlemi
def multiplication():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print(f"{num1} * {num2} = {num1 * num2}")

# Bölme işlemi
def division():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print(f"{num1} / {num2} = {num1 / num2}")

# Faktöriyel alma işlemi
def factorial(number):
    fact = math.factorial(number)
    print(f"{number}! = {fact}") # Örnek çıktı: 5! = 120

# Üs alma işlemi
def exponentiation():
    base = int(input("Number: "))           # taban
    exponent = int(input("Exponentiate: ")) # kuvvet (üst)
    expo = math.pow(base, exponent)
    print(f"Result: {expo}")

# Kök alma işlemi
def rooting(number):
    root = math.sqrt(number)
    print(f"The root of {number} is: {root}")

# 'hesapla' fonksiyonu. İşlemlerin ana merkezi burası olacak.
def calculate():
    while True:
        choice = str(input("\nSelect an operation's number from the menu: "))
        if choice == operations[0]:
            print("Have a nice day!")
            break
            
        elif choice == operations[-1]:
            print(welcome)
            
        elif choice == operations[1]:
            addition()
            
        elif choice == operations[2]:
            subtraction()
            
        elif choice == operations[3]:
            multiplication()
            
        elif choice == operations[4]:
            division()
            
        elif choice == operations[5]:
            factorial(number=int(input("Number: ")))
            
        elif choice == operations[6]:
            exponentiation()
            
        elif choice == operations[7]:
            rooting(number=int(input("Number: ")))
            
        else:
            print("[*] Invalid selection. To see the list, enter this keyword: 'list'.")

calculate()
