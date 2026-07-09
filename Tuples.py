print("-" * 10, "🌸 Tuple Product 🌸", "-" * 10)

tup1 = (4, 3, 2, 2, -1, 18)

num = int(input("Enter a number to multiply the tuple with: "))

print("\n🌼 Original Tuple:", tup1)

result = ()

for item in tup1:
    result += (item * num,)

print("🌸 New Tuple:", result)


print("\n" + "-" * 50)

tup2 = (2, 4, 8, 8, 3, 2, 9)
print("\n🌷 Tuple 2:", tup2)

result2 = ()
for item in tup2:
    result2 += (item * num,)


print("🌸 New Tuple:", result2)
