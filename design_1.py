import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Black background

# Create a turtle object
spiral = turtle.Turtle()
spiral.speed(0)  # Fastest speed
spiral.width(2)  # Pen width
spiral.hideturtle()

# Color list
colors = ["red", "yellow", "green", "blue", "purple", "cyan"]

# Draw a spiral
for i in range(200):
    spiral.pencolor(colors[i % 6])  # Cycle through colors
    spiral.forward(i * 2)  # Move forward
    spiral.left(59)  # Turn left to create a spiral

# Keep the window open
turtle.done()
