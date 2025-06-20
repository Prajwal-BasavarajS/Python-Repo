# global: This keyword is used to define a variable inside the function to be of a global scope.

# non-local : This keyword works similar to the global, but rather than global, this keyword declares a 
# variable to point to variable of outside enclosing function, in case of nested functions.

# Global and nonlocal keyword uses in Python
# In this code, the 'global' keyword is used to declare global variables 'a' and 'b'. 
# Then, there's a function 'add' that adds these global variables and prints the result.

# The second part of the code demonstrates the 'nonlocal' keyword. The function fun contains a variable var1, 
# and within the nested function gun, we use nonlocal to indicate that we want to modify the var1 defined in the 
# outer function fun. It increments the value of var1and prints it.




a = 15
b = 10

def add():
  
    # Add global variables a and b
    c = a + b  
    print(c)

add()  # Output: 25

def fun():
  
  # Local variable in fun()
    var = 10  

    def gun():
      
        # Modify var1 in the enclosing scope (fun)
        nonlocal var  
        var += 10  
        print(var)  

    gun() 

fun() # Output: 20
