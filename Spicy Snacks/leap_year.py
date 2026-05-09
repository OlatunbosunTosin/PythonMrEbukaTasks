#collect year from user
#check if year is divisible by 4 and if year is not divisible by 100 or year is divisible by 400
#if it is, it is a leap year
#else it is not a leap year


year = int(input("Enter year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
