print("Test Start")
import numpy 
from CubeClass import CubeinSpace
from pathfinding.core.grid import Grid
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.finder.a_star import AStarFinder

layer1 = [[1,1,1,1,1],
          [1,0,0,0,1],
          [1,0,0,0,1],
          [1,0,0,0,1],
          [1,1,1,1,1]]

layer2 = [[1,1,1,1,1],
          [1,1,1,0,1],
          [1,1,0,0,1],
          [1,0,0,0,1],
          [1,1,1,1,1]]

layer3 = [[1,1,1,1,1],
          [1,1,1,1,1],
          [1,1,1,1,1],
          [1,1,1,1,1],
          [1,1,1,1,1]]

print(layer1[1][2])

space = [layer1, layer2, layer3]

print(space[0][1][3])

cube0 = CubeinSpace(0,0,0,0,0,0)

print(cube0.getcoordinates())
print(cube0.getflyable())


grid1 = Grid(matrix = layer1)
grid2 = Grid(matrix = layer2)
grid3 = Grid(matrix = layer3)

# grid = Grid(matrix = matrix)

# threedgrid = Grid 

# start = grid.node(0,0)
# end = grid.node(4,4)

# finder = AStarFinder(diagonal_movement=DiagonalMovement.always)

# path,runs = finder.find_path(start,end,grid)

# print(path)
# print(runs)