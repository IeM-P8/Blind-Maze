import random
import pygame
import source.const as const
import source.case as case

def maze_gen():
    size = (const.MAP_WIDTH, const.MAP_HEIGHT)

    cols = size[0]
    rows = size[1]

    stack = []
    grid = []

    for y in range(rows):
        grid.append([])
        for x in range(cols):
            grid[y].append(case.Case(x,y,grid))

    current_cell: case.Case = grid[0][0]
    next_cell: case.Case | None = None

    # Boucle de l'algo
    while True:
        current_cell.visited = True
        current_cell.current = True
        
        next_cell = current_cell.checkNeighbors()
        
        if next_cell:
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
    key_cell: case.Case = grid[random.randint(1, rows - 2)][random.randint(1, cols - 2)]
    key_cell.key = True

    # Ajout de deux ennemis
    l_ennemis:list[case.Case] = []

    for _ in range(const.AMOUNT_ENNEMIES):
        ennemi_cell: case.Case = grid[random.randint(1, rows - 2)][random.randint(1, cols - 2)]
        if ennemi_cell not in l_ennemis and ennemi_cell != key_cell:
            ennemi_cell.ennemi = True
            l_ennemis.append(ennemi_cell)

    # Terrain de jeu terminé
    return grid, key_cell, l_ennemis


def removeWalls(current_cell: case.Case, next_cell: case.Case):
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