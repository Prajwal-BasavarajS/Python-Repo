def right_angle_triangle(n):
    for i in range(1,n):
     
        for j in range(i):
            print('*', end = ' ')
        print()


n = int(input("enter a number"))
n +=1 
right_angle_triangle(n)

print()


for i in range (1,7):
    
    for j in range(i):
            print('*',end = " ")
    print()