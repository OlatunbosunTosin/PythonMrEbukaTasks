reversed_integer = 0
integer = 12421
original_integer = integer

while integer > 0:
    digit = integer % 10
    reversed_integer = reversed_integer * 10 + digit
    integer = integer // 10

if original_integer == reversed_integer:
    print(f"{original_integer} is a palindrome")
else:
    print(f"{original_integer} is not a palindrome")
