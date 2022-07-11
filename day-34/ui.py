from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas_text = self.canvas.create_text(
            150, 
            125,
            width=280, 
            text="Blah", 
            font=('Arial', 18, 'italic'), 
            fill=THEME_COLOR
        )

        self.score_text = Label(text="Score: 0", bg=THEME_COLOR, fg='white')

        yes_img = PhotoImage(file='images/true.png')
        self.yes_btn = Button(image=yes_img, command=self.answer_true, highlightthickness=0)

        no_img = PhotoImage(file='images/false.png')
        self.no_btn = Button(image=no_img, command=self.answer_false, highlightthickness=0)

        self.score_text.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=25)
        self.yes_btn.grid(row=2, column=0)
        self.no_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="Quiz completed!")
            self.yes_btn.config(state='disabled')
            self.no_btn.config(state='disabled')

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        
        self.window.after(1000, self.get_next_question)