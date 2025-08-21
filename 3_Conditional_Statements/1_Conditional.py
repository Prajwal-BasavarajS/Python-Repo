# if 
age = 19

if age >= 18 :
    print("elegible to vote")


# short hand if 
wage = 22
if wage >= 21 : print(" girls can marry ")


# elif 

if age >= 20 :
    print("Allowed inside the PUB!! ")
elif age <= 19 :
    print("Use brains and edit the AADHAR card ")
else :
    print("Not allowed inside the PUB!! BYE BYE!! ")

def posneg():


    n = int(input())
    if n > 0 :
        return ("positive..")
    elif n < 0 :
        return ("negative..")
    else : 
        return "its zeroo.."
    

print(posneg())