def display(n):
    while(n>9):
        n = n //10
    
    print(n) 
display(1098)



def firstDigit(n):
    #code here
    n1 = str(n)
    n1 = n1[::-1]
    n2 =n1[-1]
    n2 = int(n2)
    return n2

print(firstDigit(572))


def digit(num):
    s =str(num)
    print(s[0])

digit(92932)