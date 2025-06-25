# while
count = 1
while (count <= 4) :
    print(f"{count} Nigga!")
    count += 1
    

#for 

li = ['Hello', 'this', 'is', 'PY', 'world', 'we', 'need', 'to', 'improve', 'ALOTT..!!']
li.append("Thank You") #list is changable (we can perform operations in li)
for i in li :
    print(i, end="      ")


print("")
tup = ('Hello', 1234, "bye!!")
for i in tup :
    print('\n',i)


dictionary = {1 : "APPLE", 2:"BAT",3:'CAT', 4:"DONKEY", 5:'ELEPHANT'}
for i in dictionary:
    # print(f'{i} : {dictionary[i]}')
    print("%d  %s" % (i,dictionary[i]))

set1 = {1 ,4,5,3,2,2,4,5,4}

for i in set1:
    print(i, end = "    ") #prints only distinct value in set // set gives o/p of only distinct values 


print("\nIn set we have made duplicate entries AND go to know that set doesnot print duplicate values only prints distinct values ")
for i in range(len(li)):
    print(li[i],"\n")