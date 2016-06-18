import turtle

def draw_square(some_turtle):
    i = 0
    while i < 4:
        some_turtle.forward(100)
        some_turtle.right(90)
        i = i + 1


def draw_shape():
  window = turtle.Screen()
  window.bgcolor("maroon")

  #create the turtle Henry - Draws a square
  henry = turtle.Turtle()
  henry.shape("turtle")
  henry.color("white")
  henry.speed(5)
  for i in range(1,36):
      draw_square(henry)
      henry.right(10)

  #create the turtle Sophie - Draws a circle
  sophie = turtle.Turtle()
  sophie.shape("arrow")
  sophie.color("black")
  sophie.circle(70)

  window.exitonclick()

draw_shape()
