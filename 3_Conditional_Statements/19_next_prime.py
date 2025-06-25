def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(n):
    candidate = n + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1

# Example usage
n = 15
print("First prime number greater than", n, "is:", next_prime(n))
