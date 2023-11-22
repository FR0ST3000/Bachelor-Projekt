print("Test Start")
from pathfinding.core.grid import Grid
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.finder.a_star import AStarFinder

matrix = [[1,1,1,1,1],
          [1,0,1,0,1],
          [1,1,0,1,1],
          [1,0,0,0,1],
          [1,1,1,1,1]]

grid = Grid(matrix = matrix)

# threedgrid = Grid 

for x in range(6):
    print(x)
    
start = grid.node(0,0)
end = grid.node(4,4)

finder = AStarFinder(diagonal_movement=DiagonalMovement.always)

path,runs = finder.find_path(start,end,grid)

print(path)
print(runs)