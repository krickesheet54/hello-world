"""
Author: Kricketune54
Date: 7/21/2021
File Description: Converts an inputted score and prints out corresponding grade (pg.162 #2)"

"""

def main():

    num_score = eval(input("What grade did you receive on the quiz? "))
    
    scores = ["F", "F", "D", "C", "B", "A"]
        
    print("You got a", scores[num_score])

main()
