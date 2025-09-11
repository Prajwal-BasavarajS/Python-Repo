def printGfg(n):
        if(n>0):
            print("GFG",end=" ")
            return printGfg(n-1)
        

printGfg(3)