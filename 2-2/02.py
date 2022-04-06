# Importing Turtle Graphic module

import turtle

# Define program constants 
WIDTH = 500
HEIGHT = 500

# Create a window where we can show our drawing

screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title("Welcome to my turtle's home")
screen.bgcolor("cyan")

# Creating an instance

my_turtle = turtle.Turtle()


# our turtle attributes

my_turtle.color("red")
my_turtle.shape("turtle")
my_turtle.forward(200)
# my_turtle.speed(10)

# This statement is needed at the end of all turtle programs.
turtle.done()