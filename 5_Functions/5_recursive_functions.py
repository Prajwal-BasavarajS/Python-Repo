# recusrive functions

def fact (n):
    if n == 0 :
        print("zero")
        return 1
    # if n == 1 :
    #     print("one")
    #     return 1
    
    return n * fact(n-1)


print(fact(1))