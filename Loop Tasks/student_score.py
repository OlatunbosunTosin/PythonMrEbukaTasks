count = 0
pass_counter = 0
scores = []
while count < 15:
    student_score = int(input("Enter score: "))
    scores.append(student_score)
    count += 1
for score in scores:
    if score >= 45:
        pass_counter += 1
failed_counter = count - pass_counter
print(f"{pass_counter} students passed and {failed_counter} students failed")
