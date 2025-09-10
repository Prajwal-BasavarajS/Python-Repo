# functions are block of statements that does a specific task

def odd_or_even(x):
    if x % 2 == 0:
        return "EVEN"
    else :
        return "odd"

# x = int(input("enter a number"))
res = odd_or_even(9)                        # function calling
print(res)


#  Types of Arguments in Py

#  1. Default Arguments 
        #  Are the arguments which assign a own value to their variable if not assigned nothing

def  sample_fun (y,z=9):
    print(f" y =  {y}")
    print(f"""('Here z is the default argumrnt because we are directly assigning the value to z like default') 
          z  =  {z}""")

sample_fun(10)

#  2. Keyword Arguments 
        # Are the arguments where the values are assigned using the var_names , keywords order does'nt matter

def ky_args(fname,lname):
    print(f"My name is {fname}")
    print(f"My last name is {lname}") 

ky_args(lname = 'Basavaraj', fname = "Prajwal") 

#  3. Positional Arguments 
    #  Are the arguments where the values are called based on their position 1st arg first called 

def pos_args(name,age):
    print("I am ", name)
    print(f"I am {age} years old")

pos_args("Amith",23)
print("Difference \n")
pos_args(23,"amith")


# 4. Arbitary Keywords Arguments
    #   *args  -> Non-Keyword Argument 
    #           THE *args is a special type of argument call where is allows to accept N number of positional keyword arguments in a function.
    #           The  *args is considered a tuple or the items assigned is considered tuple and we can call the run a loop or perform built-in tasks on it 
    #           These arguments are collected into a tuple, which means we can loop through them or use them with built-in functions.


def myFun(*argss):
    for arg in argss:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')  


def non_pos_args(*a):
    res = 1
    for i in a:
        res = i * res
    print(res)
    return sum(a)
        
print(non_pos_args(5,3,2))

#  5. Keyword Arguments 
    #   The special syntax **kwargs allows us to pass any number of keyword arguments (arguments in the form key=value). 
    #   These arguments are collected into a dictionary, where:

    # Keys = argument names
    # Values = argument values

def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, "=", val)

fun(s1='Python', s2='is', s3='Awesome')



#  Using both *Args and **kwargs

def both(*args,**kwargs):
    print("Subjects : ", args)
    print("Students : ", kwargs )

both("english", "math","kannada","data science", roll_no_1 =  "AMith ",rol_no_2=" bharath")

# 6 . Pass by Reference and Pass by Value


# If you pass an immutable object (like int, float, str, tuple):
# You can’t change it in place.
# So it looks like pass by value.
# If you pass a mutable object (like list, dict, set):
# You can modify it inside the function.
# So it looks like pass by reference.
def modify_num(x):
    x = x + 10
    print("Inside:", x)

a = 5
modify_num(a)
print("Outside:", a)

def modify_list(lst):
    lst.append(100)
    print("Inside:", lst)

mylist = [1, 2, 3]
modify_list(mylist)
print("Outside:", mylist)

print('''Python always passes references,     
        but whether you see changes or not depends on whether the object is mutable or immutable.''')


#  7. Recursive Functions

fact = 1

for i in range(1,6):
    fact = fact * i

print(fact)

def fact(n):
    if n == 0 or n ==  1 :
        return 1
    else :
       return (n*fact(n-1))
    
ress = fact(5)

print("Fact = ",ress)