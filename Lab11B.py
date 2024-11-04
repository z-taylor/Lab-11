# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab11B.py
def letterPositions(string, letter):
    list = []
    for position, letter_ in enumerate(string):
        if letter==letter_:
            list.append(position)
    indexTuple = tuple(list)
    return indexTuple

stringInput = input("Enter your phrase: ").lower()
letterInput = input("Enter a letter: ").lower()
print(f"{letterInput} appears inside your phrase in the following positions: {letterPositions(stringInput, letterInput)}")