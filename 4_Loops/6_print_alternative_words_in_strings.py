# Welcome to the part 2 of For Loops in Python. In this question, we'll learn to print characters of a string at even indices.

# You are given a string str, you need to print its characters at even indices(index starts at 0).

# Note: Please go through the range function to understand how to jump 2 steps.

# Example 1:

# Input:
# str = DoctorPhenomenal
# Output:
# DcoPeoea
# Example 2:

# Input:
# str = Geeks
# Output:
# Ges


str = "helloiamhedfe"
for i in range(0,len(str),2):  ## from 0 to length of str and skip 2
        print(
            str[i],
            end="")  ##printing character and separating characters by nothing