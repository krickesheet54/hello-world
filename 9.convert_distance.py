"""
Author: Bernie Garwig
Date: 4/7/2020
File Description: Challenge #9: A program converting kilometers to miles
"""

def main():
    print("The program will convert distance from metric to imperial!")
    kilometers = eval(input("What is the distance? " ))
    miles = kilometers * 0.62

    print("The imperial distance is", miles, "miles!" )

main()
