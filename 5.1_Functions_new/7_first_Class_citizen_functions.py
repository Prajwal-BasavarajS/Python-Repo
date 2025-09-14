#   Rules of Functions

# Assigning Functions to Variables

def msg(name):
    return f"Hello, {name}!"

# Assigning the function to a variable
f = msg

# Calling the function using the variable
print(f("Emma"))


a= 10 

def sum(n):
    s= a+n
    return f'{s}'

f = sum

print(f(5))



# Passing Functions as Arguments
# Functions can be passed as arguments to other functions, enabling higher-order functions.



def sum(calling_first_function,x):    # here sum(calling_first_function,x)          ccalling_first_function. ==   executes_first and  x ===     return calling_first_function(x)
    return calling_first_function(x)            # calling_first_function = executes_first and it calls the down function and executes 1st  


def executes_first(d):
    return d+10                     # gets value of d from above where d = x  and x = 20

print(sum(executes_first,20))           # 1st line which gets executed  (sum(executes_first,20))  


print("I am not part of below")



def apply(func, x): # higher order function
    return func(x)

def square(n): # function to be passed
    return n * n

print(apply(square, 5))

print("\nI am now a part \n")

def name(x,y):
    return(x(y))

def d(w):
    return w+w

print(name(d,3))


# 3. Returning Functions from Other Functions

def fun1(msg):
    def fun2():
        return f"Message: {msg}"
    return fun2

# Getting the inner function
func = fun1("Hello, World!")
print(func())




