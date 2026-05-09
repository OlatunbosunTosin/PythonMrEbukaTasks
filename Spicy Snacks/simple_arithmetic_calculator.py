#collect first number
#save it in a reference 
#collect second number
#save it in a reference 
#collect operator
#save it in a reference 
#if operator is +, add both numbers
#save it in a reference 
#if operator is -, subtract both numbers
#save it in a reference 
#if operator is *, multiply both numbers
#save it in a reference 
#if operator is /, divide both numbers
#save it in a reference 
#print the result

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operator = input("Enter +,-,* or /: ")

if operator == "+":
    result = first_number + second_number
if operator == "-":
    result = first_number - second_number
if operator == "*":
    result = first_number * second_number
if operator == "/":
    result = first_number / second_number
print(result)
