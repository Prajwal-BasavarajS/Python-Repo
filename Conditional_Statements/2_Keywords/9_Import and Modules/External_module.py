print("External module is called")

def some_function():
    print("Hello this is some function")
    n = input("enter 33 only \n")
    if n == '33':
        print("Just executing the if condition in modules")

if __name__ == "__main__" :
    some_function()

var = "Help called! "