a = int(input())
b = int(input())

########### Write your code below ###############

# Write Code to Swap

########### Write your code above ###############

# a , b = b, a

c = a
a = b
b = c

print(a, b)


def f():
    a = "I am local"
    print(a)

f()
# print(a)  # This would raise an error since 'local_var' is not accessible outside the function8

