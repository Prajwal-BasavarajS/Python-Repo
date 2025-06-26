def right_angle_triangle(n):
    for i in range(0,n):
        i+=1
        for j in range(i):
            print('*', end = ' ')
        print()


n = int(input("enter a number"))

right_angle_triangle(n)