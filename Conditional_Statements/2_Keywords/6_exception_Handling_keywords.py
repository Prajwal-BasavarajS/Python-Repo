a, b = 4, 0


try:
    k = a // b  # Attempt integer division (4 // 0)
    print(k)
    
# This block catches the ZeroDivisionError
except ZeroDivisionError: 
    print("Can't divide by zero")

finally:
    # This block is always executed regardless of the exception
    print('This is always executed')


print("The value of a / b is : ")

# Will raise an AssertionError because b == 0
assert b != 0, "Divide by 0 error"  

# Division is attempted but will not reach due to assert
print(a / b)  

# Raise a TypeError if the strings are different
temp = "geeks for geeks"
if temp != "geeks":
    raise TypeError("Both the strings are different.")