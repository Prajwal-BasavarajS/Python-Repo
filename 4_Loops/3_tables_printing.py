# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 2 * 6 = 12
# 2 * 7 = 14
# 2 * 8 = 16
# 2 * 9 = 18
# 2 * 10 = 20


for i in range(2,4):
    for j in range (1,11):
        print(f'{i} * {j} =',i*j)

    print()


list1 = ['I am ', 'You are ']
list2 = ['healthy', 'fine', 'geek']

for i in (list1):
    for j in (list2):
        print ('%s  %s' % (i , j))

print()

print('''Printing only i==j tables like
1 x 1 = 1 
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25 ''')


n = int(input("enter a number"))
for i  in range(1,n+1):
    for j in range(1,n+1):
        if i == j :
            print(f'{i} * {j} =',i*j) 


print('\n New one')

for i in range (1,n+1):
    print()
    for j in range (1,n+1):
        if i == j:
            break 
        print(f'{i} * {j} =',i*j) 
        
print()

# 2 * 1 = 2

# 3 * 1 = 3
# 3 * 2 = 6

# 4 * 1 = 4
# 4 * 2 = 8
# 4 * 3 = 12

# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20

# 6 * 1 = 6
# 6 * 2 = 12
# 6 * 3 = 18
# 6 * 4 = 24
# 6 * 5 = 30

# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# 7 * 4 = 28
# 7 * 5 = 35
# 7 * 6 = 42


# Using  list comprehension to make
# nested loop statement in single line.
list1 = [[j for j in range(3)]
         for i in range(5)]
# Printing list1
print(list1)

# same same 

list1 = []
for i in range(5):
    inner = []
    for j in range(3):
        inner.append(j)
    list1.append(inner)
