# def , return , yeild , class , lambda 


# def - to define a function def fun_name(): 

def fun():
    print('Hello we are executing the function')

fun()


# class - it is used to declare user defined class 

class cat :
    sound = "meow"
    category = "carnivorous" 


# return statements 

# return : This keyword is used to return from the function.
# yield : This keyword is used like return statement but is used to return a generator.

# The 'return' keyword is used to return a final result from a function, and it exits the function immediately.  

# 'Yield'  -  is a keyword used to create Generator, it allows the function to yield/ return multiple values without exiting .
# Return gives back onlys one value n exits from the function but 'Yield' returns multiple values one at a time and keeps the function running.

print(" ")

def fin():
    print("inside fin function - returning s")
    s = 5
    return s 


print (fin())


# Yield 

print(' ')

print("YIELD")

def yfun():
    yield 1
    yield 7
    yield 23

for val in yfun():
    print(val)



print(" ")



def fun2(m):
    for i in range(m):
        yield i               

    # when return used instead of yield it gives error           
    #     for n in fun2(5):
#           TypeError: 'int' object is not iterable

# call the generator function
for n in fun2(5):
    print(n)


# lambda 

print(" ")

print(" lambda ")
 
# Lambda keyword is used to make inline returning functions with no statements allowed internally. 

# Lambda keyword
g = lambda x: x*x*x

print(g(7))

