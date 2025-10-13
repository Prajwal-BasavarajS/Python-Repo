def palin(s):
    e = len(s)
    half = e // 2 
    s1 = s[:half]
    s2 = s[half:]
    s2 =s2[::-1]
    if s1 == s2:
        print("symmetric")
    else :
        print("not symmetric")

    s1 = s[::-1]
    if s == s1 :
        print("palindrome")
    else :
        print("not palindrome")


palin("madam")
# palin("maddam")