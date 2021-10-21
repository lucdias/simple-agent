# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Seeking "vehicle" follows the mouse position

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from Vehicle import Vehicle
from Food import Food
from random import randint

def setup():
    global v
    global food
    global grid
    global f
    global cnt
    cnt = 0
    size(640, 360)
    v = Vehicle(width / 2, height / 2)
    food = Food(50, 50)
    f = createFont("ubuntu", 16)
    
def draw():
    background(51)
    global f, cnt
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
    ret = food.checkVehicle(v.position)
    textFont(f, 16)
    if(ret):
        x,y = randint(0, width), randint(0, height)
        food.setPosition(x,y)
        cnt += 1
    text("Catched: {}".format(cnt),10,20)
    
