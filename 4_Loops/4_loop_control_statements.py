# break 

for i in range(10):
    if i == 7 :
        break
    print(i, end = '      ')

# continue
for i in range (10):
    if i == 3 or i == 6 :
        print( ' skipped / continue used ')
        continue  # this skips the block and prints next number 
    print(i)

# pass

print()
for i in range(ord('a') ,ord('f')):
    if chr(i) == 'd' :
        print('pass does nothing')
        pass 
    print( chr(i))


# ord('a') ➝ 97
# chr(97) ➝ 'a'

print()


for i in range(ord('a'), ord('z') + 1):
    print(chr(i), end=" ")



