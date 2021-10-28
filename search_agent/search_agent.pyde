from random import randint

class Spot:
    
    def __init__(self, i, j, cost=0, wall=False, food=False) :
        self.i = i
        self.j = j
        self.cost = cost if randint(0,10) > 4 else randint(0,2)
        self.wall = True if randint(0,10) < 1 else wall
        self.food = False
        self.c = 255
        self.visited = False
        self.setColor(0)
        
    def setColor(self, stage, col=255):
        if stage == 0:
            if self.food:
                self.c = 50
            elif self.wall:
                self.c = 0
            elif self.cost  == 0:
                self.c = 255
            elif self.cost == 1:
                self.c = color(255,255,0)
            elif self.cost == 2:
                self.c = color(127,0,0)
        else:
            self.c = col
        
    def show(self):
        if self.food:
            fill(self.c)
        elif self.wall:
            fill(self.c)
        elif self.cost  == 0:
            fill(self.c)
        elif self.cost == 1:
            fill(self.c)
        elif self.cost == 2:
            fill(self.c)
            
        stroke(0)
        #print(scaleX, scaleY)
        rect(self.j*scaleX, self.i*scaleY, scaleX, scaleY)


def backtrace(parent, start, e):
    path = [e]
    while path[-1] != start:
        print(path)
        path.append(parent[path[-1]])
    path.reverse()
    return path   

def neighbors(i, j):
    r = [-1,-1,-1, 0, 0, +1, +1, +1]
    c = [-1, 0, +1, -1, +1, -1, 0,  +1]
    ret = []
    for k in range(8):
        y, x = i+r[k], j+c[k]
        if ( 0 <= y < rows) and ( 0 <= x < cols) and not grid[y][x].wall:
            ret.append((y, x))
    return ret

def bfs(s, e):
    parent = {}
    frontier = []
    frontier.append(s)
    
    while frontier:
        u = frontier.pop(0)
        i,j = u
        grid[i][j].visited = True
        
        if u == e:
            i,j = u
            
            path = backtrace(parent, s, e)
            for i,j in path:
                grid[i][j].setColor(1, color(255,0,0))
                grid[i][j].show()
            
            grid[i][j].setColor(1, color(0,255,0))
            grid[i][j].show()
            print(path)
            print("chegou")
            return True
        y,x = u
        for v in neighbors(y,x):
            i,j = v
            if v not in frontier and not grid[i][j].visited:
                parent[v] = u
                frontier.append(v)
                i,j = v
                grid[i][j].setColor(1, color(0,0,255))
                grid[i][j].show()
                 
    
    

def setup():
    size(1000, 600)
    global grid
    global rows, cols
    global scaleX, scaleY
    global babaca
    babaca = False
    rows,cols = 100,100
    scaleX = width/cols
    scaleY = height/rows
    
    #lines 
    #cols
    
    grid = [[Spot(i, j) for j in range(cols)] for i in range(rows)]
    foodY, foodX = randint(0,rows-1), randint(0,cols-1)
    grid[foodY][foodX].food = True
    print(neighbors(0,0))
    
def draw():
    global babaca
    for spots in grid:
        for spot in spots:
            spot.show()
    if not babaca:
        babaca = bfs((0,0), (70,87))
    
