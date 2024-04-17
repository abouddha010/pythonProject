from turtle import *
import colorsys as cs
tracer(50)
bgcolor('black')
h=0.3
pensize(3)
for i in range(350):
    color(cs.hsv_to_rgb(h,0.9,0.8))
    h+=0.004
    rt(20)
    for j in range(5):
        fd(i)
        rt(100)
        rt(50)
    rt(118)
done()