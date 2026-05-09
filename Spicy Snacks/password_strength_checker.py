#collect password from user
#check if the length is greater or equal to 6 and if the length is less or equal to 10, print medium
#else check if the length is less than 6, print weak
#else check if the length is greater 10, print strong
#else check if the length is less than 1, print invalid



password = input("Enter password: ")

if len(password) >= 6 and len(password) <= 10:
    print("Medium")
elif len(password) < 6:
    print("Weak")
elif len(password) > 10:
    print("Strong")
elif len(password) < 1:
    print("Invalid")
