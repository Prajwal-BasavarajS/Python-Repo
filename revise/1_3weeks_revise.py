
amount = 150.75887
print("Amount: ${:.2f}".format(amount))

# end Parameter with '@'
print("Python", end='@')
print("jdnsds")



# Seprating with Comma
print('G', 'F', 'G', sep='   ' ,end="s")

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('pratik', 'geeksforgeeks', sep='@')


name = "amith"
age = 27
sex ="male"
print(f"{name} is {age} year old and his gender is {sex}")



li = []
for i in range(1,11):
    li.append(i)

print(li)


word = "hello python"
count = len(word)
print("count = ",count)



x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")



expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 5

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")



def count_bits(n):
    count = 0 
    while n > 0:
        count += n & 1 
        n = n >> 1 
        
    return count

print(count_bits(7))


for i in range (1,11):
    print(f"{i} , count_bits ==",count_bits(i))



def armstrong(n):
    s = 0
    temp = n  # Save original number
    
    while n > 0:
        r = n % 10       # Get last digit
        s += r ** 3      # Add cube of the digit to sum
        n = n // 10      # Remove last digit
    
    if s == temp:
        print("Yes its Amstrong")     # It's an Armstrong number
    else:
        print("Not Amstrong")      # Not an Armstrong number


armstrong(373)