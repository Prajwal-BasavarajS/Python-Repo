def reverse_number(num):
    return int(str(num)[::-1])

def is_adam_number(N):
    reversed_N = reverse_number(N)
    square_N = N ** 2
    square_reversed_N = reversed_N ** 2
    reversed_square_N = reverse_number(square_N)
    
    return reversed_square_N == square_reversed_N

# Example usage:
N = 12
if is_adam_number(N):
    print("YES")
else:
    print("NO")

