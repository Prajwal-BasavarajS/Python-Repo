s = "Sjnfv vjndjkfnbvv nvbfkhjv  djnvb infvonvdv nv if ifb f"

length = len(s)
print(length)

s = s.replace(" ","")
print(len(s))

print(f"{length-(len(s))} = spaces")


r = list(filter(lambda c: c !=" " ,s))
print(r)
print(len(r))

r = len(list(filter(lambda c: c !=" " ,s)))
