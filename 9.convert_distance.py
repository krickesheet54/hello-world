"""
Author: Kricketune54
Date: 4/7/2020
File Description: Challenge #9: A program converting kilometers to miles
John Zelle an Introduction to Computer Science Chapter 2 Challenge Problems

"""

def main():
    print("The program will convert distance from metric to imperial!")
    kilometers = eval(input("What is the distance? " ))
    miles = kilometers * 0.62

    print("The imperial distance is", miles, "miles!" )

main()
