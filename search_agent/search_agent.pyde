from random import randint
import heapq
import time

class Spot:
    
    def __init__(self, i, j, cost=0, wall=False, food=False) :
        self.i = i
        self.j = j
        self.cost = cost if randint(0,10) > 4 else randint(0,2)
        self.wall = True if randint(0,10) < 1 else wall
        self.food = food
        if self.food:
            self.wall = False
            
        self.c = 255
        self.visited = False
        self.setColor(0)
        
    def setColor(self, stage, col=255):
        if stage == 0:
            if self.food:
                self.c = color(0,255,0)
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
    if frontier:
        u = frontier.pop(0)
        i,j = u
        grid[i][j].visited = True
        grid[i][j].setColor(1, color(255,0,255))   
        if u == e:
            i,j = u
                
            path = backtrace(parent, s, e)
            for i,j in path:
                grid[i][j].setColor(1, color(255,0,0))
                
            grid[i][j].setColor(1, color(0,255,0))
            return True, path
                
        y,x = u
        for v in neighbors(y,x):
            i,j = v
            if v not in frontier and not grid[i][j].visited:
                parent[v] = u
                frontier.append(v)
                i,j = v
                grid[i][j].setColor(1, color(0,0,255))
    
    return False, []
                
                
def heuristic(a, b):
   # Manhattan distance on a square grid
   return abs(a[1] - b[1]) + abs(a[0] - b[0])
              
def custoso(s,e):
    
    if frontier_cost:
        cost, p =heapq.heappop(frontier_cost)
        i,j = p
        grid[i][j].visited = True
        grid[i][j].setColor(1, color(255,0,255))
        if p == e:
            path = backtrace(parent, s, e)
            for i,j in path:
                grid[i][j].setColor(1, color(255,0,0))
            i, j = e
            grid[i][j].setColor(1, color(0,255,0))
            return True, path
        y,x = p
        for next in neighbors(y,x):
            a,b = next
            new_cost = cost_so_far[p] + grid[a][b].cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                prioridade = new_cost
                heapq.heappush(frontier_cost,(prioridade, next))
                parent[next] = p
                grid[a][b].setColor(1, color(0,0,255))
    
    return False, []

def aStar(s,e):
    
    if frontier_cost:
        cost, p =heapq.heappop(frontier_cost)
        i, j = p
        grid[i][j].visited = True
        grid[i][j].setColor(1, color(255,0,255))
        if p == e:
            path = backtrace(parent, s, e)
            for i,j in path:
                grid[i][j].setColor(1, color(255,0,0))
            i, j = e
            grid[i][j].setColor(1, color(0,255,0))
            return True, path
        
        y,x = p
        for next in neighbors(y,x):
            a,b = next
            new_cost = cost_so_far[p] + grid[a][b].cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                prioridade = new_cost + heuristic(e, next)
                heapq.heappush(frontier_cost,(prioridade, next))
                parent[next] = p
                grid[a][b].setColor(1, color(0,0,255))
    
    return False, []


def greedy(s, e):
    if frontier_cost:
        c,u = frontier_cost.pop(0)
        i,j = u
        grid[i][j].visited = True
        grid[i][j].setColor(1, color(255,0,255))   
        if u == e:
            i,j = u
                
            path = backtrace(parent, s, e)
            for i,j in path:
                grid[i][j].setColor(1, color(255,0,0))
                
            grid[i][j].setColor(1, color(0,255,0))
            #print("chegou")
            return True, path
                
        y,x = u
        for v in neighbors(y,x):
            i,j = v
            if v not in came_from and not grid[i][j].visited:
                priority = heuristic(e, v)
                parent[v] = u
                heapq.heappush(frontier_cost, (priority, v))
                came_from[v] = u
                grid[i][j].setColor(1, color(0,0,255))
    
    return False, []

def dfs(s, e):
    if frontier:
        u = frontier.pop(-1)
        i,j = u
        grid[i][j].visited = True
        grid[i][j].setColor(1, color(255,0,255))   
        if u == e:
            i,j = u
                
            path = backtrace(parent, s, e)
            for i,j in path:
                grid[i][j].setColor(1, color(255,0,0))
                
            grid[i][j].setColor(1, color(0,255,0))
            #print(path)
            #print("chegou")
            return True, path
                
        y,x = u
        for v in neighbors(y,x):
            i,j = v
            if v not in frontier and not grid[i][j].visited:
                parent[v] = u
                frontier.append(v)
                i,j = v
                grid[i][j].setColor(1, color(0,0,255))
    
    return False, []

def reset():
    for spots in grid:
        for spot in spots:
            spot.setColor(0)
            spot.visited = False

def printGrid(grid):
    for spots in grid:
        for spot in spots:
            spot.show()    

def init(f):
    global s, e, finish
    global frontier, parent
    global came_from, frontier_cost, cost_so_far, grid
    global old

    s = f
    old = f
        
    i, j = s
    grid[i][j].setColor(1, color(255,165,0))
    
    i,j = e
    grid[i][j].food = False
    grid[i][j].cost = 0
    grid[i][j].setColor(0)
    
    e = randint(0, rows-1), randint(0, cols-1)
    i,j = e
    while f == e or grid[i][j].wall:
        e = randint(0, rows-1), randint(0, cols-1)
        i,j = e
    
    grid[i][j].food = True
    grid[i][j].cost = 0
        
    grid[i][j].setColor(0)
    parent = {}
    frontier = []
    frontier.append(s)
    finish = False
    
    frontier_cost = []
    heapq.heappush(frontier_cost, (0,s))
    came_from = {}
    came_from[s] = None
    cost_so_far = {}
    cost_so_far[s] = 0
    
    

def setup():
    size(600, 600)
    global grid
    global rows, cols
    global scaleX, scaleY
    global frontier, frontier_cost, parent, finish, came_from, cost_so_far, walk
    global s, e
    global old
    rows,cols = 40, 40
    scaleX = width/cols 
    scaleY = height/rows -2
    s = (0,0)
    e = (rows-1,cols-1)
    old = s
    grid = [[Spot(i, j) for j in range(cols)] for i in range(rows)]
    init(s)
    walk = False
    
def goto(old, next):
    iOld, jOld = old
    iNext, jNext = next
    
    grid[iNext][jNext].setColor(1, color(255,165,0))
    grid[iOld][jOld].setColor(1, color(255,0,0))
    
def draw():
    global frontier, parent, s, path
    global finish
    global last
    global walk
    global old
    
    if not finish:
        finish, path = aStar(s, e)
        if finish:
            walk = finish
            s = e
    elif walk and finish:
        next = path.pop(0)
        goto(old, next)
        old = next
        time.sleep(0.2)
        if len(path) == 0:
            walk = False
    else:
        time.sleep(1)
        reset()
        init(e)
        
        #finish = False
        
    background(0)
    printGrid(grid)
            
        
