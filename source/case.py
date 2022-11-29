import random
import pygame

class Case():
    def __init__(self, x, y, grid):    
        self.x = x
        self.y = y
        self.grid = grid

        self.visited: bool = False
        self.current: bool = False
        self.key: bool = False
        self.ennemi: bool = False
        
        self.walls: list[bool] = [True,True,True,True] # top , right , bottom , left
        
        # neighbors
        self.neighbors = []
        
        self.top: Case | None = None
        self.right: Case | None = None
        self.bottom: Case | None = None
        self.left: Case | None = None
        
        self.next_cell = 0

    
    def checkNeighbors(self):
        if self.y > 0:
            self.top = self.grid[self.y - 1][self.x]
        if self.x + 1 < len(self.grid[0]):
            self.right = self.grid[self.y][self.x + 1]
        if self.y + 1 < len(self.grid):
            self.bottom = self.grid[self.y + 1][self.x]
        if self.x > 0:
            self.left = self.grid[self.y][self.x - 1]
        
        if self.top:
            if not self.top.visited:
                self.neighbors.append(self.top)
        if self.right:
            if not self.right.visited:
                self.neighbors.append(self.right)
        if self.bottom:
            if not self.bottom.visited:
                self.neighbors.append(self.bottom)
        if self.left:
            if not self.left.visited:
                self.neighbors.append(self.left)
        
        if len(self.neighbors) > 0:
            self.next_cell = self.neighbors[random.randrange(0,len(self.neighbors))]
            return self.next_cell
        else:
            return None