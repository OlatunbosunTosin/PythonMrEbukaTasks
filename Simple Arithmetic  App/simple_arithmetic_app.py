import random
def random_numbers_generator():
    
    first_random_number = random.randint(1,100)
    second_random_number = random.randint(1,100)
    return first_random_number, second_random_number


def subtraction_problems():
    count = 0
    count_of_correct_questions = 0
    while True:
        random_number = random_numbers_generator()
        first_random_number, second_random_number = random_number
       
        counter = 0
        question = int(input(f"What is {first_random_number} minus {second_random_number}? "))
        count += 1

        while question != abs(first_random_number - second_random_number):

            counter += 1
            if counter == 2:
                break
            print("Wrong. Please try again.")
                
            question = int(input(f"What is {first_random_number} minus {second_random_number}? "))

        if question == abs(first_random_number - second_random_number):
            print("Very good!")
            count_of_correct_questions += 1
        if count == 10:
            break
    return count, count_of_correct_questions



    
        
        



    


