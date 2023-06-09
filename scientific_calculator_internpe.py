# -*- coding: utf-8 -*-
"""scientific calculator internpe.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C4N788xfU_oQ3ptBXZmLdsrpoYV4jjur
"""

import math

def scientific_calculator():
    print("Scientific Calculator")
    print("--------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square root")
    print("6. Logarithm")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print("The result is: ", result)
    
    elif choice == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print("The result is: ", result)
    
    elif choice == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 * num2
        print("The result is: ", result)
    
    elif choice == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print("The result is: ", result)
    
    elif choice == 5:
        num = float(input("Enter a number: "))
        result = math.sqrt(num)
        print("The square root of", num, "is", result)
    
    elif choice == 6:
        num = float(input("Enter a number: "))
        result = math.log10(num)
        print("The logarithm of", num, "is", result)
    
    elif choice == 7:
        angle = float(input("Enter an angle in degrees: "))
        result = math.sin(math.radians(angle))
        print("The sine of", angle, "degrees is", result)
    
    elif choice == 8:
        angle = float(input("Enter an angle in degrees: "))
        result = math.cos(math.radians(angle))
        print("The cosine of", angle, "degrees is", result)
    
    elif choice == 9:
        angle = float(input("Enter an angle in degrees: "))
        result = math.tan(math.radians(angle))
        print("The tangent of", angle, "degrees is", result)
    
    elif choice == 10:
        exit()
    
    else:
        print("Invalid choice. Please try again.")
    
    print()
    scientific_calculator()
    
scientific_calculator()