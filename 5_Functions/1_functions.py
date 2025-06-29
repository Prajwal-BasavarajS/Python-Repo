# Python Functions is a block of statements that does a specific task. The idea is to put some commonly or
# repeatedly done task together and make a function so that instead of writing the same code again and again for 
# different inputs, we can do the function calls to reuse code contained in it over and over again.


# Types of Functions in Python

# Built-in library function: These are Standard functions in Python that are available to use.
# User-defined function: We can create our own functions based on our requirements.

def fun(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(fun(7))

print('\n')
# Types of Arguments in Functions

# Default Arguments
# keyword Agruments
# Positional Arguments
# Arbitary Arguments

#1: Calling functions without keyword arguments 

def student(firstname, lastname ='Mark', standard ='Fifth'):
     print(firstname, lastname, 'studies in', standard, 'Standard')

# 1 positional argument
student('John') 

# 3 positional arguments                         
student('John', 'Gates', 'Seventh')     

# 2 positional arguments  
student('John', 'Gates')                  
student('John', 'Seventh')


print()

# 1 keyword argument
student(firstname ='John')     

# 2 keyword arguments                 
student(firstname ='John', standard ='Seventh')  

# 2 keyword arguments 
student(lastname ='Gates', firstname ='John')



# mutable default argument values example using python list

# itemName is the name of the item that we want to add to list
# that is being passed, or if it is not passed then appending in 
# the default list

# def appendItem(itemName, itemList = []):
#     itemList.append(itemName)
#     return itemList


# print(appendItem('notebook'))
# print(appendItem('pencil'))
# print(appendItem('eraser'))



print()
def appenditem(itemNamee,listitem = []):
    listitem.append(itemNamee)
    return listitem


print(appenditem("Notebook"))
print(appenditem("classroom"))
print(appenditem('keyboard'))


def adddictitem(item,keynumbe,dict = {}):
    dict[keynumbe] = item
    return dict


print(adddictitem('notebook', 4))
print(adddictitem('pencil', 1))
print(adddictitem('eraser', 1))