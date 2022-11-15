import random
import source.const as const
import source.case as case

def maze_gen():
    size = (const.MAP_WIDTH, const.MAP_HEIGHT)

    done = False

    cols = size[0]
    rows = size[1]

    stack = []
    grid = []

    for y in range(rows):
        grid.append([])
        for x in range(cols):
            grid[y].append(case.Case(x,y,grid))

    current_cell = grid[0][0]
    next_cell = 0

    # Boucle de l'algo
    while True:
        current_cell.visited = True
        current_cell.current = True
        
        next_cell = current_cell.checkNeighbors()
        
        if next_cell != False:
            current_cell.neighbors = []
            
            stack.append(current_cell)
            removeWalls(current_cell, next_cell)
            
            current_cell.current = False
            
            current_cell = next_cell
        
        elif len(stack) > 0:
            current_cell.current = False
            current_cell = stack.pop()
            
        elif len(stack) == 0:
            break
    
    # Ajout d'une clé
    key_cell = grid[random.randint(1, rows - 2)][random.randint(1, cols - 2)]
    key_cell.key = True

    # Terrain de jeu terminé
    return grid


def removeWalls(current_cell,next_cell):
    d_x = current_cell.x - next_cell.x
    d_y = current_cell.y - next_cell.y
    if d_x == -1: # À droite de current
        current_cell.walls[1] = False
        next_cell.walls[3] = False
    elif d_x == 1: # À gauche de current
        current_cell.walls[3] = False
        next_cell.walls[1] = False
    elif d_y == -1: # En dessous de current
        current_cell.walls[2] = False
        next_cell.walls[0] = False
    elif d_y == 1: # Au dessus de current
        current_cell.walls[0] = False
        next_cell.walls[2] = False

if __name__ == "__main__":
    # Retirer le package source dans les imports
    print(maze_gen())