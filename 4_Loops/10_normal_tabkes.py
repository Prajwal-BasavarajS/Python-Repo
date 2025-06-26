n=9
for i in range(1,11):
            print(i*n)


def getTable(n):
        # code here
        table = []
        for i in range(1,11):
            table.append(i*n)
        return table

print(getTable(9))