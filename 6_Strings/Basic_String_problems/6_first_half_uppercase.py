# s = "cjnnvjvnevefvefvjndfv mddvjnfevefvdvdvdfvfedcd"

def inputs(s):
    r = len(s) // 2
    strig = s[:r].upper() + s[r:]
    print(strig)


inputs(input('enter any string\n'))