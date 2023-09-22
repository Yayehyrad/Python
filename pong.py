import turtle
import tkinter


 

class screen:
    wn = turtle.Screen()
    wn.title("pong")
    wn.bgcolor('black')
    wn.setup(width=800,height=600)
    # wn.tracer(0)
    

class paddle:
    def __init__(self , x , y) -> None:
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape('square')
        self.paddle.color('white')
        self.paddle.shapesize(stretch_wid=5 ,stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x , y)
    def paddleUp(self):
        x = self.paddle.ycor()
        x += 20
        self.paddle.sety(x)
    def paddleDown(self):
        x = self.paddle.ycor()
        x -= 20
        self.paddle.sety(x)

class ball:
    def __init__(self) -> None:
        self.tur = turtle.Turtle()
        self.tur.color('white')
        self.tur.shape('circle')
        self.tur.penup()
        self.tur.dx = 2
        self.tur.dy = 2
        self.tur.speed(-1)
        # self.tur.backward(20)


scn = screen()

paddle1 = paddle(-315 , 0)
paddle2 = paddle(315 , 0)
ballm = ball()
scn.wn.listen()
scn.wn.onkeypress(paddle1.paddleUp , "w")
scn.wn.onkeypress(paddle1.paddleDown , "s")
scn.wn.onkeypress(paddle2.paddleUp , "Up")
scn.wn.onkeypress(paddle2.paddleDown , "Down")
 


while True:
    scn.wn.update()

    ballm.tur.sety(ballm.tur.ycor()+ballm.tur.dx)
    ballm.tur.setx(ballm.tur.xcor()+ballm.tur.dy)

    if  abs(ballm.tur.ycor()) > 290:
            if(ballm.tur.ycor() < 0):
                 ballm.tur.sety(-290)
            else:
                 ballm.tur.sety(290)
            ballm.tur.dx *= -1
    if ballm.tur.xcor() > 390:
         ballm.tur.goto(0,0)
         ballm.tur.dy *= -1
    if ballm.tur.xcor() < -390:
         ballm.tur.goto(0,0)
         ballm.tur.dy *= -1
    if ballm.tur.xcor() > 300 and ballm.tur.xcor() < 340 and ballm.tur.ycor() < paddle2.paddle.ycor() + 50 and ballm.tur.ycor()  > paddle2.paddle.ycor() -50:
         ballm.tur.dy *=-1
    if ballm.tur.xcor() < -300 and ballm.tur.xcor() > -340 and ballm.tur.ycor() < paddle1.paddle.ycor() + 50 and ballm.tur.ycor()  > paddle1.paddle.ycor() -50:
         ballm.tur.dy *=-1