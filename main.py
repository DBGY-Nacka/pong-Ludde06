from time import sleep
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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

    ball = Ball()
    stick1 = Paddle((-350, 0))
    stick2 = Paddle((350, 0))
    scoreboard = Scoreboard(name1, name2)

    screen.listen()#Listen to key inputs  
    screen.onkey(stick2.up, "Up")
    screen.onkey(stick2.down, "Down")  
    screen.onkey(stick1.up, "w")
    screen.onkey(stick1.down, "s") 

    game_is_on = True

    while game_is_on:
        screen.update()
        sleep(ball.movement_speed)
        ball.move()

        scoreboard.update_scoreboard()

        if ball.ycor() < -290 or ball.ycor() > 290:
            ball.y_bounce()#If the ball bounces on the walls up or down

        if (ball.xcor() > 330 and ball.distance(stick2) < 55) or (ball.xcor() < -330 and ball.distance(stick1) < 55):
            ball.x_bounce()#If the ball bounces on stick 1 or 2 it changes direction (x_bounce)            

        if ball.xcor() > 345:
            ball.reset_position()
            scoreboard.player1_point()#Give player 1 a point

        if ball.xcor() < -345:
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