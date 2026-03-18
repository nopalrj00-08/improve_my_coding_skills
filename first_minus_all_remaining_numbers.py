numbers = []
for i in range(10):
    num=float(input(f"Enter a number {i+1}: ")) # input ten numbers
    numbers.append(num)

result = numbers[0]
for j in numbers [1:]:
    result -= num # minus the first number to the remaining numbers
print(f"The remaining numbers are {result}") # Print the result