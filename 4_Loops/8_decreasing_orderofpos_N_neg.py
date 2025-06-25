def pos(n):
    ## Write the code
        for i in range(n-1,-1,-1):
            print(i)
    
def neg(n):
    ##Write the code
    for i in range(n,-1,-1):
            print(f'-{i}' )

pos(7)
neg(4)

# You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.

# Note:- You don't have to return anything, you just have to print the array.

# Example 1:

# Input:
# n = 0
# Output:
# already Zero
# Example 2:

# Input:
# n = 4
# Output:
# 3 2 1 0
# Example 3:

# Input:
# n = -3
# Output:
# -3 -2 -1 0
    