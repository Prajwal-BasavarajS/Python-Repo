# we normally use def keyword to define any functions...
# Lambda is also used to define a function but anonymously


def cube(x): 
    return x*x*x   # without lambda

cube_l = lambda x : x*x*x  # with lambda

print(cube(7))
print(cube_l(7))


print()
s = "hello everyone!!"

s2 = lambda s3 : s3.upper()

print(s2(s))

print()

n = lambda x: "Positive" if x > 0  else ('zero'  if x == 0  else 'negative' )
    
print(n(-9))
print(n(18))
print(n(0))    

print()

