word = "RoSEGold"
count = 0
for character in word:
    if ord(character) >= 65 and ord(character) <= 90:
        count += 1
print(count)
