x = float(input("Enter a number"))

# while x < 0 :
#     i = x % 10 

# print(i)

i = abs( x )%10
print(i)

print('new')
while x > 0 :
    last = x % 10
    print(last)
    x //= 10
print("end")

n = 836321
digits = []

while n > 0 : 
    digits.append(n%10)
    n//=10

digits.reverse()

print("new")
print(digits)


# num = 12345
# digits = []

# while num > 0:
#     digits.append(num % 10)
#     num //= 10

# digits.reverse()
# print(digits)   # Output: [1, 2, 3, 4, 5]
