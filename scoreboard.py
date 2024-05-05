from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.ht()
        self.penup()

        self.line = '══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════'
        self.line_mid = '─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─'
        self.level_score = 0
        with open('data.txt') as file:
            high_score_data = int(file.read())

        self.high_score = high_score_data
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-375, 350)
        self.write(f'Score: {self.level_score}      High Score: {self.high_score} ', align='left', font=FONT)

        # line road
        self.goto(-600, 285)
        self.write(self.line, align='center', font=FONT)
        self.goto(-600, -80)
        self.write(self.line, align='center', font=FONT)
        for i in range(1, 8):
            self.goto(-600, -80 + 45 * i)
            self.write(self.line_mid, align='center', font=FONT)

    def level_up(self):
        self.level_score += 1

    def game_over(self):
        self.goto(-20, -20)
        self.write('GAME OVER', align='center', font=FONT)
        time.sleep(2)
        if self.level_score > self.high_score:
            self.high_score = self.level_score
            with open('data.txt', 'w') as file:
                file.write(f'{self.high_score}')
        self.level_score = 0
        self.write_score()
