# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:21:52 2022

@author: JeremyGarrard
"""

import turtle
import winsound
import time

wn = turtle.Screen()
wn.title("Pong by Jeremy")
wn.bgcolor("black")
wn.setup(width=800,height = 600)
wn.tracer(0)

winner = False


#score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=(5),stretch_len=(1))
paddle_a.penup()
paddle_a.goto(-350,0)




# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=(5),stretch_len=(1))
paddle_b.penup()
paddle_b.goto(350,0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .4
ball.dy = .4


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align= "center", font=("Courier",24,"normal"))
                                                           
#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
def clse():
    wn.exitonclick()


def quit():
    global running
    running = False
    
def cheat_status():
    global cheat
    cheat = True
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("red")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,0)
    pen.write("GIRLFRIEND MODE ENGAGED",align= "center", font=("Courier",24,"normal"))

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
wn.onkeypress(quit,"q")
wn.onkeypress(cheat_status, "t")


running = True
cheat = False




#main game loop

while running:
    wn.update()
    
    
    
    
    if not cheat:    
        #move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
    else:
        if ball.xcor() > 0: 
            ball.setx(ball.xcor() + ball.dx*2)
            ball.sety(ball.ycor() + ball.dy*2)
        else:
            ball.setx(ball.xcor() + ball.dx*.8)
            ball.sety(ball.ycor() + ball.dy*.8)
    
    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
            
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align= "center", font=("Courier",24,"normal"))
    if score_a >10:
        winner= True
        winner_name = "Player A"
        running = False
            
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align= "center", font=("Courier",24,"normal"))
    if score_b >10:
        winner= True
        winner_name = "Player B"
        running = False
        
    
    #collison detection
    if abs(ball.xcor() - paddle_a.xcor()) <10 and abs(ball.ycor() - paddle_a.ycor()) <50:
        ball.dx *= -1
        #winsound.PlaySound('C:/Users/JeremyGarrard/Desktop/Pong_Game/Left_Bounce.m4a', winsound.SND_ASYNC)
        
    if abs(ball.xcor() - paddle_b.xcor()) <10 and abs(ball.ycor() - paddle_b.ycor()) <50:
        ball.dx *= -1
        #winsound.PlaySound(r'C:\\Users\JeremyGarrard\Desktop\Pong_Game\Right_Bounce.m4a', winsound.SND_ASYNC)
    
    

    
    
    
    
    
    
    wn.update()

if winner:
    winner = winner
    wn.clear()
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("red")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("The winner is: {}!".format(winner_name),align= "center", font=("Courier",24,"normal"))
    time.sleep(10)

         

wn.bye()
turtle.done()