import turtle


colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']


pen = turtle.Pen()

pen.speed(10)
turtle.bgcolor('black')


for x in range(360):
    pen.pencolor(colors[x%6])
    pen.width(x//100 + 1)
    pen.forward(x)
    pen.left(59)

turtle.done()
