import turtle
def spiral(side,turn):
    may = turtle.Turtle()
    may.color("cyan")
    may.width(2)
    may.speed(2)
    for side in range(100):
        may.forward(side)
        may.right(turn)

spiral(50,30)