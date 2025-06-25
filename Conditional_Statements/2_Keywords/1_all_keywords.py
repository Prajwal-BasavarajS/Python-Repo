import keyword
print('the list of keywords are')
for i , kw in enumerate(keyword.kwlist,start=1) :
    print(i,kw)
