def empty_right_angle_triangle(n):
    for i in range(1,n+1):
        # i += 1
        for j in range(1,i+1):
            if j == 1 or j == i or i == n :
                print('*', end = ' ')
            else :
                print(" ",end = " ")
        
        print()

n = int(input(" "))
print()
empty_right_angle_triangle(n)