import turtle
import time
import random

delay = 0.15

#Score
score = 0
high_score = 0
head_size = 1.1

#Set Up Screen

wn = turtle.Screen()
wn.title ("Snake Game by Mike")
wn.bgcolor("green")
wn.setup(width = 700, height = 500)
wn.tracer(0) # turns off screen updates

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("turtle")
head.color("blue")
head.penup()
head.goto(0,0)
head.shapesize(head_size)
head.direction = "stop"

mower = turtle.Turtle()
mower.speed(0)
mower.shape('arrow')
mower.color('red')
mower.penup()
mower.goto(0,0)
mower.direction = 'up'

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#Wall

segments = []

walls = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write(f"Score: {score}  High Score: 0", align="center", font=("Comic Sans", 24, "normal"))
#Functions

def go_up():
    if head.direction != "down":
        head.direction = "up"
        head.settiltangle(90)

def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.settiltangle(270)

def go_left():
    if head.direction != "right":
        head.direction = "left"
        head.settiltangle(180)

def go_right():
    if head.direction != "left":
        head.direction = "right"
        head.settiltangle(360)

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    

#keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
# Main Game Loop
while True:
    wn.update()
    head.shapesize(head_size)
    # if mower.direction =='up':
    #     if mower.ycor() <340:
    #         mowerY = mower.ycor()
    #         mower.sety(mowerY+20)

    #elif mower.direction == 'down':
        #if mower
    mower_time = random.randint(1,4)
    if mower_time == 1:
        mower.direction = 'up'
        mowerY = mower.ycor()
        mower.sety(mowerY + 20)
            
    elif mower_time == 2:
        mower.direction = 'down'
        mowerY = mower.ycor()
        mower.sety(mowerY-20)
        
    elif mower_time == 3:
        mower.direction = 'right'
        mowerX = mower.xcor()
        mower.setx(mowerX +20)

    elif mower_time == 4:
        mower.direction = 'left'
        mowerX = mower.xcor()
        mower.setx(mowerX -20)

    #Check for border collision
    if head.xcor()> 340 or head.xcor()<-340  or head.ycor() > 240 or head.ycor() < -240:
        time.sleep(0.5)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.hideturtle()
        segments.clear()

        #Reset the score
        score = 0

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Comic Sans", 24, "normal"))

    #Check for Collision with Food
    if head.distance(food) < 20:
        # Move food to random spot on screen
        x = random.randint(-340, 340)
        y = random.randint(-240, 240)
        food.goto(x,y)
        head_size += 0.05

        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('turtle')
        new_segment.color('gray')
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -=0.001

        #Make the wall list bigger:
        new_wall = turtle.Turtle()
        new_wall.speed(0)
        new_wall.shape("square")
        new_wall.color('black')
        new_wall.penup()
        new_wall.goto(-500, -500)
        walls.append(new_wall)

        #Add onto the score
        score +=10
        
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Comic Sans", 24, "normal"))

    # move the end segments first in reverse order
    for index in range (len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move Segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Reset Snake if Snake Head Touches Snake Body
    for segment in segments: 
        if segment.distance(head)<20:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.hideturtle()
            segments.clear()

    #Make the wall
    if len(walls) < 20:
        x = -200
        for index in range(len(walls)-1, 0, -1):
            x+=20
            if len(walls) >1:
                walls[index].goto(x+20, 50)


    time.sleep(delay)


wn.mainloop()
