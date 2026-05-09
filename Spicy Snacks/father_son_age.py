#collect father's age
#save it in a reference 
#collect son's age
#save it in a reference 
#calculate how many years ago the father was twices the son's age
#multiply son's age by 2 and subtract father's age


current_fathers_age = int(input("Enter father's current age: "))
current_son_age = int(input("Enter son's current age: "))

year = (current_son_age * 2) - current_fathers_age
print(year)
