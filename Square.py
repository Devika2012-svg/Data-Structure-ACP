print("-" * 10 ,"🌺 Square Numbers", "-" * 10)
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

square_numbers = []

for num in range(start, end + 1):
    root = int(num ** 0.5)
    if root * root == num:
        square_numbers.append(num)

print("\nSquare numbers between", start, "and", end, "are:")
print(square_numbers)

even = []
odd = []

for num in square_numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("\nThe even square numbers are:", even)
print("The odd square numbers are:", odd)
