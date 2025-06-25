# # You are familiar with basics of input/output and many other useful things in Python. This module is all about conditional statements like if, elif, else; for, while, etc.

# # In Python, any conditional statement ends with ':' (proper indentation must be followed while working through loops).

# # There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.

# # Now, complete the function which returns true if you are in trouble, else return false

# # Example 1:

# # Input:
# # j_angry = True, s_angry = True
# # Output:
# # True
# # Explanation:
# # Since both of them are angry, you are in trouble.

# Input:
# j_angry = True, s_angry = False
# Output:
# False
# Explanation:
# Only one of them is angry, you are not in trouble.



def angry(j_angry,s_angry):
    if (j_angry and s_angry) == 1 :
        return True
    elif(not j_angry and not s_angry) == 1 :
        return True
    else :
        return False 


# print("For inputs enter only 0 / 1 \n \n ")    
# j_angry = bool(input())
# s_angry = bool(input())

j_angry = 0
s_angry = 1

res = angry(j_angry , s_angry )
print(res)