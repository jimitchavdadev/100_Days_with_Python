from question_model import Question  # Import the Question class from question_model module
from data import question_data  # Import the question_data list from data module
from quiz_brain import QuizBrain  # Import the QuizBrain class from quiz_brain module
from ui import QuizInterface  # Import the QuizInterface class from ui module

# Initialize an empty list to store the questions
question_bank = []

# Iterate through each question in the question_data list
for question in question_data:
    question_text = question["question"]  # Get the question text
    question_answer = question["correct_answer"]  # Get the correct answer
    new_question = Question(question_text, question_answer)  # Create a new Question object
    question_bank.append(new_question)  # Add the new Question object to the question_bank list

# Create an instance of QuizBrain with the question_bank
quiz = QuizBrain(question_bank)

# Create an instance of QuizInterface with the quiz instance
quiz_ui = QuizInterface(quiz)

# Print a message indicating the quiz is complete
print("You've completed the quiz")

# Print the final score
print(f"Your final score was: {quiz.score}/{quiz.question_number}")