
def fizzbuzz(a):
    
    if( a % 3 == 0 and a % 5 == 0 )  :
        print(" FizzBuzz ")
    elif ( a % 5 == 0 ):
        print("Buzz")    
    elif ( a % 3 == 0 ) :
        print("Fizz")
    else: 
        print(f"{a} is not fizz or buzz")

        
a = int(input("Enter a number\n"))
fizzbuzz(a)


def fizzbuzz(n):
        

    if (n % 3 == 0 and n % 5 == 0) : 
        return "fizzbuzz"
    elif n % 3 == 0 :
        return  "buzz"
    elif n % 5 == 0 :
        return "fizz"
    else :
        return "not a fizzbuzz number"
    


n = int(input("Enter a number "))

print(fizzbuzz(n))
