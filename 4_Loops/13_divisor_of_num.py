def divisor_of_num(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end = " ")

divisor_of_num(80)