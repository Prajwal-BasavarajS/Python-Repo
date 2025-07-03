def print_gfg(n):
    if n == 0:
        return
    print("GFG", end=" ")
    print_gfg(n - 1)

# Example usage:
n = int(input())
print_gfg(n)
