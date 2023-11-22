import random
import Worldcreation
import CubeClass
from CubeClass import CubeinSpace
from Worldcreation import CreateWorld
from GBWCpathfinder import GBWC
import time
import copy
import math
from pathwitklos import Path_with_VLOS
from LoScreation import VLOScreation
from Worldcreation import CreateWorld
from GBWCpathfinder import GBWC
from CubeClass import CubeinSpace
from pathfinding.core.grid import Grid
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.finder.a_star import AStarFinder
from LoScreation import VLOScreation


random.seed(9000)

combienelist = []               # combinelist[x] = [2dflymap, field as list of cubes, GBWCpath of the field, time of GBWCpath creation, GBWCpath_heuristic/restep of the field, time of GBWCpath_heuristic/restep creation, doubled covered cubes]
faild_fields = 0                #  to DO: path lenght as line  cube1 -> cube2 -> cube3 -> .....

while len(combienelist) < 10:

    NewWorld = CreateWorld(17,12,1)
    NewWorld.setfieldzone(1,1,0,15,10,0)
    NewWorld.setflyzone(1,1,0,15,10,0)
    NewWorld.setwalkzone(0,0,0,16,0,0)
    NewWorld.setwalkzone(0,0,0,0,11,0)
    NewWorld.setwalkzone(0,11,0,16,11,0)
    NewWorld.setwalkzone(16,0,0,16,11,0)
    NewWorld.setflyzone(0,0,0,16,0,0)
    NewWorld.setflyzone(0,0,0,0,11,0)
    NewWorld.setflyzone(0,11,0,16,11,0)
    NewWorld.setflyzone(16,0,0,16,11,0)


    Amount_of_Obstacles = 0 # random.randrange(0,4,1)           # Number of Obstacles

    i = 0                                                   # Obstacle creation
    while i < Amount_of_Obstacles:
        i += 1

        Obstacle_startX = random.randrange(1,15,1)
        Obstacle_startY = random.randrange(1,10,1)

        Obstacle_endX = random.randrange(int(Obstacle_startX),15,1)
        Obstacle_endY = random.randrange(int(Obstacle_startY),11,1)

        NewWorld.setnofieldzone(Obstacle_startX,Obstacle_startY,0,Obstacle_endX,Obstacle_endY,0)
        NewWorld.setnoflyzone(Obstacle_startX,Obstacle_startY,0,Obstacle_endX,Obstacle_endY,0)

    fields = NewWorld.getfield_lists()
    NewWorld.getdimesions()

    if len(fields) > 1:
        faild_fields += 1
    else:
        temp_list = []
        temp_list.append(NewWorld.get2dflymatrixoflevel(0))
        temp_list.append(fields[0])

        
        #path_w_VLOS = Path_with_VLOS(NewWorld)

        #copyed_field_1 = copy.copy(fields[0])
        

        # -------------------------------- with VLOS

        #groundstartpoint = [5,0,0]
        los = VLOScreation(NewWorld)
        los.VLOS_from_point(0,0,0, 20)
        print(los.VLOSmatrix())
        testest = Path_with_VLOS(NewWorld)
        fields = NewWorld.getfield_lists()
        print(testest.of_Field_from_Groundstartpoint(fields[0],0,0,0, 15))

        #print("Time for paths_VLOS creation: " + str(round(temp_list[5], 2)) + " sec")



        combienelist.append(temp_list)

    """     # prints the fields out
    for x in NewWorld.get2dflymatrixoflevel(0):
        print(x)
    print("-------------------------------------------")
    #"""
#"""
for list in combienelist:
    print("--------------------------------")
    for x in list[0]:
        print(x)

print("faild fields: " + str(faild_fields))
#"""

#--------------------------------------------------------- ploting values: -----------------

print("---------------------------------------------")

#Time:

