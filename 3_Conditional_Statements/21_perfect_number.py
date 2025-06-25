def is_perfect_number(n):
    if n <= 1:
        return False

    sum_of_factors = 0

    # Loop from 1 to n//2 to find proper divisors
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_of_factors += i

    return sum_of_factors == n

# Example usage:
n1 = 6
n2 = 10
print(is_perfect_number(n1))  # Output: True
print(is_perfect_number(n2))  # Output: False
