# Context Keywords: With, as Keyword in Python
# with Keyword in Python
# with keyword is used to wrap the execution of block of code within methods defined by context manager. 
# This keyword is not used much in day to day programming.

# This code demonstrates how to use the with statement to open a file named 'file_path' in write mode ('w'). 
# It writes the text 'hello world !'to the file and automatically handles the opening and closing of the
# file. with statement is used for better resource management and ensures that the file is properly closed after the block is executed.




# using with statement'


with open('file_path', 'w') as file:
    file.write('hello world !')



# as Keyword In Python
# as keyword is used to create the alias for the module imported. i.e giving a new name to the imported module. 
# E.g import math as mymath.

# This code uses the Python math module, which has been imported with the alias gfg. It calculates and prints the factorial of 5. 
# The math.factorial() function is used to calculate the factorial of a number, and in this case, it calculates the factorial of 5, which is 120.




import math as gfg

print(gfg.factorial(5))

