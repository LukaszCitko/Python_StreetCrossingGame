from turtle import Turtle
import time
from car_manager import FIRST_LANE_Y, LANE_COUNT, LANE_HEIGHT

class Scoreboard(Turtle):

    def __init__(self, scale=1):
        super().__init__()
        self.color('black')
        self.ht()
        self.penup()
        self.font = ('Courier', max(10, round(24 * scale)), 'normal')

        self.level_score = 0
        with open('data.txt') as file:
            high_score_data = int(file.read())

        self.high_score = high_score_data
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-375, 350)
        self.write(f'Score: {self.level_score}      High Score: {self.high_score} ',
                   align='left', font=self.font)

        # Cars travel through lane centers; markings belong between lanes.
        road_bottom = FIRST_LANE_Y - LANE_HEIGHT / 2
        road_top = road_bottom + LANE_COUNT * LANE_HEIGHT
        for y in (road_bottom, road_top):
            self.goto(-400, y)
            self.pendown()
            self.goto(400, y)
            self.penup()
        for lane in range(1, LANE_COUNT):
            y = road_bottom + lane * LANE_HEIGHT
            for x in range(-400, 400, 80):
                self.goto(x, y)
                self.pendown()
                self.goto(x + 40, y)
                self.penup()

    def level_up(self):
        self.level_score += 1

    def game_over(self):
        self.goto(0, -20)
        self.write('GAME OVER', align='center', font=self.font)
        time.sleep(2)
        if self.level_score > self.high_score:
            self.high_score = self.level_score
            with open('data.txt', 'w') as file:
                file.write(f'{self.high_score}')
        self.level_score = 0
        self.write_score()
