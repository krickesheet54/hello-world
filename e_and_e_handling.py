"""
Author: Kricketune54
Date: 2/16/2022
File Description: Practice accepting an integer input, and using try, except, 
and else to handle incorrect input exceptions
"""

def ask():
    while True:
        try:
            result = int(input("Please provide an integer: "))
        except:
            print("Oops!  Not an integer")
            continue
        else:
            print("Thanks chief!")
            break
