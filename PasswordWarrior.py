import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*?"
extra_symbols = "_-+=~<>"

personalities = [
    "🐉 Dragon",
    "🥷 Ninja",
    "🧙 Wizard",
    "🏴‍☠️ Pirate",
    "🤖 Robot",
    "👽 Alien"
]

def generate_password(length, difficulty):
    if difficulty == 1:
        characters = letters + numbers
    elif difficulty == 2:
        characters = letters + numbers + symbols
    else:
        characters = letters + numbers + symbols + extra_symbols

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


def password_score(password):
    score = 0

    if len(password) >= 8:
        score += 25

    if len(password) >= 12:
        score += 25

    if any(char.isupper() for char in password):
        score += 15

    if any(char.islower() for char in password):
        score += 15

    if any(char.isdigit() for char in password):
        score += 10

    if any(char in symbols for char in password):
        score += 10

    return score


print("=" * 50)
print("          🔐 PASSWORD FORTRESS 🔐")
print("=" * 50)

print("\nWelcome, Password Warrior! 🛡️")
print("Let's create some powerful passwords to protect our kingdom!!!\n")

while True:
    print("Choose your password difficulty:")
    print("1. 🟢 Easy")
    print("2. 🟡 Strong")
    print("3. 🔴 INSANE")

    try:
        difficulty = int(input("\nEnter your choice (1-3): "))
    except ValueError:
        print("⚠️ Please enter a number!")
        continue

    if difficulty < 1 or difficulty > 3:
        print("⚠️ Please choose 1, 2, or 3!")
        continue

    try:
        length = int(input("\n📏 How long should the password be? "))
    except ValueError:
        print("⚠️ Please enter a number!")
        continue

    if length < 6:
        print("⚠️ Too short! Even a goblin could guess that. 👺")
        continue

    try:
        amount = int(input("🎲 How many passwords should I generate? "))
    except ValueError:
        print("⚠️ Please enter a number!")
        continue

    if amount < 1:
        print("⚠️ You need to generate at least 1 password!")
        continue

    print("\n" + "=" * 50)
    print("             ⚔️ PASSWORD FORGE ⚔️")
    print("=" * 50)

    for i in range(amount):
        password = generate_password(length, difficulty)
        score = password_score(password)
        personality = random.choice(personalities)

        print("\n🔑 Password", i + 1, ":", password)
        print("🎭 Personality:", personality)
        print("🏆 Strength Score:", score, "/100")

        if score < 50:
            print("🔴 Weak - The fortress will fall!! You failed!")
        elif score < 75:
            print("🟡 Good - Your fortress is holding!")
        elif score < 90:
            print("🟢 Strong - Nice work, warrior!")
        else:
            print("🔥 LEGENDARY - You have done well!")

    print("\n" + "=" * 50)

    again = input("🔄 Generate more passwords? (y/n): ").lower()

    if again != "y":
        print("\n🏰 The Password Fortress is closing...")
        print("👋 Goodbye, Password Warrior! Come back stronger!")
        break
