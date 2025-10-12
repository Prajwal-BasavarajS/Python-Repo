def toLower (s)-> str :
    # code here
    a = []
    for char in s : 
        if char.upper() == char or char.lower() == char :
            x = char.lower()
        a.append(x)
        
    word = ''.join(a)
    return word

 
print(toLower("ASDSDfdjndaWW"))


def tolow(s):
    return s.lower()

print(tolow("WDDASCAC cvdcdscs"))