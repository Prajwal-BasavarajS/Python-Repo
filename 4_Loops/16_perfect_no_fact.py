def is_perfect_number(n):
    if n < 1:
        return False
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum == n

# Test the function
num = int(input("Enter a number: "))
if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")


def generate_perfect_numbers(limit):
    for num in range(2, limit + 1):
        if is_perfect_number(num):
            print(num)

generate_perfect_numbers(10000)



def perfect_no(n):
    res = 0
    for i in range(1,n):
        if(n%i==0):
            res+= i
    
    if(res == n ):
        print(f"{n}Perfect Number")
    else:
        print('not a perfect number')
    
n = int(input("enter any number from above \n"))
perfect_no(n)

