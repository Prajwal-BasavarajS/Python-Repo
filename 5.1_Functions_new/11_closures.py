def outer_function(x):
    # Outer function: takes 'x' and defines inner_function
    def inner_function(y):
        return x + y  # 'x' is remembered from outer_function
    return inner_function  # Returns inner function (closure)

# Create a closure with x = 10
closure = outer_function(10)

# Call the closure with different values of 'y'
print(closure(5)) 
print(closure(20))














a =43

def fun1(): 
    a = 45
    def fun2(): 
        
        a=54
        print(a)
    fun2()
    print(a)
fun1()
print(a)



a = "I am global"

def outer():
    b = "I am enclosing"
    
    def inner():
        global a
        nonlocal b
        a = "Modified global"
        b = "Modified enclosing"
    
    inner()
    print("Inside outer:", b)
    
outer()
print("Outside outer:", a)






def make_multiplier(factor):
    def multiply_by(x):
        return x * factor
    return multiply_by


x = 4
y = int(input())
double = make_multiplier(x)

print(f"{double(y)}, {x}*{y}") 
print(double(10)) 


def add(h):
    def sub(i):
        return h + " " + i
    return sub

strr = add("hello")
print(strr("world"))


# Check closure variables
print(strr.__closure__[0].cell_contents,"closure")



def addition(o):
    def multiply(v):
        p = 5
        return o * p + v
    return multiply


clos = addition(10)
# clos = addition(20)
trip = addition(20)

print(clos(5))
print(trip(10))

print(clos.__closure__[0].cell_contents)
print(trip.__closure__[0].cell_contents)

