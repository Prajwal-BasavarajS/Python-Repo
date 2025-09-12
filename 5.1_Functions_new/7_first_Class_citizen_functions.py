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
    return f'hello {s}'

f = sum

print(f(5))



# Passing Functions as Arguments
# Functions can be passed as arguments to other functions, enabling higher-order functions.


