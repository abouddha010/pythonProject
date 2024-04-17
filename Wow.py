import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Hey Amita, Let's celebrate your 12 Years of IT Career!!")

career = turtle.Turtle()

career.shape()

career.shape("arrow")
career.pensize(5)
# career.pencolor("orange")
career.penup()
career.goto(-250,-50)
career.pendown()
career.speed(-10)
# career.circle(80, steps=4)
for side in range(6):
    # career.pencolor("blue")
    # career.fd(10)
    # career.circle(100, steps=4)
    # career.pencolor("white")
    # career.fd(20)
    # career.circle(120, steps=4)
    #career.lt(10)
    # career.pencolor("red")
    # career.fd(30)
    # career.circle(140, steps=4)
    # career.pencolor("orange")
    # career.fd(40)
    # career.circle(160, steps=4)

    career.color('red', 'yellow')
    career.begin_fill()
    while True:
        career.forward(200)
        career.left(170)
        if abs(career.pos()) < 1:
            break
    career.end_fill()
    career.done()
wn.exitonclick()
