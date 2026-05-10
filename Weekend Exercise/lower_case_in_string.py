word = "RoSEGold"
count = 0
for character in word:
    if ord(character) >= 97 and ord(character) <= 122:
        count += 1
print(count)
