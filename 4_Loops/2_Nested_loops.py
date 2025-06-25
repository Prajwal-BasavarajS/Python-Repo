# Nested Loops 

# range starts from 0 to n-1
for i in range(1,3):
    print(i)
    print(f'''running {i} block till j- loop is full executed and when J-loop is done i-loop wll again run for
2nd condition(i in range (1,3) ) or next iteration again j gets extectued and prints its range till i-loops gets terminated''')
    for j in range (10,13):
        print(j)



print("\n Matrix printing 2x2")
x = [ 2 , 4 , 9 ]
y = [ 6 , 7 , 8 ]

for i in x:
    for j in y :
        print(i , j )
    print('\n')


