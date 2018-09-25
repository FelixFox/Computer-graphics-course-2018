from utils import create_lsystem, Position
import turtle

"""

F   -  moving forward
[   - push current posiotion to stack
]   - pop position from stack
+   - rotate to left 
-   - rotate to right

"""

axiom = 'X'
angle = 20
length = 30


def create_turtle():
    sticks = turtle.Turtle()
    sticks.pensize(2)
    sticks.speed(0)
    sticks.up()
    screen = sticks.getscreen()
    
    turtle.setup(1000,1000)
    iter = screen.textinput("Iterations", "Number of iterations:")

    sticks.goto(0, -400)
    sticks.down()
    return sticks, int(iter)


def draw_fractal(axiom='X', angle=angle, length=length, num_iters=5):
    stack = []
    sticks, num_iters = create_turtle()
    screen = sticks.getscreen()
    if num_iters>=8:
        length = 2
        sticks._tracer(0)
    elif num_iters >= 6:
        length = 7
        sticks._delay(0)
    else:
        length = 20
        sticks._delay(2)

    # sticks._tracer(0)
    
    sticks.hideturtle()
    sticks.left(90)

    generated_string = create_lsystem(axiom=axiom, num_iters=num_iters)
    print('Generated string: {}'.format(generated_string))

    for i, char in enumerate(generated_string):
        if char == 'F':
            sticks.forward(length)
        elif char == '+':
            sticks.left(angle)
        elif char == '-':
            sticks.right(angle)
        elif char == '[':
            position = sticks.pos()
            state = Position(position[0], position[1], sticks.heading())
            stack.append(state)
        elif char == ']':
            state = stack.pop()
            position = (state.x, state.y)
            ang = state.angle
            sticks.up()
            sticks.goto(position)
            sticks.setheading(ang)
            sticks.down()

    screen.exitonclick()


if __name__ == "__main__":
    draw_fractal(length=10)
