vowelList = ["a", "e", "i", "o", "u"]
letter = input("Enter a letter: ").strip()[:1]

for i in vowelList:
    if i == letter:
        print("the letter ",letter, "is a vowel letter")
        break
else:
    print("the letter ",letter, "is not a vowel letter")