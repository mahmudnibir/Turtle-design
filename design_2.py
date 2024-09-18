import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the turtle object
spiral = turtle.Turtle()
spiral.speed(0)  # Fastest speed
spiral.width(2)
spiral.hideturtle()

# Color palette for the wave effects
colors = ["#FF5733", "#C70039", "#900C3F", "#581845", "#FFC300", "#DAF7A6"]

# Function to draw a circular wave pattern
def draw_wave(radius, offset_angle):
    for i in range(360):
        spiral.pencolor(colors[i % len(colors)])  # Color cycling
        spiral.circle(radius)  # Draw a circle with given radius
        spiral.left(offset_angle)  # Slight rotation for wave effect
        radius += 0.5  # Gradually increase the radius

# Draw expanding and rotating waves
for i in range(6):
    draw_wave(20, 61)  # Change the initial radius and angle for variety
    spiral.right(60)  # Rotate the entire wave structure

# Keep the window open
turtle.done()
