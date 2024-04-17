from turtle import *
import colorsys as cs
tracer(50)
bgcolor('black')
title("Hey Amita, Let's celebrate your 12 Years of IT Career!!")
h=0.3
pensize(3)
setup(800,800)
penup()
name = input("Enter your name: ")
#Type Hey Amita
goto(-270, 300)
color('white')
style = ('Courier', 20, 'italic')
write('Hey', font=style, align='right', move=True)

goto(-200, 300)
color('grey')
style = ('Courier', 20, 'italic')
write(name, font=style, align='right', move=True)

#Type Congratulations
goto(-210, 260)
color('blue')
style = ('Courier', 20, 'italic')
write("Congratulations", font=style, align='right', move=True)
hideturtle()

#Cracker
goto(40,-40)
pendown()
for i in range(610):
    color(cs.hsv_to_rgb(h, 0.9, 1))
    h += 0.005
    fd(i)
    rt(20)
    for i in range(6):
        fd(i)
        rt(145)
        lt(180)
done()