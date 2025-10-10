x = 3
print(type(x))



def add(t):
    def combine(p):
        return t + "doesn't like " + p 
    return combine

love = add("Macbook ")

i = love("Charging")
print(i)

print(love.__closure__[0].cell_contents, "Closure \n")
