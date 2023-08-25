from turtle import Screen
from food import food
from scoreboard import scoreboard
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
s = Snake()
Food = food()
sb = scoreboard()
screen.listen()
screen.onkey(key="Up", fun=s.up)
screen.onkey(key="Down", fun=s.down)
screen.onkey(key="Left", fun=s.left)
screen.onkey(key="Right", fun=s.right)

continue_game = True


while continue_game :
    screen.update()
    time.sleep(0.1)
    s.move()

    if s.head.distance(Food) < 15 :
        Food.refresh()
        s.extend()
        sb.increase_score()
    if s.head.xcor() > 290 or s.head.xcor() < -290 or s.head.ycor() > 290 or s.head.ycor() < -290:
        continue_game = False
        print(f"Your final score is {sb.score}")
        sb.end_game()

    for segment in s.all_turtles[1:] :
        # if s.head == segment :
        #     pass

        if s.head.distance(segment) < 10 :
            continue_game = False
            sb.end_game()
    # if s.head.ycor() > 280 or s.head.ycor() < -280:
    #     continue_game = False
    #     print(f"Your final score is {sb.score}")



screen.exitonclick()