import turtle  # importing turtle

"""
Since we are Creating Geometry Game and applying some turtle graphic so lets do some
revision of  turtle so we can get a kick start
"""

"""
Note if we want to see code of any class or Method so what we can do is 
->select that class or function
->then right click and go to the Go To option
->than click Declaration Usage and it will open file where the code corresponding to 
  that class or function is written.
  
  OR

->select that class or function and press CTRL+ALT+B we will get same result 
"""
# Creating Canvas/Turtle Instance
my_turtle = turtle.Turtle()  # Create Arrow/Turtle

my_turtle.penup()  # Pull the pen up -- no drawing when moving.
my_turtle.goto(50, 75)  # Move turtle to an absolute position. (Go to a Certain Co-ordinate)
my_turtle.pendown()  # Pull the pen down -- drawing when moving. Since we want to draw the line now
my_turtle.forward(100)  # Move the Turtle forward by the specified distance. here we done 100 pixel
my_turtle.left(90)  # Turn turtle head (arrow head) left by angle 90 degree
my_turtle.forward(200)  # move the turtle forward by 200 pixels
my_turtle.left(90)  # turn arrow head left by 90 degree
my_turtle.forward(100)  # move the turtle forward by 100 pixels
my_turtle.left(90)  # turn arrow head left by 90 degree
my_turtle.forward(200)  # move the turtle forward by 200 pixels

turtle.done()  # if not written screen will get close automatically Note:-its library name turtle.done()

"""
So we are done we needed this much for our Geometry game if you want to know more about turtle than try to learn using
documentation its really easy to learn this Turtle Module
"""
