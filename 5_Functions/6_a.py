def print_numbers(n, current=1):
    if current > n:
        return
    print(current, end=" ")
    print_numbers(n, current + 1)

# Example usage:
n = int(input())
print_numbers(n)
