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
