def fibonacci(n):
    a = 0 
    b = 1  
    if n == 0 :
            print('0')
    elif n ==1:
            print('1')
   
    for i in range(2,n+1):
        a,b =b, a + b 
    return b

n = 6
print(fibonacci(n))

print("recursive function answer  = " , end = " ")
def fibonacci1(n):

    # print("called")
    if n == 0 :
            return 0
    elif n == 1 :
          return 1
    else :
          return fibonacci1(n-1) + fibonacci1(n-2)  
    

print(fibonacci1(n))