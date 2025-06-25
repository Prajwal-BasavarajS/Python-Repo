# if , elif, else

x = int(input("Enter a number"))

if x > 0:
    print('Positive number')
elif x < 0 :
    print('Negative Number')
else :
    print ("ZOROO DAAA!!! ")

a , b , c  = map(int,input().split()) 
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
# a, b, c = int(input().split())
# You're trying to convert the result of input().split() directly into an int, but input().split() returns a list of strings, not a single value.

if a >= b & b >= c:
    print("A is largest")
elif b >= a & b >= c :
    print("B is largest")
else :
    print('c is largest')


