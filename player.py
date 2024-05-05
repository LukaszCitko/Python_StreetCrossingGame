from turtle import Turtle

STARTING_POSITION = (0, -90)
MOVE_DISTANCE = 45
FINISH_LINE_Y = 460


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.turtlesize(1.2)
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.ymove = MOVE_DISTANCE

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        if self.ycor() < 545:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() != -110:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)


