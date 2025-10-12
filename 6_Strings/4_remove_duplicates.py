def remove_dup(s):
    r = []
    for char in s:
        if char not in r:
            r.append(char)

    word = "".join(r)

    return word


print(remove_dup("geEksforGEeks"))