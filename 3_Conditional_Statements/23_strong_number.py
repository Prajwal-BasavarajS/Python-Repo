def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_strong_number(N):
    original = N
    total = 0
    while N > 0:
        digit = N % 10
        total += factorial(digit)
        N //= 10
    return 1 if total == original else 0

# Example usage
N = 145
print(is_strong_number(N))

