import turtle
win=turtle.Turtle()
#win.hideturtle()
X=0
Y=0
win.speed(10)
win.pencolor("GREEN")
win.screen.bgcolor("black")
win.write(0,0)
'''
for i in range(0,360):
    win.forward(1)
    win.setheading(i)'''
win.penup()
win.goto(0,-100)

win.pendown()
win.begin_fill()
win.circle(100)
win.fillcolor("red")
win.penup()
win.goto(0,0)
win.goto(0,-60)
win.pendown()
win.penup()
win.circle(60)
win.end_fill()


win.home()
