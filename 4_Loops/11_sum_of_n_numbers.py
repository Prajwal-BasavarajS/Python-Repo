def findSum(n):
    sum = 0
    x = 1
    
    # Iterating over all the numbers between 1 to n
    while x <= n:
        sum = sum + x
        x = x + 1
    return sum

if __name__ == "__main__":
    n = 5
    print(findSum(n))


def sum_of_n(n):
    return n * (n+1)//2

print(sum_of_n(8))