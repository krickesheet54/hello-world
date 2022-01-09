def palindrome(s):
    x = s[::-1]
    if x == s:
        return True
    elif x !=s:
        return False
