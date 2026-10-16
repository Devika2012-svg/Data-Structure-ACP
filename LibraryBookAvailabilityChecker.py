import random
from datetime import date, timedelta

print("=" * 55)
print("📚✨ WELCOME TO THE MAGIC LIBRARY! ✨📚")
print("=" * 55)

name = input("👋 What is your name? ")

print(f"\nHello, {name}! 😄")
print("Welcome to the Magic Library!")
print("📖 So many stories are waiting for you...")

books = [
    "Harry Potter",  "The Hobbit",  "1984", "The Alchemist", "Diary of a Wimpy Kid", "Percy Jackson", "The Hunger Games", "The Little Prince", "Atomic Habits", "Sherlock Holmes", "Charlie and the Chocolate Factory", "The Maze Runner"
]

copies = [ 3, 2, 0, 4, 5, 0, 3, 2, 4, 1, 5, 2]

categories = [
    "Fantasy", "Fantasy", "Dystopian", "Adventure", "Comedy", "Fantasy", "Dystopian", "Fantasy", "Self-Help", "Mystery", "Children", "Science Fiction"
]

ratings = [4.8, 4.7, 4.5, 4.6, 4.4, 4.8, 4.6, 4.9, 4.7, 4.8, 4.8, 4.0]

late_fees = [2, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 3]

library = {
    book: {"copies": copy, "category": category, "rating": rating, "late_fee": fee}
    for book, copy, category, rating, fee
    in zip(books, copies, categories, ratings, late_fees)
}

print("\n📚 OUR BOOK COLLECTION")
print("-" * 55)

for book in books:

    info = library[book]

    if info["copies"] > 0:
        status = f"🟢 {info['copies']} copies available"
    else:
        status = "🔴 Currently unavailable"

    print(f"\n📖 {book}")
    print(f"   🏷️ Category: {info['category']}")
    print(f"   ⭐ Rating: {info['rating']}/5")
    print(f"   📦 {status}")

search = input("\n🔎 Search for a book (or press Enter to skip): ")

if search:

    found_books = [ book for book in books if search.lower() in book.lower() ]

    print("\n🔍 SEARCH RESULTS")
    print("-" * 55)

    if found_books:

        for book in found_books:

            info = library[book]

            print(f"📖 {book}")
            print(f"   🏷️  {info['category']}")
            print(f"   ⭐  {info['rating']}/5")
            print(f"   📦  Copies: {info['copies']}")

    else:
        print("😢 Sorry! No books are found.")

surprise = input(
    "\n🎲 Would you like a surprise book recommendation? (yes/no): "
).lower()

if surprise == "yes":

    available_books = [
        book for book in books
        if library[book]["copies"] > 0
    ]

    if available_books:

        recommended = random.choice(available_books)
        info = library[recommended]

        print("\n🎉✨ YOUR SURPRISE BOOK ✨🎉")
        print("-" * 55)
        print(f"📖 {recommended}")
        print(f"🏷️ Category: {info['category']}")
        print(f"⭐ Rating: {info['rating']}/5")
        print(f"📦 Copies available: {info['copies']}")

        print("\n📚 Maybe this is your next favorite book! 😎")

    else:
        print("😢 There are no available books to recommend.")

chosen_book = input(
    "\n📖 Which book do you want to borrow? "
)

if chosen_book not in library:

    print("❌ Sorry, that book isn't in our library.")

else:

    info = library[chosen_book]

    if info["copies"] == 0:

        print("😢 Sorry, this book is currently unavailable.")

    else:

        borrowing_days = 14
        due_date = date.today() + timedelta(days=borrowing_days)

        info["copies"] -= 1

        book_index = books.index(chosen_book)

        print("\n" + "=" * 55)
        print("🎉📚 BOOK BORROWED SUCCESSFULLY! 📚🎉")
        print("=" * 55)

        print(f"👤  Borrower: {name}")
        print(f"📖  Book: {chosen_book}")
        print(f"🏷️  Category: {info['category']}")
        print(f"⭐  Rating: {info['rating']}/5")
        print(f"📅  Borrowing period: {borrowing_days} days")
        print(f"⏰  Due date: {due_date}")
        print(f"💰  Late fee: ${info['late_fee']} per day")
        print(f"📦  Copies remaining: {info['copies']}")
        print(f"🔢  Book index: {book_index}")

        print("\n✨ Enjoy your book! Don't forget to return it! 📚😊")
