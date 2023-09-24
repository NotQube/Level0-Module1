import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    chicken = turtle.Turtle()
    
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title='question', prompt="what shape do you want to draw?")
    radius = 250
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "square":
        for i in range(4):
            turtle.right(90)
            turtle.forward(300)
    if shape == "triangle":
        for i in range(3):
            turtle.right(120)
            turtle.forward(300)
    if shape == "circle":
        chicken.circle(radius=radius)


    
    # Call the turtle .done() method
