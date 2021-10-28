from random import randint


class Spot:
    
    def __init__(self, i, j, cost=0, wall=False, food=False) :
        self.i = i
        self.j = j
        self.cost = cost if randint(0,10) > 4 else randint(0,2)
        self.wall = True if randint(0,10) < 2 else wall
        self.food = False
        
    def show(self):
        if self.food:
            fill(50)
        elif self.wall:
            fill(0)
        elif self.cost  == 0:
            fill(255)
        elif self.cost == 1:
            fill(color(255,255,0))
        elif self.cost == 2:
            fill(color(127,0,0))
            
        stroke(0)
        #print(scaleX, scaleY)
        rect(self.j*scaleX, self.i*scaleY, scaleX, scaleY)
    

def neighbors(i, j):
    r = [-1,-1,-1, 0, 0, +1, +1, +1]
    c = [-1, 0, +1, -1, +1, -1, 0,  +1]
    ret = []
    for k in range(8):
        y, x = i+r[k], j+c[k]
        if ( 0 <= y < rows) and ( 0 <= x < cols):
            ret.append((y, x))
    return ret

def setup():
    size(640, 480)
    global grid
    global rows, cols
    global scaleX, scaleY
    rows,cols = 5,5
    scaleX = width/cols
    scaleY = height/rows
    
    #lines 
    #cols
    
    grid = [[Spot(i, j) for j in range(cols)] for i in range(rows)]
    foodY, foodX = randint(0,rows-1), randint(0,cols-1)
    grid[foodY][foodX].food = True
    print(neighbors(0,0))
    
def draw():
    for spots in grid:
        for spot in spots:
            spot.show()
    
