def check(text):
    for letter in text:
        if letter >= 'A' and letter <= 'Z':
            print(letter, "is uppercase")
        elif letter >= 'a' and letter <= 'z':
            print(letter, "is lowercase")

check(input("Enter a word: "))