count = 0
for i in range (10):
    num=float(input("Enter Ten numbers:  ")) # input ten numbers
    if num % 2 != 0:
        count += 1 # counting the odd numbers
print(f"The odd numbers are {count}") # print how many are odds


