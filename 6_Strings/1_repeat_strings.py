# Whooaah! Your are now familiar with String slicing. Let's have one more question to make it crystal 
# clear for you with some conditional statements.

# Given two strings a and b. The task is to make a new string where the string with longer length 
# should be in between and the one with shorter length should be outside on front and end. 
# New string should be like shorter+longer+shorter.



def program(s,r):
    if len(s)>len(r):
        return r+s+r   
    if len(r)>len(s):
        return s+r+s


print(program("hiii","theree"))