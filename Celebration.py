from turtle import *
import colorsys as cs
tracer(50)
bgcolor('black')
h=0.3
pensize(3)
for i in range(600):
    color(cs.hsv_to_rgb(h, 0.9, 1))
    h += 0.005
    fd(i)
    rt(20)
    for i in range(6):
        fd(i)
        rt(145)
        lt(180)
goto(-200,-50)
for i in range(350):
    color(cs.hsv_to_rgb(h,0.9,1))
    h+=0.005
    rt(20)
    for j in range(5):
        fd(i)
        rt(100)
        rt(50)
    rt(118)
goto(200,50)
for i in range(600):
    color(cs.hsv_to_rgb(h, 0.7, 0.9))
    h += 0.025
    fd(i)
    rt(20)
    for i in range(6):
        fd(i)
        rt(145)
        lt(180)
done()