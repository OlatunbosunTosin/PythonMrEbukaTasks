number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))
number_three = int(input("Enter number three: "))

largest = number_one
if number_two > largest:
    largest = number_two
if number_three > largest:
    largest = number_three

print(largest)



