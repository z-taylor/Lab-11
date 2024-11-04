# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab11A.py
def allMath(num1, num2):
    addition = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2
    divide   = (num1/num2) if num2!=0 else None
    floorDiv = (num1//num2) if num2!=0 else None
    modulus  = (num1%num2) if num2!=0 else None
    power    = num1 ** num2 
    return addition, subtract, multiply, divide, floorDiv, modulus, power
input1 = int(input("Enter your first number: "))
input2 = int(input("Enter your second number: "))
print(f"Your resulting tuple is {allMath(input1, input2)}")