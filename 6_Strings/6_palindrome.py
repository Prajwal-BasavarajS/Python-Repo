def palindrome(s):
    s = s.lower()
    r = s[::-1]
    if r == s:
        print("true plaindrome")
    else:
        print("false")

palindrome("Tenet") 