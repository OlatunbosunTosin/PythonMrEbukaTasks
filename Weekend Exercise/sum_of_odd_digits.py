integer = "123456"
sum = 0
for digit in integer:
    if int(digit) % 2 != 0:
        sum += int(digit)
print(sum)
