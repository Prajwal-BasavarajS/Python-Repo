def greatest_number(a,b,c):
    if(a > b and a > c) :
        return "A greatest"
    elif( b > a and b > c ):
        return "B greatest"
    else :
        return "c is greatest"
    

a = int(input())
b = int(input())
c = int(input())

# res = greatest_number(a,b,c)
# print(res)

print(greatest_number(a,b,c))
