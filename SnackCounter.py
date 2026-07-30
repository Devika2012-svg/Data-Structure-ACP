from array import array

print("---Snack Inventory---")
snack_box = {"Cookies", "Chocolate Milk", "Chocolate", "Twix"}
print("Available snacks: ", snack_box)

new = str(input("What snacks do you want to add to the current snack box? "))
snack_box.add(new)
print("New item is added! ", snack_box)

snack_box2 = {"Chocolate Milk", "Apple", "Cookies", "Banana", "Oreos"}
print("\nFriend's Snack Box:", snack_box2)

shared_snacks = snack_box.intersection(snack_box2)
print("Shared Snacks:", shared_snacks)

snack_count = array('i', [5, 8, 3, 9, 8, 5])

print("\nCurrent snack quantities:", snack_count)

snack_count.append(10)
snack_count.insert(1, 2)

print("Updated snack quantities:", snack_count)

print("\nThere are", snack_count.count(8), "snack(s) with a quantity of 8.")

snack_count.reverse()
print("\nSnack quantities in reverse order:", snack_count)
