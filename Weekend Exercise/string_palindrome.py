reversed_string = ""
word = "Ama"
for character in word:
    reversed_string =  character + reversed_string
if word.lower() == reversed_string.lower():
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
