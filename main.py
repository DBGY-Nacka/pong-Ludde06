from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def create_users():
    name1 = "Player 1"
    name2 = "Player 2"
    
    inputplayer1 = input("Skriv in namnet för spelare 1 (ENTER för standard namn): ")
    if not inputplayer1 == "":
        name1 = inputplayer1 #Changes the name if a new one has been entered
    print()
    inputplayer2 = input("Skriv in namnet för spelare 2 (ENTER för standard namn): ")
    if not inputplayer2 == "":
        name2 = inputplayer2
    return name1, name2

def main(name1, name2):

    game_is_on = True

    ball = Ball()
    paddle1 = Paddle((-350, 0))
    paddle2 = Paddle((350, 0))
    scoreboard = Scoreboard(name1, name2)

    screen.listen()
    screen.onkey(paddle2.up, "Up")     
    screen.onkey(paddle2.down, "Down")  
    screen.onkey(paddle1.up, "w")
    screen.onkey(paddle1.down, "s") 

    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        scoreboard.update_scoreboard()

        if (ball.xcor() > 320 and ball.distance(paddle2) < 50) or (ball.xcor() < -320 and ball.distance(paddle1) < 50 ):
            ball.x_bounce()
            
        if ball.ycor() < -290 or ball.ycor() > 290:
            ball.y_bounce()

        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.player1_point()

        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.player2_point()

        if scoreboard.player1_score >= 10:
            game_is_on = False
            scoreboard.game_over(name1)

        if scoreboard.player2_score >= 10:
            game_is_on = False
            scoreboard.game_over(name2)
            
    screen.exitonclick()


if __name__ == "__main__":
    player1, player2 = create_users()

    screen = Screen()
    screen.setup(800, 600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    main(player1, player2)