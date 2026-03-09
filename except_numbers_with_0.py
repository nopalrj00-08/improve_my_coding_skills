# input 100 numbers
for i in range (0,101):
    if i % 10 !=0: # not include the numbers with 0's
        print(f"{i}",end=",") # print the numbers