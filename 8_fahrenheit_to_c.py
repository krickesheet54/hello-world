"""
Author: Kricketune54
Date: 4/5/2020
File Description: Chapter 2 Challenge #8 of John Zelle book, does the reverse of convert.py
"""
def main():
    print("This program will convert Fahrenheit temperatures to Celsius!")
    fahrenheit = eval(input("What is the Fahrenheit temperature? " ))
    #Note that having eval is what allows the numbers to caculate from the user's input
    celsius = (fahrenheit - 32) / 9/5
    print("The temperature is", celsius, "degrees Celsius.")


main()


#refer to pseudocode for a guide on the structure of this program!
