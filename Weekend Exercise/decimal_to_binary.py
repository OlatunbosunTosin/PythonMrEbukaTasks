integer = 7
binary_number = 0
while integer > 0:
    remainder = integer % 2
    binary_number = remainder + (binary_number * 10)
    integer = integer // 2

binary = str(binary_number)
final_binary = ""
for character in binary:
    final_binary = final_binary + character 
print(final_binary)
