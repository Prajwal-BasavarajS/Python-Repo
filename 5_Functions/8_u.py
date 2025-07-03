def first_digit(n):
    n = abs(n)  # Ensure it's positive
    while n >= 10:
        n = n // 10
    return n

# Example usage:
n = int(input())
print(first_digit(n))
