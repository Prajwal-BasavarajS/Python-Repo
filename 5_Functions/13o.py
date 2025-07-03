def generateNthRow(n):
    row = [1]
    for k in range(1, n):
        prev = row[-1]
        # Using formula: C(n, k) = C(n, k-1) * (n - k) / k
        curr = prev * (n - k) // k
        row.append(curr)
    row.append(1)
    return row

# Example usage:
n = int(input())
print(generateNthRow(n))
