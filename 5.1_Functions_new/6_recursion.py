# Recursion is a programming technique where a function calls itself either directly or indirectly 
# to solve a problem by breaking it into smaller, simpler subproblems.

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1)

print(factorial(5))


def fibo(s):
    if s == 0:
        return 1
    elif s == 1:
        return 1
    else :
        return fibo(s-1)+fibo(s-2)
    
print(fibo(10))

# Tail Recursion: The recursive call is the last thing the function does, so nothing happens after it returns. 
                    #Some languages can optimize this to work like a loop, saving memory.

# Non-Tail Recursion: The function does more work after the recursive call returns, so it can’t be optimized into a loop.


def tail_fact(n, acc=1):
    # Base case
    if n == 0:
        return acc
    # Tail recursive call with an accumulator
    else:
        return tail_fact(n-1, acc * n)

def nontail_fact(n):
    # Base case
    if n == 1:
        return 1
    # Non-tail recursive call because the multiplication happens after the call
    else:
        return n * nontail_fact(n-1)

# Example usage
print(tail_fact(5))  
print(nontail_fact(5))