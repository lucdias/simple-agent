# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Seeking "vehicle" follows the mouse position

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from Vehicle import Vehicle
from Food import Food

def setup():
    global v
    global food
    global grid
    size(640, 360)
    v = Vehicle(width / 2, height / 2)
    print(grid)
    food = Food(50, 50)

def draw():
    background(51)

    mouse = PVector(mouseX, mouseY)

    # Draw an ellipse at the mouse position
    fill(127)
    stroke(200)
    strokeWeight(2)
    ellipse(mouse.x, mouse.y, 48, 48)

    # Call the appropriate steering behaviors for our agents
    v.arrive(food.position)
    v.update()
    v.display()
    food.display()
