numbers = 0
for i in range (10):
    num=float(input(f"Enter a number {i+1}: ")) # Ask for 10 numbers
    if num % 2 == 0: # Find the even numbers
        numbers += 1
print(f"{numbers} even numbers") # Print the even numbers
