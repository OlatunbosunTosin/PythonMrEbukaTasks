#collect first score
#save it in a reference 
#collect second score
#save it in a reference 
#collect third score
#save it in a reference 
#calculate average
#if the average is between 90 and 100, print A
#elif the average is between 80 and 89, print B
#elif the average is between 70 and 79, print C
#elif the average is between 60 and 69, print D
#elif the average is between 0 and 59, print F

first_score = int(input("Enter first score: "))
second_score = int(input("Enter second score: "))
third_score = int(input("Enter third score: "))

average = (first_score + second_score + third_score) / 3

if average >= 90 and average <= 100:
    print('A')
elif average >= 80 and average < 90:
    print('B')
elif average >= 70 and average < 80:
    print('C')
elif average >= 60 and average < 70:
    print('D')
elif average >= 0 and average < 60:
    print('F')
