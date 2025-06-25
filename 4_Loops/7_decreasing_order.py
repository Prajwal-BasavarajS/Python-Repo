# Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.

# for i in range(9,0):
#     print(i)

x = 9 
while x >= 0 :
    print(x , end = "       ")
    x-=1

x = 7
for i in range(x, -1,-1):
    print('\n', i, end ='      ')

