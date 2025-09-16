# FILTER
# filter() function is used to extract elements from an iterable (like a list, tuple or set) that satisfy a given condition. 
# It works by applying a function to each element and keeping only those for which function returns True.

def funct(word):
    return word.startswith("a")

def ends(words):
    return words.endswith("a")



s = ["apple","adam","avacado",'cherrya','ricea','ant','A4','anaconda']

print()

ends_with = list(filter(ends,s)) 
res = list(filter(funct,s))

print(res)      # prints all the words that starts with a 

print(f'\n{ends_with}')

print()

# filter function that filters all even number in the range

def even(n):
    return n%2 == 0

s=[]            #important  or s  = range(1,21)

for i in range(1,21):
    s.append(i)


def double(d):
    return d * 2


even_numbers = list(filter(even,s))
doubling = list(map(double,even_numbers))
print(even_numbers)

print(f'\n{doubling}')





