import turtle


def koch_snowflake(t, order, size):
    # Koch snowflake drawing
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


def koch_curve(t, order, size):
    #  Koch curve drawing
    if order == 0:
        t.forward(size)
    else:
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        t.right(120)
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)


def draw_koch_snowflake(order, size):
    # turtle initialisation
    window = turtle.Screen()
    window.bgcolor("white")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(0)
    snowflake_turtle.penup()
    snowflake_turtle.goto(-size / 2, -size / 2 * (3**0.5) / 3)
    snowflake_turtle.pendown()

    koch_snowflake(snowflake_turtle, order, size)

    window.exitonclick()


if __name__ == "__main__":
    # order: The order of the Koch snowflake (integer)
    # size: The size of each side of the initial equilateral triangle
    draw_koch_snowflake(order=4, size=300)
