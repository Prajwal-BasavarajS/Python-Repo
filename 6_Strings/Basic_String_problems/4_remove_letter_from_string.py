s = "hello world"

r = s.replace("o","*")

print(r)
s = "".join(filter(lambda c: c != "o", s))
print(s)

f = []
for ch in s:
    if ch != "o":
        f.append(ch)
i = "".join(f)

print(f)
print(i)

r = "".join(filter(lambda c : c!="o",s ))
print(r)
