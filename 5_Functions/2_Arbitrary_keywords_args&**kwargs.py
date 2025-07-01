
def arbitrary_non_keyword_arguments(*args):
    for key  in args:
        print(key)
arbitrary_non_keyword_arguments('Geeks','for', 'Geeks','ji')


def arbitrary_keyword_arguments(**kwargs):
    for i,j in kwargs.items():
        print("%s == %s" % (i,j))


arbitrary_keyword_arguments( one ='Hello', two = ' ppl ' , three= 'i love you')


def non_key_agrs(*args):
    for arg in args:
        return sum(args)
    

print('\n sum == ',non_key_agrs(8,99,77,5,4,3))