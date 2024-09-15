from turtle import Turtle


FONT= ("Arial", 20, "normal")
ALIGN = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(0, 265)
        self.sc = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.rewrite()

    # def game_over(self):
    #     self.teleport(0, 0)
    #     self.write(arg="Game Over.", align=ALIGN, font=FONT)    

    def rewrite(self):    
        self.clear()
        self.write(arg=f"Score: {self.sc} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.sc > self.high_score:
            self.high_score = self.sc
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.sc = 0

        self.rewrite()            