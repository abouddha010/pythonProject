import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Hey Amita, Let's celebrate your 12 Years of IT Career!!")

career = turtle.Turtle()

career.shape()

career.shape("arrow")
career.pensize(3)
#career.penup()
#career.goto(-250,-50)
career.pendown()
#career.tracer(50)
career.ht()
for i in range(600):
    color=('red','white','green','blue')
    career.color(color[i%4])
    career.fd(i)
    career.rt(20)
    for i in range(6):
        career.fd(i)
        career.rt(145)
        career.bk(i/2)
        career.lt(180)
career.done()


# while True:
# for side in range(20):
#     career.color('red', 'yellow')
#     career.begin_fill()
#     career.forward(200)
#     career.left(170)
#     career.color('blue', 'green')
#     career.begin_fill()
#     career.forward(210)
#     career.left(170)
#     career.color('gold', 'white')
#     career.begin_fill()
#     career.forward(220)
#     career.left(170)
#     career.color('orange', 'purple')
#     career.begin_fill()
#     career.forward(210)
#     career.left(170)
#     career.color('gold', 'white')
#     career.begin_fill()
#     career.forward(200)
#     career.left(170)
#     career.color('pink', 'silver')
#     career.begin_fill()
#     career.forward(200)
#     career.left(170)
# career.end_fill()
wn.exitonclick()
