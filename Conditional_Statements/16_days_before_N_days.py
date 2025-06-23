def day_before(d, n):
    return (d - n) % 7

# Example usage
d = 3  # Wednesday
n = 4
result = day_before(d, n)
print("Index of the day", n, "days before day", d, "is:", result)
