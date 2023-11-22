from LoScreation import VLOScreation
from Worldcreation import CreateWorld
from GBWCpathfinder import GBWC
from CubeClass import CubeinSpace
import time
import copy
import math
from pathfinding.core.grid import Grid
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.finder.a_star import AStarFinder

NewWorld = CreateWorld(50,25,1)
NewWorld.setflyzone(1,1,0,48,23,0)
NewWorld.setwalkzone(1,11,0,48,12,0)
NewWorld.setwalkzone(12,1,0,13,23,0)
NewWorld.setwalkzone(32,1,0,33,23,0)
NewWorld.setfieldzone(1,1,0,11,10,0)
NewWorld.setfieldzone(1,13,0,11,23,0)
NewWorld.setfieldzone(14,1,0,31,10,0)
NewWorld.setfieldzone(14,13,0,31,23,0)
NewWorld.setfieldzone(34,1,0,48,10,0)
NewWorld.setfieldzone(34,13,0,48,23,0)
#NewWorld.setnofieldzone(14,1,0,15,10,0)
NewWorld.setnofieldzone(31,1,0,32,10,0)
NewWorld.setnofieldzone(33,1,0,34,10,0)
NewWorld.setnofieldzone(31,13,0,32,23,0)
NewWorld.setnofieldzone(33,13,0,34,23,0)
#NewWorld.setnoflyzone(14,1,0,15,10,0)
NewWorld.setnoflyzone(31,1,0,31,10,0)
NewWorld.setnoflyzone(34,1,0,34,10,0)
NewWorld.setnoflyzone(31,13,0,31,23,0)
NewWorld.setnoflyzone(34,13,0,34,23,0)
NewWorld.setnofieldzone(1,1,0,2,4,0)
NewWorld.setnoflyzone(1,1,0,2,4,0)
NewWorld.setnofieldzone(1,1,0,4,3,0)
NewWorld.setnoflyzone(1,1,0,4,3,0)
NewWorld.setnofieldzone(20,15,0,22,16,0)
NewWorld.setnoflyzone(20,15,0,22,16,0)
#NewWorld.setnofieldzone(5,5,0,9,9,0)
#NewWorld.setnoflyzone(5,5,0,9,9,0)
NewWorld.setnofieldzone(19,5,0,22,7,0)
NewWorld.setnoflyzone(19,5,0,22,7,0)
NewWorld.setnofieldzone(25,5,0,27,7,0)
NewWorld.setnoflyzone(25,5,0,27,7,0)


class Path_with_VLOS:
    def __init__(self, World):
        self.World = copy.copy(World)
        self.xdim = World.getdimesions()[0]
        self.ydim = World.getdimesions()[1]
        self.zdim = World.getdimesions()[2]

    def of_Field_from_Groundstartpoint(self, Field, GroundposX,GroundposY,GroundposZ, sight_range):

        field_for_while_loop = copy.copy(Field)
        field_to_compare = copy.copy(Field)
        secound_field_to_compare = copy.copy(Field)
        secound_world = copy.deepcopy(self.World)
        VLOS_creation = VLOScreation(self.World)
        GBWCfinder = GBWC(self.World.getWorld())

        walkablecubs = []
        for zline in self.World.getWorld():
            for yline in zline:
                for cube in yline:
                    if cube.getwalkable() == 1:
                        walkablecubs.append(cube)

        walkablecubs_for_wavefront = copy.copy(walkablecubs)


        #-----------------------------------  # generates a wavefront on the walkable spaces to later determine how close a walkspot is to the field in question

        currentwave = copy.copy(Field)
        currentnode = currentwave[0]
        nextwave = []
                
        WaveforntGrid_walkable_cubes = []
        wavecounter = 0
        used_walk_spots_for_wavefront = []
        
        while len(walkablecubs_for_wavefront) > 0:

            wavecounter += 1
            
            while len(currentwave) > 0:


                for temp_y in range(currentnode.getcoordinates()[1]-1,currentnode.getcoordinates()[1]+2):
                    if temp_y >= 0 and temp_y < self.ydim:
                        for temp_x in range(currentnode.getcoordinates()[0]-1,currentnode.getcoordinates()[0]+2):
                            if temp_x >= 0 and temp_x < self.xdim:
                                if self.World.getWorld()[temp_x][temp_y][0].getwalkable() == True:
                                    if used_walk_spots_for_wavefront.__contains__(self.World.getWorld()[temp_x][temp_y][0]) != True:
                                        used_walk_spots_for_wavefront.append(self.World.getWorld()[temp_x][temp_y][0])
                                        if currentwave.__contains__(self.World.getWorld()[temp_x][temp_y][0]) != True:
                                            if nextwave.__contains__(self.World.getWorld()[temp_x][temp_y][0]) != True:
                                                nextwave.append(self.World.getWorld()[temp_x][temp_y][0])
                                                if WaveforntGrid_walkable_cubes.__contains__([self.World.getWorld()[temp_x][temp_y][0], wavecounter]) != True:
                                                    WaveforntGrid_walkable_cubes.append([self.World.getWorld()[temp_x][temp_y][0], wavecounter])
            
                for cube in walkablecubs_for_wavefront:
                    if currentnode.getcoordinates()[0] == cube.getcoordinates()[0] and currentnode.getcoordinates()[1] == cube.getcoordinates()[1]:
                        walkablecubs_for_wavefront.remove(cube)

                currentwave.remove(currentnode)
                if len(currentwave) > 0:
                    currentnode = currentwave[0]


            if len(nextwave) > 0:
                for node in nextwave:
                    currentwave.append(node)

                currentnode = currentwave[0]

                for node in currentwave:
                    if nextwave.__contains__(node) == True:
                        nextwave.remove(node)
   

        print("Wavegrid_walkable_cubes done")

        #-----------------------------------  # walks on wavefront (from start position) until all parts of the field are seen 

        pos_plus_visible_part_of_field = []  # [[currentposition, fieldparts_visible_from_currentposition], ....]
        used_walk_spots = []
        currentposition = [GroundposX,GroundposY,GroundposZ]

        runs = 0
        while len(field_for_while_loop) > 0 and runs <= len(walkablecubs):
            runs += 1
            

            print("still running")
            print(currentposition)

            if isinstance(currentposition, CubeinSpace):                      # ???????????????????????
                
                print(currentposition.getcoordinates())

            used_walk_spots.append(currentposition)

            old_current_pos = copy.copy(currentposition)

            if isinstance(currentposition, CubeinSpace):                      # ???????????????????????
                cp = []
                cp = currentposition.getcoordinates()
                currentposition = cp

            VLOS_creation.VLOS_from_point(currentposition[0],currentposition[1],currentposition[2], sight_range)

            fieldparts_visible_from_currentposition = []

            for zline in self.World.getWorld():
                for yline in zline:
                    for cube in yline:
                        if cube.getVLOS() == 1 and field_to_compare.__contains__(cube):
                            if field_for_while_loop.__contains__(cube):
                                field_for_while_loop.remove(cube)
                            fieldparts_visible_from_currentposition.append(cube)

            pos_plus_visible_part_of_field.append([currentposition, fieldparts_visible_from_currentposition])
            

            temp_currentposition = [currentposition, self.xdim*self.ydim*self.zdim]
            
            if len(field_for_while_loop) > 0:
                for temp_z in range(currentposition[2]-1,currentposition[2]+2):
                    if temp_z >= 0 and temp_z < self.zdim:
                        for temp_y in range(currentposition[1]-1,currentposition[1]+2):
                            if temp_y >= 0 and temp_y < self.ydim:
                                for temp_x in range(currentposition[0]-1,currentposition[0]+2):
                                    if temp_x >= 0 and temp_x < self.xdim:
                                        if self.World.getcube(temp_x,temp_y,temp_z).getwalkable() == 1:
                                            for cube_prio in WaveforntGrid_walkable_cubes:                                                            
                                                if cube_prio[0].getcoordinates()[0] == temp_x and cube_prio[0].getcoordinates()[1] == temp_y:
                                                    if cube_prio[1] < temp_currentposition[1]:
                                                        temp_currentposition = cube_prio

                if temp_currentposition[0] == currentposition:
                    return("Can´t cover field -> sight range to short")
                currentposition = temp_currentposition[0].getcoordinates()
                for cube_prio in WaveforntGrid_walkable_cubes:                                                            
                    if cube_prio[0].getcoordinates()[0] == currentposition[0] and cube_prio[0].getcoordinates()[1] == currentposition[1]:
                        WaveforntGrid_walkable_cubes.remove(cube_prio)

            if old_current_pos == currentposition and len(WaveforntGrid_walkable_cubes) > 0:  # if walked in to a corner get the next best spot in the wavefront
                currentposition_prio = WaveforntGrid_walkable_cubes[0]
                for cube_prio in WaveforntGrid_walkable_cubes:
                    if cube_prio[1] < currentposition_prio[1]:
                        currentposition_prio = cube_prio
                currentposition = currentposition_prio[0]

            else:
        
                if old_current_pos == currentposition and len(field_for_while_loop) > 0:
                    VLOS_creation.VLOSmatrix()
                    return("got stuck here. (the 8 in the matrix)")


        #-----------------------------
        orginal_full_list_of_parts = copy.deepcopy(pos_plus_visible_part_of_field)
        #-----------------------------

        # sort out -----------------------       # sorts which groundpoint can see the most new points in the field


        pos_plus_visible_part_of_field.sort(key=lambda x: len(x[1]), reverse=True)
        pos_plus_visible_part_of_field_sorted = []
        current_double = pos_plus_visible_part_of_field[0]
        while len(current_double[1]) > 0:
            pos_plus_visible_part_of_field_sorted.append(current_double)
            pos_plus_visible_part_of_field.remove(current_double)
            already_see_cubes = []
            for double in pos_plus_visible_part_of_field_sorted:
                for cube in double[1]:
                    if already_see_cubes.__contains__(cube) != True:
                        already_see_cubes.append(cube)
            for double in pos_plus_visible_part_of_field:
                for cube in already_see_cubes:
                    if double[1].__contains__(cube):
                        double[1].remove(cube)
            pos_plus_visible_part_of_field.sort(key=lambda x: len(x[1]), reverse=True)
            if len(pos_plus_visible_part_of_field) > 0:
                current_double = pos_plus_visible_part_of_field[0]
            else:
                current_double = [0,[]]

        """
        pos_plus_visible_part_of_field_sorted = []
        while len(field_to_compare) > 0:
            temp_double = [[], []]
            for double in pos_plus_visible_part_of_field:

                overlap_with_compare_field = 0
                for cube in double[1]:
                    if field_to_compare.__contains__(cube) == True:
                        overlap_with_compare_field += 1

                if overlap_with_compare_field > len(temp_double[1]) and overlap_with_compare_field > 0:
                    temp_double = double

            if len(temp_double[1]) > 0:      
                pos_plus_visible_part_of_field.remove(temp_double)
                pos_plus_visible_part_of_field_sorted.append(temp_double)

            for cube in temp_double[1]:
                if field_to_compare.__contains__(cube):
                    field_to_compare.remove(cube)

        for x in range(len(pos_plus_visible_part_of_field_sorted)-1):
            for cube in pos_plus_visible_part_of_field_sorted[x][1]:
                if pos_plus_visible_part_of_field_sorted[x+1][1].__contains__(cube):
                    pos_plus_visible_part_of_field_sorted[x+1][1].remove(cube)
        #"""

        # --------------  in case the visible areas are not conected split them and save them as sepered pices in the sorted list

        for double in pos_plus_visible_part_of_field_sorted:

            fields = []
            nodelist = copy.copy(double[1])
            if len(nodelist) > 1:
                currentnode = nodelist[0]

            while len(nodelist) > 0 and currentnode != None:
                temp_field_list = []
                temp_field_list.append(currentnode)
                neigboringfieldnodes = []
                neigbors = 1

                while neigbors > 0  and currentnode != None:   

                    for temp_z in range(currentnode.getcoordinates()[2]-1,currentnode.getcoordinates()[2]+2):
                        if temp_z >= 0 and temp_z < self.zdim:
                            for temp_y in range(currentnode.getcoordinates()[1]-1,currentnode.getcoordinates()[1]+2):
                                if temp_y >= 0 and temp_y < self.ydim:
                                    for temp_x in range(currentnode.getcoordinates()[0]-1,currentnode.getcoordinates()[0]+2):
                                        if temp_x >= 0 and temp_x < self.xdim:
                                            if self.World.getWorld()[temp_x][temp_y][temp_z].getfield() == 1:
                                                if temp_field_list.__contains__(self.World.getWorld()[temp_x][temp_y][temp_z]) != True:
                                                    if neigboringfieldnodes.__contains__(self.World.getWorld()[temp_x][temp_y][temp_z]) != True:
                                                        neigboringfieldnodes.append(self.World.getWorld()[temp_x][temp_y][temp_z])

                    for x in neigboringfieldnodes:
                        if temp_field_list.__contains__(x) != True:
                            temp_field_list.append(x)                                        

                    if len(neigboringfieldnodes) == 0:        # all neigboring nodes are entered in to Fields as one and removed from the pool(allfieldnodes)
                        neigbors = 0
                        fields.append(temp_field_list)
                        
                        for x in temp_field_list:
                            if nodelist.__contains__(x) == True:
                                nodelist.remove(x)
                        if len(nodelist) > 0:        
                            currentnode = nodelist[0]
                        else:
                            currentnode = None

                    else:            
                        currentnode = neigboringfieldnodes[0]
                        neigboringfieldnodes.remove(currentnode)  
            
            if len(fields) > 1:

                for field in fields:
                    pos_plus_visible_part_of_field_sorted.insert(pos_plus_visible_part_of_field_sorted.index(double), double[0], field)

                pos_plus_visible_part_of_field_sorted.remove(double)     

        # ---------------------------------  
        pos_plus_visible_part_of_field_sorted.sort(key=lambda x: len(x[1]), reverse=True)
        # ---------------------------------

        #"""    # "Better sorting" 

        #orginal_full_list_of_parts = copy_for_better_paths
        orginal_start_position = [GroundposX,GroundposY,GroundposZ]
        relevant_Groundpositions = []
        relevant_Groundpositions_sorted = []

        for double in pos_plus_visible_part_of_field_sorted:
            relevant_Groundpositions.append(double[0])


         # sorts allways for the nearest Groundposition  ----------------------------------

        Groundgrid = Grid(matrix = NewWorld.get2dwalkmatrixoflevel(0))
        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        current_ground_pos = orginal_start_position
        Ground_pos_plus_distance_to_next = [orginal_start_position, self.xdim*self.ydim*self.zdim]

        if relevant_Groundpositions.__contains__(orginal_start_position):
            relevant_Groundpositions_sorted.append(orginal_start_position)
            relevant_Groundpositions.remove(orginal_start_position)

        while len(relevant_Groundpositions) > 0:

            for Ground_pos in relevant_Groundpositions:

                Groundstart = Groundgrid.node(current_ground_pos[0],current_ground_pos[1])
                Groundend = Groundgrid.node(Ground_pos[0],Ground_pos[1])

                #finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
                G_path,path_len = finder.find_path(Groundstart,Groundend,Groundgrid)
                Groundgrid.cleanup()

                if path_len < Ground_pos_plus_distance_to_next[1]:
                    Ground_pos_plus_distance_to_next = [Ground_pos, path_len]

            relevant_Groundpositions_sorted.append(Ground_pos_plus_distance_to_next[0])
            current_ground_pos = Ground_pos_plus_distance_to_next[0]
            Ground_pos_plus_distance_to_next[1] = self.xdim*self.ydim*self.zdim
            relevant_Groundpositions.remove(Ground_pos_plus_distance_to_next[0])

         #--------------------------------------------------------------------------------

        sorted_ground_pos_plus_fieldpart = []

        for ground_pos in relevant_Groundpositions_sorted:
            for ground_pos_plus_field_part in pos_plus_visible_part_of_field_sorted:
                if ground_pos == ground_pos_plus_field_part[0]:
                    sorted_ground_pos_plus_fieldpart.append(ground_pos_plus_field_part)

        """           # recomienes the "puzzelparts" for less doubel coverage
        ground_position_and_full_fieldpart = []
        #secound_VLOS_creation = VLOScreation(secound_world)

        for ground_pos in sorted_ground_pos_plus_fieldpart:

            currentposition = ground_pos[0]

            VLOS_creation.VLOS_from_point(currentposition[0],currentposition[1],currentposition[2], sight_range)

            fieldparts_visible_from_currentposition = []

            for zline in self.World.getWorld():
                for yline in zline:
                    for cube in yline:
                        if cube.getVLOS() == 1 and field_to_compare.__contains__(cube):
                            fieldparts_visible_from_currentposition.append(cube)

            ground_position_and_full_fieldpart.append([currentposition, fieldparts_visible_from_currentposition])

        # #------------ checks for better combination

        for ground_pos_and_fieldpart in ground_position_and_full_fieldpart:
            temp_combolist = []
            for cube in ground_pos_and_fieldpart[1]:
                temp_combolist.append(cube)
            for ground_pos_and_fieldpart_other in ground_position_and_full_fieldpart:
                if ground_pos_and_fieldpart[0] != ground_pos_and_fieldpart_other[0]:
                    for cube in ground_pos_and_fieldpart_other[1]:
                        temp_combolist.append(cube)
                    faild = 0
                    for cube in field_to_compare:
                        if temp_combolist.__contains__(cube) != True:
                            faild = 1
                            break
                    if faild == 0:
                        ground_position_and_full_fieldpart = [ground_pos_and_fieldpart, ground_pos_and_fieldpart_other]

        #

        if len(ground_position_and_full_fieldpart) > 1:
            for ground_pos_and_fieldpart_current in ground_position_and_full_fieldpart:
                for ground_pos_and_fieldpart_other_than_current in ground_position_and_full_fieldpart:
                    if ground_pos_and_fieldpart_current[0] != ground_pos_and_fieldpart_other_than_current[0]:
                        for cube in secound_field_to_compare:
                            if ground_pos_and_fieldpart_current[1].__contains__(cube) == True and ground_pos_and_fieldpart_other_than_current[1].__contains__(cube) == True:

                                distance_to_current_groundpoint = math.sqrt((ground_pos_and_fieldpart_current[0][0] - cube.getcoordinates()[0])**2 + (ground_pos_and_fieldpart_current[0][1] - cube.getcoordinates()[1])**2)

                                distance_to_other_groundpoint = math.sqrt((ground_pos_and_fieldpart_other_than_current[0][0] - cube.getcoordinates()[0])**2 + (ground_pos_and_fieldpart_other_than_current[0][1] - cube.getcoordinates()[1])**2)

                                if distance_to_other_groundpoint < distance_to_current_groundpoint:
                                    ground_pos_and_fieldpart_current[1].remove(cube)
                                else:
                                    ground_pos_and_fieldpart_other_than_current[1].remove(cube)

        sorted_ground_pos_plus_fieldpart = ground_position_and_full_fieldpart

        #"""

        """ #------------------------------------------

        for ground_pos in relevant_Groundpositions_sorted:
            for ground_pos_plus_field_part in orginal_full_list_of_parts:
                if ground_pos == ground_pos_plus_field_part[0]:
                    sorted_ground_pos_plus_fieldpart.append(ground_pos_plus_field_part)

        sorted_ground_pos_plus_ajusted_fieldpart = copy.deepcopy(sorted_ground_pos_plus_fieldpart)

        for ground_pos_plus_fieldpart_current in sorted_ground_pos_plus_fieldpart:
            ground_pos_current = ground_pos_plus_field_part[0]
            sorted_ground_pos_plus_fieldpart.remove(ground_pos_plus_fieldpart_current)  

            if len(sorted_ground_pos_plus_fieldpart) > 0:
                for ground_pos_plus_fieldpart_other in sorted_ground_pos_plus_fieldpart:
                    ground_pos_other = ground_pos_plus_fieldpart_other[0]

                    doublecubes_with_current = []

                    for cube in ground_pos_plus_fieldpart_current[1]:
                        if ground_pos_plus_fieldpart_other[1].__contains__(cube) == True:
                            doublecubes_with_current.append(cube)

                    for cube in doublecubes_with_current:

                        distance_to_current_groundpoint = math.sqrt((cube.getcoordinates()[0] - ground_pos_current[0])**2 + ((cube.getcoordinates()[1] - ground_pos_current[1])**2))

                        distance_to_other_groundpoint = math.sqrt((cube.getcoordinates()[0] - ground_pos_other[0])**2 + ((cube.getcoordinates()[1] - ground_pos_other[1])**2))

                        if distance_to_other_groundpoint < distance_to_current_groundpoint:
                            for groundpoint_fieldpart in sorted_ground_pos_plus_ajusted_fieldpart:
                                if groundpoint_fieldpart[0] == ground_pos_current:
                                    if groundpoint_fieldpart[1].__contains__(cube) == True:
                                       groundpoint_fieldpart[1].remove(cube)


        #for double in pos_plus_visible_part_of_field_sorted:
            #pos_plus_visible_part_of_field_sorted.remove(double)

        pos_plus_visible_part_of_field_sorted = []

        for double in sorted_ground_pos_plus_ajusted_fieldpart:
            pos_plus_visible_part_of_field_sorted.append(double)
                
                
        #"""



        pos_plus_visible_part_of_field_sorted = sorted_ground_pos_plus_fieldpart


        Groundpositions_plus_Path = []

        for double in pos_plus_visible_part_of_field_sorted:
            if len(double[1]) > 0:
                temp_list = []
                temp_list.append(double[0])
                current_field_part = double[1]

                # to do get better(?) start and end node

                closest_fieldnode_to_groundposition = [0,0,0, 1000000]
                for cube in double[1]:
                    distance_to_groundpoint = math.sqrt((double[0][0] - cube.getcoordinates()[0])**2 + (double[0][1] - cube.getcoordinates()[1])**2)
                    if distance_to_groundpoint < closest_fieldnode_to_groundposition[3]:
                        closest_fieldnode_to_groundposition = [cube.getcoordinates()[0],cube.getcoordinates()[1],cube.getcoordinates()[2], distance_to_groundpoint]


                Startnode = [closest_fieldnode_to_groundposition[0],closest_fieldnode_to_groundposition[1]]
                Endnode = [closest_fieldnode_to_groundposition[0],closest_fieldnode_to_groundposition[1]]

                #""" # see if there is the option for seperate Start/Endnode
                if len(double[1]) > 1:
                    second_closest_fieldnode_to_groundposition = [0,0,0, 1000000]

                    for cube in double[1]:
                        if (cube.getcoordinates()[0],cube.getcoordinates()[1]) != (Startnode[0],Startnode[1]):
                            distance_to_groundpoint = math.sqrt((double[0][0] - cube.getcoordinates()[0])**2 + (double[0][1] - cube.getcoordinates()[1])**2)
                            if distance_to_groundpoint < second_closest_fieldnode_to_groundposition[3]:
                                second_closest_fieldnode_to_groundposition = [cube.getcoordinates()[0],cube.getcoordinates()[1],cube.getcoordinates()[2], distance_to_groundpoint]

                
                cube_next_to_Start_and_End = 0
                if len(double[1]) > 2:
                    
                    for cube in double[1]:
                        if(cube.getcoordinates()[0],cube.getcoordinates()[1]) != (Startnode[0],Startnode[1] and cube.getcoordinates()[0],cube.getcoordinates()[1]) != (second_closest_fieldnode_to_groundposition[0],second_closest_fieldnode_to_groundposition[1]):
                            distance_to_startpoint = math.sqrt((Startnode[0] - cube.getcoordinates()[0])**2 + (Startnode[1] - cube.getcoordinates()[1])**2)
                            distance_to_endpoint = math.sqrt((second_closest_fieldnode_to_groundposition[0] - cube.getcoordinates()[0])**2 + (second_closest_fieldnode_to_groundposition[1] - cube.getcoordinates()[1])**2)

                            if distance_to_startpoint < 1.5 and distance_to_endpoint < 1.5:
                                cube_next_to_Start_and_End = 1

                if cube_next_to_Start_and_End == 1:
                    Endnode = [second_closest_fieldnode_to_groundposition[0],second_closest_fieldnode_to_groundposition[1]]
                #"""
                """
                if len(double[1]) > 1:
                    second_closest_fieldnode_to_groundposition = [0,0,0, 1000000]

                    for cube in double[1]:
                        if (cube.getcoordinates()[0],cube.getcoordinates()[1]) != (Startnode[0],Startnode[1]):
                            distance_to_groundpoint = math.sqrt((double[0][0] - cube.getcoordinates()[0])**2 + (double[0][1] - cube.getcoordinates()[1])**2)
                            if distance_to_groundpoint < second_closest_fieldnode_to_groundposition[3]:
                                second_closest_fieldnode_to_groundposition = [cube.getcoordinates()[0],cube.getcoordinates()[1],cube.getcoordinates()[2], distance_to_groundpoint]

                    Endnode = [second_closest_fieldnode_to_groundposition[0],second_closest_fieldnode_to_groundposition[1]]
                #"""


                path = GBWCfinder.GBWCpath_with_heuristic_and_restep(current_field_part,Startnode[0],Startnode[1],Endnode[0],Endnode[1])
                temp_list.append(path)
                Groundpositions_plus_Path.append(temp_list)

        return Groundpositions_plus_Path

# Tests --------------------------------
"""
testest = Path_with_VLOS(NewWorld)
fields = NewWorld.getfield_lists()
print(testest.of_Field_from_Groundstartpoint(fields[1],12,5,0, 20))

#"""

