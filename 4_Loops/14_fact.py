def facttorial(n):
    fact =1
    for i in range(1,n+1):
        fact = fact * i
    return(fact)



n = int(input("Enter a number"))

print(facttorial(n))



# recursion 

print("Recursive Function \n ")


def factof(n):
    if n == 0 or n == 1 :
        return 1
    else :
        return n * factof(n-1)
    
print(factof(n))
