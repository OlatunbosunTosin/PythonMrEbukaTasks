reversed_integer = 0
integer = 152

while integer > 0:
    digit = integer % 10
    reversed_integer = reversed_integer * 10 + digit
    integer = integer // 10
print(reversed_integer)
