# Function to check if a letter is a vowel
def is_vowel(letter):
    vowels = "AEIOUaeiou"
    return letter in vowels

# Input a letter
letter = input("Enter a letter: ")

if len(letter) == 1 and letter.isalpha():
    if is_vowel(letter):
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")
else:
    print("Please enter a single alphabet character.")
