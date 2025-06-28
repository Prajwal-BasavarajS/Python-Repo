for i in range(0,9):
    for j in range(0,9-i):
        print('*', end = " ")
    print()


# def inverted_right_angle(n):
#     print("Inverted Right angle triangle")
   
#     for i in range(0,n):
#         for j in range(1,(n+1)-i):
#             print("*", end = " ")
#         print()


# inverted_right_angle(8)


def inverted_right_angle(n):
    print("Inverted Right angle triangle")
   
    for i in range(0, n):
        for j in range(0, n - i):
            print("*", end = " ")
        print()


inverted_right_angle(8)


n = 9
li =[]
for i in range(1,n+1):
    if(n % i == 0):
        li.append(i) 
    print(li)