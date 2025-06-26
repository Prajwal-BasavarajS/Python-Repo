# #User function Template for python3
n1 = int(input())
n2 = int(input())

# Your code here
tab1 = []
tab2  = []
for i in range (1,11):
    tab1.append(i*n1)
    tab2.append(i*n2)

    
diff =[]    
for i in range(1,11):
      diff.append((n1-n2)*i)
      
print(tab1)
print(tab2)
print(diff) 


def fun_diff(n1,n2):
    diff =[]    
    for i in range(1,11):
        diff.append((n1-n2)*i)
        
    return diff

print(fun_diff(9,5))