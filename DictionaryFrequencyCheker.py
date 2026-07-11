print("🎉 This is the Dictionary Frequency Checker!\n")

words = {
    "Python" : 1,
    "CSS" : 2,
    "JavaScript" : 9,
    "JAVA" : 6,
    "C++" : 7,
    "SQL": 3,
    "HTML": 5,
    "Bootstrap": 7,
    "Node.js": 1,
    "Firebase": 8,
}

print("Dictionary:")
print(words)

word = input("\n🔍 Enter the word you wish to check: ")

if word in words:
    if words[word] == 1:
        print(f"\n✅ '{word}' appears {words[word]} time in the dictionary.")
    else:
        print(f"\n✅ '{word}' appears {words[word]} times in the dictionary.")
else:
    print(f"\n❌ Sorry! '{word}' is not found in the dictionary.")
