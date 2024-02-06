from turtle import Turtle, Screen
import time, random

screen = Screen()
screen.bgcolor("lightblue")
screen.title("Vitejte v hadi hre")
screen.setup(width=600,height=600)
screen.tracer(False)
screen.listen()
head = Turtle("square")
head.color("red")
head.speed(0)
head.penup()
head.direction="stop"
body=[]
food = Turtle("circle")
food.color("black")
food.penup()
food.goto(random.randint(-280,280),random.randint(-280,280))
score_sign=Turtle("square")
score_sign.color("navy")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0,280)


def move():
    y=head.ycor()
    x=head.xcor()
    if head.direction == "up":
        head.sety(y+20)
    if head.direction == "down":
        head.sety(y-20)
    if head.direction == "left":
        head.setx(x-20)
    if head.direction == "right":
        head.setx(x+20)

def move_up():
    if head.direction!="down":
        head.direction = "up"
def move_down():
    if head.direction!="up":
        head.direction = "down"
def move_left():
    if head.direction!="right":
        head.direction = "left"
def move_right():
    if head.direction!="left":
        head.direction = "right"

def reset():
    time.sleep(2)
    food.goto(random.randint(-280,280),random.randint(-280,280))
    head.goto(0,0)
    head.direction = ("stop")
    for bodypart in body:
        bodypart.goto(1500,1500)
    body.clear()
    return(0)

screen.onkey(move_up,"w")
screen.onkey(move_down,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")

def main_loop(score,hi_score):
    score_sign.clear()
    score_sign.write(f"Skóre: {score}    Nejvyšší skóre: {hi_score}",align = "center")
    screen.update()
    
# kontrola kolize se stenou
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        score = reset()

# kolize s telem
    for body_part in body:
        if head.distance(body_part) < 20:
            score = reset()

# sezrani jidla
    if head.distance(food) <20:
        food.goto(random.randint(-280,280),random.randint(-280,280))
        # pridani tela
        body_part=Turtle("square")
        body_part.speed(0)
        body_part.color("green")
        body_part.penup()
        body.append(body_part)
        score+=1
        hi_score=score if score>hi_score else hi_score

# vykresleni tela
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)

    if len(body)>0:
        y=head.ycor()
        x=head.xcor()
        body[0].goto(x,y)
    
    move()        
    screen.ontimer(lambda: main_loop(score, hi_score), 100)

main_loop(0,0)
screen.exitonclick()
