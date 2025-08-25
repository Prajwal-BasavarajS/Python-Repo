def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage
n = int(input("Enter the value of n: "))
print("The", n, "th Fibonacci number is:", fibonacci(n))



d = 10
e = 11
f = d
d = e
e = f

# d , e = e , d

print(d, "       " , e )