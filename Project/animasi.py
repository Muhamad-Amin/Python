import turtle

def draw_petal(t, size):
  for i in range(20):
    t.forward(size)
    t.right(123)

def draw_flower(t, num_petals, size):
  for i in range(num_petals):
    draw_petal(t, size)
    t.left(360 / num_petals)

window = turtle.Screen()
window.bgcolor("white")

tess = turtle.Turtle()
tess.color("red")
tess.pensize(3)

draw_flower(tess, 10, 60)

window.exitonclick()
