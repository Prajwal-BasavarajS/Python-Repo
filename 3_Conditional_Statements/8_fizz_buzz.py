
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