a = 1


def f():
    print("f() : ",a)
    print("abve f uses global a value and prints the same as no val assigned for a in f() \n")

def g():
    a = 3 
    print("g():",a)
    print("here a is locally modified to a = 3 and global value is not touched only local val is altered")

def h():
    global a 
    a = 9
    print("h() : ", a)
    print("\n Here global var is called and modified so a = ",a)

print("Global a = ",a)
f()
print("Global a = ",a)
g()
print("Global a = ",a)
h()




class EmptyClass:
    pass  # No methods or attributes yet

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        pass  # Placeholder for greet method

# Creating an instance of the class
p = Person("Emily", 30)