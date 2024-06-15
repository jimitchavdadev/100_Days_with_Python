class QuizBrain:
    def __init__(self, q_list):
        # Initialize QuizBrain with a list of questions
        self.question_number = 0  # Initialize question number to track progress
        self.score = 0  # Initialize score to track correct answers
        self.question_list = q_list  # Store the list of questions

    def still_has_question(self):
        # Check if there are more questions to ask
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Present the next question to the user and check their answer
        current_question = self.question_list[self.question_number]  # Get the current question
        self.question_number += 1  # Move to the next question
        user_answer = input(f"Q. {self.question_number}: {current_question.text} (True/False): ")  # Get user's answer
        self.check_answer(user_answer, current_question.answer)  # Check user's answer

    def check_answer(self, user_answer, correct_answer):
        # Check if the user's answer matches the correct answer and update the score
        if user_answer.lower() == correct_answer.lower():  # Check if the answers match (case insensitive)
            self.score += 1  # Increment score for correct answer
            print("You got it right! ")  # Print message for correct answer
        else:
            print("You got it Wrong! ")  # Print message for wrong answer
        print(f"The correct answer was {correct_answer}.")  # Print the correct answer
        print(f"Your current score is: {self.score}/{self.question_number}\n")  # Print current score and question number