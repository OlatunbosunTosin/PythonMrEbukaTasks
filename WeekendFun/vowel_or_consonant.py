letter = input("Enter between A-Z: ")
vowel = ["a","e","i","o","u"]
alphabet = "abcdefghijklmnopqrstuvwxyz"
if letter.lower() in vowel:
    print("Vowel")
if letter.lower() not in vowel and letter.lower() in alphabet:
    print("Consonant")
if letter.lower() not in alphabet:
    print("Invalid input")



