def operators(op,a,b):
    match op:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case _:
            return "Invalid_Input"
        
op = input("enter operators \n ")
print(operators(op,3,5))
        