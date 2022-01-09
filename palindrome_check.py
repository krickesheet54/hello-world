def palindrome(s):
    # Remove spaces
    s = s.replace(' ','')
    
    # Check if palindrome, return False if not
    return s == [::-1]
