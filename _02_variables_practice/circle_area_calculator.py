import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    radius = simpledialog.askinteger(title='question', prompt="what is the radius in pixels?")

    
    # Make a new turtle
    chicken = turtle.Turtle()
    
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    chicken.circle(radius=radius)

    # Call the turtle .penup() method
    chicken.penup()

    # Move your turtle to a new x,y position using .goto()
    chicken.goto(x=-45, y=32)

    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = math.pi * radius * radius




    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    chicken.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))

    # Hide your turtle
    chicken.hideturtle()

    # Call turtle.done()
    turtle.done()
