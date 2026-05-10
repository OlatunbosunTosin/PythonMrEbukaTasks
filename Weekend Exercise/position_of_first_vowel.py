word = "hippopotamus"
vowel = ["a","e","i","o","u"]
count = 0
for character in word:
    if character in vowel:
        break
print(word.index(character))
    
