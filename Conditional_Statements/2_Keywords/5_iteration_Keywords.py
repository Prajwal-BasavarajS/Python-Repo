
# iteration keywords
#  For While Continue Pass break

#  For iteration statement used to control the flow of statements
#  While same as for 
# break: “break” is used to control the flow of the loop. The statement is used to break out of the loop and passes the control to the statement following immediately after loop.
# continue: “continue” is also used to control the flow of code. The keyword skips the current iteration of the loop but does not end the loop.


for n in range(6) : 
    if n == 4 :
        continue
    # skips the umber 4 and prints upto 5
    print(n, end="     ")
print('')
count = 0 
while count < 7:
    count += 1 
    if count == 4:
        break 
    # break stops the flow and comes out when count 4 == 4
    print(count)