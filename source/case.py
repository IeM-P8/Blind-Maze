import random

class Case():
    def __init__(self, x, y, grid):    
        self.x = x
        self.y = y
        self.grid = grid

        self.visited = False
        self.current = False
        self.key = False
        
        self.walls = [True,True,True,True] # top , right , bottom , left
        
        # neighbors
        self.neighbors = []
        
        self.top = 0
        self.right = 0
        self.bottom = 0
        self.left = 0
        
        self.next_cell = 0

    
    def checkNeighbors(self):
        if self.y >= 0:
            self.top = self.grid[self.y - 1][self.x]
        if self.x + 1 < len(self.grid[0]):
            self.right = self.grid[self.y][self.x + 1]
        if self.y + 1 < len(self.grid):
            self.bottom = self.grid[self.y + 1][self.x]
        if self.x - 1 >= 0:
            self.left = self.grid[self.y][self.x - 1]
        
        if self.top != 0:
            if not self.top.visited:
                self.neighbors.append(self.top)
        if self.right != 0:
            if not self.right.visited:
                self.neighbors.append(self.right)
        if self.bottom != 0:
            if not self.bottom.visited:
                self.neighbors.append(self.bottom)
        if self.left != 0:
            if not self.left.visited:
                self.neighbors.append(self.left)
        
        if len(self.neighbors) > 0:
            self.next_cell = self.neighbors[random.randrange(0,len(self.neighbors))]
            return self.next_cell
        else:
            return False