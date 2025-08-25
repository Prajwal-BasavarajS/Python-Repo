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



n = 5 
print()

for i in range(1,11):
    print(f" {i} * {n}  = ", i*n )




s = "hello we are studying python "

for i in range(0,len(s),2):
    print(f"{s[i]}  = " , i )

