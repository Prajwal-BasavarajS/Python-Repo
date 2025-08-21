number = 0

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
         
    case _:                                     #default case 
        print("Other number")


# match case is similar to switch case 