
#  To create closure 1st need to define a funtion then, define another function inside the 1st function and 
# then return the second function 


def add(t):
    def combine(p):
        return t + "doesn't like " + p 
    return combine

love = add("Macbook ")

i = love("Charging")
print(i)

print(love.__closure__[0].cell_contents, "Closure \n")



def make_multi(x):
    def multi(y):
        return x * y
    return multi

multiplication = make_multi(7)
second_multi = make_multi(8)

print(multiplication(2))
print(second_multi(3))


print(f"\n closure at multiplication is {multiplication.__closure__[0].cell_contents}")
print(f"\n Closure at second_multi = {second_multi.__closure__[0].cell_contents}")

