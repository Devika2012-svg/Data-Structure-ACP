print("-" * 10, "🌺 Square Numbers", "-" * 10)

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

choice = int(input(
    "\nChoose:\n"
    "1. Find the perfect square numbers between this range.\n"
    "2. Find the squares of all numbers between this range.\n"
    "Enter your choice: "
))

if choice == 1:
    square_numbers = []

    for num in range(start, end + 1):
        root = int(num ** 0.5)
        if root * root == num:
            square_numbers.append(num)

    print("\nPerfect square numbers between", start, "and", end, "are:")
    print(square_numbers)

    even = []
    odd = []

    for num in square_numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    print("\nEven perfect square numbers:", even)
    print("Odd perfect square numbers:", odd)

elif choice == 2:
    print("\nSquares of all numbers between", start, "and", end, "are:")

    even_squares = []
    odd_squares = []

    for num in range(start, end + 1):
        square = num ** 2
        print(f"{num}² = {square}")

        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print("\nEven squares:", even_squares)
    print("Odd squares:", odd_squares)

else:
    print("Invalid choice! Please enter 1 or 2.")
