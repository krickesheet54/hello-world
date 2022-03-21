"""
Author: Krickesheet54
Date: 6/25/2020
File Description: Calculates cost of the order (Chapter 3, Question 5)

"""

coffee = eval(input("How many pounds of coffee to order? "))

shipping_cost = 1.50 + (coffee * .86)

coffee_cost = shipping_cost + (coffee * 10.50)

print("The total cost of this order is", round(coffee_cost, 2), "dollars.")
