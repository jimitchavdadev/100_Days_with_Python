import html  # Import the html module to unescape HTML characters in question text


class QuizBrain:

    # Initialize the QuizBrain object with a list of questions
    def __init__(self, q_list):
        self.question_number = 0  # Initialize the question number to 0
        self.score = 0  # Initialize the score to 0
        self.question_list = q_list  # Store the list of questions
        self.current_question = None  # Initialize the current question as None

    # Check if there are still questions left to ask
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Move to the next question and return its text
    def next_question(self):
        self.current_question = self.question_list[self.question_number]  # Get the current question
        self.question_number += 1  # Increment the question number
        q_text = html.unescape(self.current_question.text)  # Unescape HTML characters in the question text
        return f"Q.{self.question_number}: {q_text}"  # Return the formatted question text

    # Check if the user's answer is correct
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer  # Get the correct answer for the current question
        if user_answer.lower() == correct_answer.lower():  # Compare user answer with correct answer (case-insensitive)
            self.score += 1  # Increment the score if the answer is correct
            return True  # Return True indicating the answer was correct
        else:
            return False  # Return False indicating the answer was incorrect
