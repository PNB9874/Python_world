import turtle
turtle.title("sixteen petals Flower")
turtle.setworldcoordinates(-2000,-2000,2000,2000)

def draw_flowers(x,y,tilt,radius):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(tilt-45)
    turtle.circle(radius,90)
    turtle.left(90)
    turtle.circle(radius,90)

for tilt in range(0,260,30):
    draw_flowers(0,0,tilt,1000)
