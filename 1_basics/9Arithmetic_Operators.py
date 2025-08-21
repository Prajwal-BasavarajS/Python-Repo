# x =  int(input(" Enter a Number "))
# y =  int(input(" Enter a Number "))

x , y = map(int,input().split())
print("x = ", x)
print("y = " ,y)

add = x + y
sub = x - y
multi = x * y
div = x / y
fdiv = x // y
mod = x % y
power = x ** y

print( ' add = ', add,'\n' , 
      'sub = ', sub , '\n' , 
      'multi = ' , multi ,'\n', 
      'div = %.2f'  %div , '\n' ,  
      'floor division = ',fdiv, '\t gives quotient \n', 
      'modulous = ', mod , '\tgives remiander \n',
       "power = ", power )


x = int(input())
print(x)
x = 1.5 
print(int(x))

c = 5
y = 5
print(c+5)
