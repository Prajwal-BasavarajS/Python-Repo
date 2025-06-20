a =int(input('enter number \n'))
b = int(input('enter number \n'))
# a =int(input('enter number \n'))
# b = int(input('

def checkStatus(a, b, flag):
        # code here
        if flag:
            return a < 0 and b < 0
        else:
            return (a >= 0) != (b >= 0)


a=4 
b=-1
flag = True       
res = checkStatus(a,b,flag)
print(res)
