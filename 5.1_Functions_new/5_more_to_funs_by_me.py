# Rule 1 function can be assigned to variable
# Rule 2: Variable / data type assigned a function shld be able to pass the arguments 
# Rule 2: Variable / data type assigned a function shld be able to return / print the results from a function

name = "Prajwal Basavaraj"

print("Rule 1")

def display():
    print (f"Myself {name}, I am studing my masters in Data Science and completing by core basics in python!!")
    print("Nice to meet you")

a = display           # --> Rule 1

a()  


print("\nRule 2 ")


def add(n):
    sum = 0
    for i in range(n):
        sum+=i
    print(sum)


c = add    

c(10)    # --> Rule 2


print("\nRule 3 ")

def passing(num):
    if  num == 0 or num == 1:
        return 1
    else :
      return(num*(passing(num-1)))


b = passing        # Rule --> 3

print(b(5))
 
