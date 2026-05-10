import unittest
import simple_arithmetic_app

class TestThatSimpleArithmeticAppWorksCorrectly(unittest.TestCase):

    def test_that_random_nummber_generated_is_not_less_than_zero(self):
        first_number, second_number = simple_arithmetic_app.random_numbers_generator()
        self.assertTrue(first_number > 0)
        self.assertTrue(second_number > 0)
        

    def test_for_total_number_of_questions(self):
        total_questions, total_correct_answers = simple_arithmetic_app.subtraction_problems()
        self.assertEqual(total_questions, 10)
        self.assertTrue(total_correct_answers)



