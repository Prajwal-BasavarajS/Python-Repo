# sort() function sorts/ arranges the items in acending or decending order without altering the original items


a = [5,5,6, 2, 9, 1, 3]

#Sorted() arranges the list in ascending order
b = sorted(a)
print(b)

# sort () decending

c = sorted(a,reverse=True)
print(c)


d = ["apple", "banana", "cherry", "date"]
res = sorted(d, key=len)
print(res)

e = [ {"name":"apple","score":98},
     {"name":"banana","score":36},
     {"name":"cherry","score":65}]

result = sorted(e,key=lambda x:x['score'])
print(result)



g = [923,3434,6,56,234,432,553,4,565]
print()
g.sort(reverse=True)
print(g,"decending")
print()
g.sort()
print(g,"ascending")


print()
h = ['appple','cheery','fruit','kiwi', 'sapotta','organe','mango']
p = sorted(h,key = lambda x:x[-1])
print(p,'\n')


