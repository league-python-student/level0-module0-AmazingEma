import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # This code makes a new Turtle. Pick a new name for the turtle
    t = turtle.Turtle()
    
    # Make your turtle's shape 'turtle', .shape('turtl
    t.shape('turtle')

    # Set your turtle's speed using .speed(2)
    t.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    t.color('green')
    t.pencolor('blue')
    # Move your turtle forward using .forward(100)
    for i in range(4) :
        t.forward(100)
        t.left(90)
    
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    t.goto(-300, 300)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    t.begin_fill()
    t.circle(100, 360, 30)
    t.end_fill()
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    t.color('pink')
    t.penup()
    t.goto(-50,50)
    t.pendown()
    t.circle(50,600,10)


    # Draw 3 more shapes with different fill colors!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
