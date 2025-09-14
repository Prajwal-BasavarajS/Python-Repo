# print('''map() function in Python applies a given function to each element of an iterable (list, tuple, set, etc.) and 
#     returns a map object (iterator). It is a higher-order function used for uniform element-wise transformations, 
#         enabling concise and efficient code.''')



s = ['5','4','3','2','2','1']
p = map(int,s)

print("SET")
print(set(p))

print('\nTuple')
print(tuple(p))

print('\nlist')
print(list(p))


print('''\nIn the above map function iterates once only and it gets exhausted so we get blank print statement or tuple and list ''')

print("To set it correct")

s = ['5','4','3','2','2','1'] 
p = list(map(int,s))            #change here

print("SET")
print(set(p))

print('\nTuple')
print(tuple(p))

print('\nlist')
print(list(p))



def twice(a):
    return a * 2

d = [2,3,4,5,6]
res = list(map(twice,d))
print(res)
