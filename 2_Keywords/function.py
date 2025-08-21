def fun1_rule():
    print('called')
    print("hei")
    x = input()
    y = '5' + x
    print(y)
    return 2,x

res = fun1_rule
print(res())
