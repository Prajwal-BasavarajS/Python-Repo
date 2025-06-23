arr = tuple(map(int, input().split()))
test=dict()
def tester(test,arr):
    for i in arr:
        if i in test:
            test[i]+=1
        else:
            
            test[i]=0
    for i in test.keys():
        
        if test[i]>=1:
            
            return False
            break
    return True
print(tester(test,arr))