a = True
b = False

print (a and b)
# True and True = true 
# True and false = false in AND keyword

print(a or b )
# any one is ture then o/p is true

print(not a)
# inverts the value of a  = False

c = 5 
d = [6,7,9,5,8,19]

if c in d:
    print("hello")
else : 
    print("fuck off")


if "J" in "Jaggu":
    print("Truee")
else : 
    print("false")


e = [1,2,3,4,5,6]
f = e
g =  [1,2,3,4,5,6]

if e is g :
    print("Both are same")
else :
    print('in e is g though the variables are same they are getting compared to the address in memory not the values')

if e == g :
    print ('here e==g values are getting compared so ans is True')
