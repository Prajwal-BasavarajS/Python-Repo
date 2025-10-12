# Python has a lot of string methods that can be used to manipulate the strings like converting 
# to lowercase, capitalizing, trimming the spaces and so on.

# In this question, we'll take a look at inbuilt string methods like title(), swapcase(), find(), strip().
# You'll be given a string str and x, you'll perform various operations on them.



def trim(s):
    return s.strip()


def findd(s,x):
    return s.find(x)

def make_title(s):
    return s.title()

def swapcases(s):
    return s.swapcase()

print(trim("          jekfwmfs      "))
print("\n",findd("hellothere", "the"))
print("check 5")
print()
print(swapcases("hhebdeqhEWFNIN"))
print()
print(make_title("hello"))