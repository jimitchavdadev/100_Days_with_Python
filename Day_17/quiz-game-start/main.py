from question_model import Question  # Import the Question class from question_model.py
from data import question_data  # Import the question data from data.py
from quiz_brain import QuizBrain  # Import the QuizBrain class from quiz_brain.py

question_bank = []  # Initialize an empty list to store Question objects

# Iterate through the question data and create Question objects, then add them to question_bank
for question in question_data:
    question_text = question["question"]  # Get the text of the question from the data
    question_answer = question["correct_answer"]  # Get the correct answer from the data
    new_question = Question(text=question_text, answer=question_answer)  # Create a new Question object
    question_bank.append(new_question)  # Add the new Question object to the question bank list

quiz = QuizBrain(question_bank)  # Create a QuizBrain object with the question bank

# Loop through the quiz questions until there are no more questions
while quiz.still_has_question():
    quiz.next_question()  # Ask the next question in the quiz

# Print the final score after completing the quiz
print("You have completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")