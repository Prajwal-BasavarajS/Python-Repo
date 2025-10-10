
# Local(L): Defined inside function/class
# Enclosed(E): Defined inside enclosing functions(Nested function concept)
# Global(G): Defined at the uppermost level
# Built-in(B): Reserved names in Python builtin modules



print(""" \n
      How the order or variable called takes place 
      1st looks in local scope 
      2nd If no var in local scope then in any outer functions or above enclosed functions 
      3rd If nothing is declared in inner function or outer functions then final its going to 
      get reference of the variable in global scope""")


print(" \n Local Scope\n")

pi = "global variable 3.14"

def outer():
    pi = "outer function 3.14"
    def inner():
        pi = "inner function variable 3.14"
        print(pi)
    inner()

outer()

print(" \n Outer / Enclosed Scope \n")


pi = "global variable 3.14"

def outer():
    pi = "outer function 3.14"
    def inner():
        # pi = "inner function variable 3.14"
        nonlocal pi
        print(pi)
    inner()

outer()


print("\n Printing Global variable\n")


pi = "global variable 3.14"

def outer():
    # pi = "outer function 3.14"
    def inner():
        # pi = "inner function variable 3.14"
        # nonlocal pi
        print(pi)
    inner()

outer()

print("\n Built In function \n")

from math import pi 
# pi = 'global pi variable'

def outer():
    # pi = 'outer pi variable'
    def inner():
        # pi = 'inner pi variable'
        print(pi)
    inner()

outer()


# LEGB = LOCAL ENCLOSED GLOBAL BUILT IT