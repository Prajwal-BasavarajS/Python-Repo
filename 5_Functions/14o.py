def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

def power_of_number(n, r):
    return pow(n, r)

# Example usage:
n = int(input())
r = reverse_number(n)
print(power_of_number(n, r))
