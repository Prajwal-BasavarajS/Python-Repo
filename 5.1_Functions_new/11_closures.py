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




def fun1(): 
    a = 45
    def fun2(): 
        nonlocal a 
        a=54
        print(a)
    fun2()
    print(a)
fun1()




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