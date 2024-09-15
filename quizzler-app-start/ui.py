THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.quiz_text  = self.canvas.create_text(150, 125, width=280,text=f"", font=("arial", 20,"italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.score_label= Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        right_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")

        self.right_button = Button(image=right_image, highlightthickness=0 ,command=lambda:self.checking("True")) 
        self.right_button.grid(column=0, row=2)

        self.wrong_button= Button(image=wrong_image, highlightthickness=0 ,command=lambda:self.checking("False"))
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.quiz_text ,text=f"{q_text}")
            
        else:
            self.canvas.itemconfig(self.quiz_text, text="You Have Reach The End Of The Quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")    

    def checking(self, answer):
        result = self.quiz.check_answer(answer)
        self.feed_back(result)    

    def feed_back(self, result):
        if result :
            self.canvas.config(bg= "green")
        else:
            self.canvas.config(bg= "red")

        self.window.after(1000, self.get_next_question)    