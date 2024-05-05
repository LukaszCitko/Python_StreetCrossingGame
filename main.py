import time
import random
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

images = ['./gif/car.gif', './gif/truck.gif', './gif/blue_car.gif', './gif/green.gif', './gif/cabrio_red.gif',
          './gif/pickup_red.gif', './gif/yellow_taxi.gif']
TRAFIC = [1, 1, 2, 2, 2, 2, 2]
screen = Screen()
screen.setup(width=800, height=800, startx=0, starty=0)

# screen.addshape('road.gif')
for i in images:
    screen.addshape(i)

# road = Turtle()
# road.shape('road.gif')
# road.penup()
# road.goto(0,125)

screen.tracer(0)
screen.bgcolor('white')
screen.title('Street Cross - press here and move with arrow "up" and "down"')

score_level = Scoreboard()
player = Player()
cars = CarManager()

game_is_prepared = False
game_is_on = True


def tesla():
    temp_start = random.randint(0, 8)
    temp_stop = random.randint(temp_start, 8)
    for i in range(temp_start, temp_stop, random.choice(TRAFIC)):
        cars.create_car(random.choice(images))
    while cars.trafic_list == []:
        tesla()


while game_is_on:

    time.sleep(0.1)

    if not game_is_prepared:
        tesla()
        cars.fast_move()


    else:
        screen.listen()
        screen.onkey(player.go_up, 'Up')
        screen.onkey(player.go_down, 'Down')
        screen.update()
        cars.move(score_level.level_score)

        # place for rising dificulty level ( variable changing will affect cars distance)

        if cars.trafic_list[-1].xcor() < 700 + score_level.level_score * 10:
            tesla()

            # winning conditions & level up:
        if player.ycor() == 315:
            time.sleep(0.6)
            score_level.level_up()
            score_level.write_score()
            player.reset_position()

    # cleaning trafic_list
    for _ in cars.trafic_list:
        if _.xcor() < -1200:
            cars.trafic_list.pop(0)
            game_is_prepared = True

        # collisions:
        if _.distance(player) < 35:
            score_level.game_over()
            player.reset_position()
