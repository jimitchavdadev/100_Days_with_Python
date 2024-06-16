from tkinter import *  # Import everything from the tkinter module
from quiz_brain import QuizBrain  # Import the QuizBrain class from quiz_brain module

THEME_COLOR = "#375362"  # Define a constant for the theme color


class QuizInterface:

    # Initialize the QuizInterface with a QuizBrain object
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain  # Store the QuizBrain object
        self.window = Tk()  # Create the main window
        self.window.title("Quiz Game")  # Set the window title
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)  # Configure the window's padding and background color

        # Create a canvas widget to display the question
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)  # Position the canvas with padding
        self.question_text = self.canvas.create_text(
            150,  # X position of the text
            125,  # Y position of the text
            width=280,  # Maximum width of the text
            text="test",  # Initial text
            fill=THEME_COLOR,  # Text color
            font=("Arial", 15, "italic")  # Text font
        )

        # Create a label to display the score
        self.score_text = Label(
            text="Score: 0",  # Initial score text
            fg="white",  # Text color
            bg=THEME_COLOR,  # Background color
            font=("Arial", 20, "italic")  # Text font
        )
        self.score_text.grid(column=1, row=0)  # Position the score label

        # Load the true button image and create the button
        true_png = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_png, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2)  # Position the true button

        # Load the false button image and create the button
        false_png = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_png, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)  # Position the false button

        # Get the first question
        self.get_next_question()

        # Start the main loop to run the application
        self.window.mainloop()

    # Fetch the next question from the quiz and display it
    def get_next_question(self):
        self.canvas.config(bg="white")  # Reset the canvas background color
        if self.quiz.still_has_questions():  # Check if there are still questions left
            self.score_text.config(text=f"Score: {self.quiz.score}")  # Update the score display
            q_text = self.quiz.next_question()  # Get the next question text
            self.canvas.itemconfig(self.question_text, text=q_text)  # Display the question text on the canvas
        else:
            # Display end of quiz message and disable buttons if no more questions
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # Handle the event when the "False" button is pressed
    def answer_false(self):
        is_right = self.quiz.check_answer("False")  # Check if the answer is correct
        self.give_feedback(is_right)  # Provide feedback based on the correctness of the answer

    # Handle the event when the "True" button is pressed
    def answer_true(self):
        is_right = self.quiz.check_answer("True")  # Check if the answer is correct
        self.give_feedback(is_right)  # Provide feedback based on the correctness of the answer

    # Provide feedback by changing the canvas background color
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")  # Set background color to green if the answer is correct
        else:
            self.canvas.config(bg="red")  # Set background color to red if the answer is incorrect
        self.window.after(1000, self.get_next_question)  # Wait 1 second and fetch the next question
