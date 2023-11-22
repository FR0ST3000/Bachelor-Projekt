from Worldcreation import CreateWorld
import time
import copy
import math
import random

random.seed(12000)
                                                         # GBWC = Grid based wavefront coverage
                                                         
class GBWC:
    def __init__(self, world):
        self.world = world
        self.xdim = len(world)
        self.ydim = len(world[0])
        self.zdim = len(world[0][0])

    def getdim(self):
        return([self.xdim,self.ydim,self.zdim])


    def GBWCpath(self,Field, StartX, StartY, EndX, EndY):


        for node in Field:                                                                # get the starting point for the wavefront (point with priority 0)
            if node.getcoordinates()[0] == EndX and node.getcoordinates()[1] == EndY:
                currentnode = node
                

        WaveforntGrid = []
        wavecounter = 0
        WaveforntGrid.append([currentnode, wavecounter])
        
        currentwave = []
        currentwave.append(currentnode)
        nextwave = []

        
        while len(Field) > 0:

            wavecounter += 1
            
            # -----------------------
            while len(currentwave) > 0:


                for temp_y in range(currentnode.getcoordinates()[1]-1,currentnode.getcoordinates()[1]+2):
                    if temp_y >= 0 and temp_y < self.ydim:
                        for temp_x in range(currentnode.getcoordinates()[0]-1,currentnode.getcoordinates()[0]+2):
                            if temp_x >= 0 and temp_x < self.xdim:
                                if Field.__contains__(self.world[temp_x][temp_y][0]) == True:
                                            if currentwave.__contains__(self.world[temp_x][temp_y][0]) != True:
                                                if nextwave.__contains__(self.world[temp_x][temp_y][0]) != True:
                                                    nextwave.append(self.world[temp_x][temp_y][0])
                                                    if WaveforntGrid.__contains__([self.world[temp_x][temp_y][0], wavecounter]) != True:
                                                        WaveforntGrid.append([self.world[temp_x][temp_y][0], wavecounter])
                
                for field in Field:
                    if currentnode.getcoordinates()[0] == field.getcoordinates()[0] and currentnode.getcoordinates()[1] == field.getcoordinates()[1]:
                        Field.remove(field)

                currentwave.remove(currentnode)
                if len(currentwave) > 0:
                    currentnode = currentwave[0]

            # -------------------------        
            if len(nextwave) > 0:
                for node in nextwave:
                    currentwave.append(node)

                currentnode = currentwave[0]

                for node in currentwave:
                    if nextwave.__contains__(node) == True:
                        nextwave.remove(node)
   

        print("Wavegrid done")

        # path creation --------------------------
        
        Path = []

        Backupwavefrontgrid = copy.copy(WaveforntGrid)
        retrycounter = 0

        for x in WaveforntGrid:                                                             # set first node
            if x[0].getcoordinates()[0] == StartX and x[0].getcoordinates()[1] == StartY:
                currentpathnode = x[0]

        Path.append(currentpathnode)
        for x in WaveforntGrid:                                                             # remove it from wavefront
            if x[0] == currentpathnode:
                WaveforntGrid.remove(x)

        errorcheck = 0

        while len(WaveforntGrid) > 0 and errorcheck != currentpathnode:


            errorcheck = currentpathnode

            temp_pathnode = [currentpathnode, -1]

            for temp_y in range(currentpathnode.getcoordinates()[1]-1,currentpathnode.getcoordinates()[1]+2):
                if temp_y >= 0 and temp_y < self.ydim:
                    for temp_x in range(currentpathnode.getcoordinates()[0]-1,currentpathnode.getcoordinates()[0]+2):
                        if temp_x >= 0 and temp_x < self.xdim:
                            for nodeplusprio in WaveforntGrid:                                                            
                                if nodeplusprio[0].getcoordinates()[0] == temp_x and nodeplusprio[0].getcoordinates()[1] == temp_y:
                                    if nodeplusprio[1] > temp_pathnode[1]:
                                        temp_pathnode = nodeplusprio
                                    if nodeplusprio[1] == temp_pathnode[1]:
                                        if random.randrange(0,2,1) == 1:
                                            temp_pathnode = nodeplusprio


            currentpathnode = temp_pathnode[0]


            Path.append(currentpathnode)
            for x in WaveforntGrid:                                                             # remove it from wavefront
                if x[0] == currentpathnode:
                    WaveforntGrid.remove(x)

           
            # ...........................................................................................................................................
            if errorcheck == currentpathnode:
              
                print("! Somthing went wrong !")
               
              # ................................................................................................................................................

        
        return Path


    def GBWCpath_withoneretry(self,Field, StartX, StartY, EndX, EndY):


        #Fieldlen = len(Field)


        for node in Field:                                                              # get the starting point for the wavefront (point with priority 0)
            if node.getcoordinates()[0] == EndX and node.getcoordinates()[1] == EndY:
                currentnode = node
                

        WaveforntGrid = []
        wavecounter = 0
        WaveforntGrid.append([currentnode, wavecounter])
        
        currentwave = []
        currentwave.append(currentnode)
        nextwave = []

        
        while len(Field) > 0:

            wavecounter += 1
            
            # -----------------------
            while len(currentwave) > 0:


                for temp_y in range(currentnode.getcoordinates()[1]-1,currentnode.getcoordinates()[1]+2):
                    if temp_y >= 0 and temp_y < self.ydim:
                        for temp_x in range(currentnode.getcoordinates()[0]-1,currentnode.getcoordinates()[0]+2):
                            if temp_x >= 0 and temp_x < self.xdim:
                                if Field.__contains__(self.world[temp_x][temp_y][0]) == True:
                                            if currentwave.__contains__(self.world[temp_x][temp_y][0]) != True:
                                                if nextwave.__contains__(self.world[temp_x][temp_y][0]) != True:
                                                    nextwave.append(self.world[temp_x][temp_y][0])
                                                    if WaveforntGrid.__contains__([self.world[temp_x][temp_y][0], wavecounter]) != True:
                                                        WaveforntGrid.append([self.world[temp_x][temp_y][0], wavecounter])
                
                for field in Field:
                    if currentnode.getcoordinates()[0] == field.getcoordinates()[0] and currentnode.getcoordinates()[1] == field.getcoordinates()[1]:
                        Field.remove(field)

                currentwave.remove(currentnode)
                if len(currentwave) > 0:
                    currentnode = currentwave[0]

            # -------------------------        
            if len(nextwave) > 0:
                for node in nextwave:
                    currentwave.append(node)

                currentnode = currentwave[0]

                for node in currentwave:
                    if nextwave.__contains__(node) == True:
                        nextwave.remove(node)
   

        print("Wavegrid done")

        # path creation --------------------------

        
        Path = []

        Backupwavefrontgrid = copy.copy(WaveforntGrid)
        retrycounter = 0

        for x in WaveforntGrid:                                                             # set first node
            if x[0].getcoordinates()[0] == StartX and x[0].getcoordinates()[1] == StartY:
                currentpathnode = x[0]

        Path.append(currentpathnode)
        for x in WaveforntGrid:                                                             # remove it from wavefront
            if x[0] == currentpathnode:
                WaveforntGrid.remove(x)

        errorcheck = 0

        while len(WaveforntGrid) > 0 and errorcheck != currentpathnode:


            errorcheck = currentpathnode

            temp_pathnode = [currentpathnode, -1]

            for temp_y in range(currentpathnode.getcoordinates()[1]-1,currentpathnode.getcoordinates()[1]+2):
                if temp_y >= 0 and temp_y < self.ydim:
                    for temp_x in range(currentpathnode.getcoordinates()[0]-1,currentpathnode.getcoordinates()[0]+2):
                        if temp_x >= 0 and temp_x < self.xdim:
                            for nodeplusprio in WaveforntGrid:                                                            
                                if nodeplusprio[0].getcoordinates()[0] == temp_x and nodeplusprio[0].getcoordinates()[1] == temp_y:
                                    if nodeplusprio[1] > temp_pathnode[1]:
                                        temp_pathnode = nodeplusprio

            currentpathnode = temp_pathnode[0]


            Path.append(currentpathnode)
            for x in WaveforntGrid:                                                             # remove it from wavefront
                if x[0] == currentpathnode:
                    WaveforntGrid.remove(x)

           
            # ...........................................................................................................................................
            if errorcheck == currentpathnode:
              
                print("! Somthing went wrong !")
               
              # ................................................................................................................................................

        #"""
        if Path[len(Path)-1] == Path[len(Path)-2]  and retrycounter < 1:
            retrycounter += 1
            print("Retry...")
            Path2 = []
            
            WaveforntGrid2 = Backupwavefrontgrid


            for x in WaveforntGrid2:                                                             # set first node
                if x[0].getcoordinates()[0] == StartX and x[0].getcoordinates()[1] == StartY:
                    currentpathnode = x[0]

            Path2.append(currentpathnode)
            for x in WaveforntGrid2:                                                             # remove it from wavefront
                if x[0] == currentpathnode:
                    WaveforntGrid2.remove(x)

            errorcheck = 0

            while len(WaveforntGrid2) > 0 and errorcheck != currentpathnode:


                errorcheck = currentpathnode

                temp_pathnode = [currentpathnode, -1]

                for temp_y in range(currentpathnode.getcoordinates()[1]-1,currentpathnode.getcoordinates()[1]+2):
                    if temp_y >= 0 and temp_y < self.ydim:
                        for temp_x in range(currentpathnode.getcoordinates()[0]-1,currentpathnode.getcoordinates()[0]+2):
                            if temp_x >= 0 and temp_x < self.xdim:
                                for nodeplusprio in WaveforntGrid2:                                                            
                                    if nodeplusprio[0].getcoordinates()[0] == temp_x and nodeplusprio[0].getcoordinates()[1] == temp_y:
                                        if nodeplusprio[1] >= temp_pathnode[1]:
                                            temp_pathnode = nodeplusprio

                currentpathnode = temp_pathnode[0]


                Path2.append(currentpathnode)
                for x in WaveforntGrid2:                                                             # remove it from wavefront
                    if x[0] == currentpathnode:
                        WaveforntGrid2.remove(x)

            
                # ...........................................................................................................................................
                if errorcheck == currentpathnode:
                
                    print("! Somthing went wrong again!")
                
                # ................................................................................................................................................
        #"""
        if retrycounter == 1:
            return Path2
        else: 
            return Path

    def GBWCpath_withrestep(self,Field, StartX, StartY, EndX, EndY):

        for node in Field:                                                              # get the starting point for the wavefront (point with priority 0)
            if node.getcoordinates()[0] == EndX and node.getcoordinates()[1] == EndY:
                currentnode = node
                
        fieldsize = len(Field)

        WaveforntGrid = []
        wavecounter = 0
        WaveforntGrid.append([currentnode, wavecounter])
        
        currentwave = []
        currentwave.append(currentnode)
        nextwave = []

        
        while len(Field) > 0:

            wavecounter += 1
            
            # -----------------------
            while len(currentwave) > 0:


                for temp_y in range(currentnode.getcoordinates()[1]-1,currentnode.getcoordinates()[1]+2):
                    if temp_y >= 0 and temp_y < self.ydim:
                        for temp_x in range(currentnode.getcoordinates()[0]-1,currentnode.getcoordinates()[0]+2):
                            if temp_x >= 0 and temp_x < self.xdim:
                                if Field.__contains__(self.world[temp_x][temp_y][0]) == True:
                                            if currentwave.__contains__(self.world[temp_x][temp_y][0]) != True:
                                                if nextwave.__contains__(self.world[temp_x][temp_y][0]) != True:
                                                    nextwave.append(self.world[temp_x][temp_y][0])
                                                    if WaveforntGrid.__contains__([self.world[temp_x][temp_y][0], wavecounter]) != True:
                                                        WaveforntGrid.append([self.world[temp_x][temp_y][0], wavecounter])
                
                for field in Field:
                    if currentnode.getcoordinates()[0] == field.getcoordinates()[0] and currentnode.getcoordinates()[1] == field.getcoordinates()[1]:
                        Field.remove(field)

                currentwave.remove(currentnode)
                if len(currentwave) > 0:
                    currentnode = currentwave[0]

            # -------------------------        
            if len(nextwave) > 0:
                for node in nextwave:
                    currentwave.append(node)

                currentnode = currentwave[0]

                for node in currentwave:
                    if nextwave.__contains__(node) == True:
                        nextwave.remove(node)
   

        print("Wavegrid done")

        # path creation --------------------------

        
        Path = []

        for x in WaveforntGrid:                                                             # set end node
            if x[0].getcoordinates()[0] == EndX and x[0].getcoordinates()[1] == EndY:
                pathendnode = x[0]

        for x in WaveforntGrid:                                                             # set first node
            if x[0].getcoordinates()[0] == StartX and x[0].getcoordinates()[1] == StartY:
                currentpathnode = x[0]

        Path.append(currentpathnode)
        for x in WaveforntGrid:                                                             # set wavefront priority to negativ (x * (-1))
            if x[0] == currentpathnode:
                x[1] = (x[1]*(-1))

        errorcheck = 0

        while len(WaveforntGrid) > 0 and errorcheck != currentpathnode:


            errorcheck = currentpathnode

            temp_pathnode = [currentpathnode, (-fieldsize - 2)]

            for temp_y in range(currentpathnode.getcoordinates()[1]-1,currentpathnode.getcoordinates()[1]+2):
                if temp_y >= 0 and temp_y < self.ydim:
                    for temp_x in range(currentpathnode.getcoordinates()[0]-1,currentpathnode.getcoordinates()[0]+2):
                        if temp_x >= 0 and temp_x < self.xdim:
                            for nodeplusprio in WaveforntGrid:                                                            
                                if nodeplusprio[0].getcoordinates()[0] == temp_x and nodeplusprio[0].getcoordinates()[1] == temp_y:
                                    if nodeplusprio[1] > temp_pathnode[1]:
                                        temp_pathnode = nodeplusprio

            currentpathnode = temp_pathnode[0]


            Path.append(currentpathnode)
            for x in WaveforntGrid:                                                             # set wavefront priority to negativ (x * (-1))
                if x[0] == currentpathnode:
                    if x[1] >= 0:
                        x[1] = (x[1]*(-1))

            if currentpathnode == pathendnode:
                #print(WaveforntGrid)
                break

        return Path
    
    def GBWCpath_withheuristic(self,Field, StartX, StartY, EndX, EndY):



        for node in Field:                                                              # get the starting point for the wavefront (point with priority 0)
            if node.getcoordinates()[0] == EndX and node.getcoordinates()[1] == EndY:
                currentnode = node
                

        WaveforntGrid = []
        wavecounter = 0
        WaveforntGrid.append([currentnode, wavecounter,0])
        
        currentwave = []
        currentwave.append(currentnode)
        nextwave = []

        
        while len(Field) > 0:

            wavecounter += 1
            
            # -----------------------
            while len(currentwave) > 0:


                for temp_y in range(currentnode.getcoordinates()[1]-1,currentnode.getcoordinates()[1]+2):
                    if temp_y >= 0 and temp_y < self.ydim:
                        for temp_x in range(currentnode.getcoordinates()[0]-1,currentnode.getcoordinates()[0]+2):
                            if temp_x >= 0 and temp_x < self.xdim:
                                if Field.__contains__(self.world[temp_x][temp_y][0]) == True:
                                            if currentwave.__contains__(self.world[temp_x][temp_y][0]) != True:
                                                if nextwave.__contains__(self.world[temp_x][temp_y][0]) != True:
                                                    nextwave.append(self.world[temp_x][temp_y][0])
                                                    if WaveforntGrid.__contains__([self.world[temp_x][temp_y][0], wavecounter]) != True:
                                                        distance_to_endpoint = math.sqrt((temp_y - EndY)**2 + (temp_x - EndX)**2)
                                                        WaveforntGrid.append([self.world[temp_x][temp_y][0], wavecounter, distance_to_endpoint])
                
                for field in Field:
                    if currentnode.getcoordinates()[0] == field.getcoordinates()[0] and currentnode.getcoordinates()[1] == field.getcoordinates()[1]:
                        Field.remove(field)

                currentwave.remove(currentnode)
                if len(currentwave) > 0:
                    currentnode = currentwave[0]

            # -------------------------        
            if len(nextwave) > 0:
                for node in nextwave:
                    currentwave.append(node)

                currentnode = currentwave[0]

                for node in currentwave:
                    if nextwave.__contains__(node) == True:
                        nextwave.remove(node)
   

        print("Wavegrid done")

        # path creation --------------------------

        
        Path = []


        for x in WaveforntGrid:                                                             # set first node
            if x[0].getcoordinates()[0] == StartX and x[0].getcoordinates()[1] == StartY:
                currentpathnode = x[0]

        Path.append(currentpathnode)
        for x in WaveforntGrid:                                                             # remove it from wavefront
            if x[0] == currentpathnode:
                WaveforntGrid.remove(x)

        errorcheck = 0

        while len(WaveforntGrid) > 0 and errorcheck != currentpathnode:


            errorcheck = currentpathnode

            temp_pathnode = [currentpathnode, -1, -1]

            for temp_y in range(currentpathnode.getcoordinates()[1]-1,currentpathnode.getcoordinates()[1]+2):
                if temp_y >= 0 and temp_y < self.ydim:
                    for temp_x in range(currentpathnode.getcoordinates()[0]-1,currentpathnode.getcoordinates()[0]+2):
                        if temp_x >= 0 and temp_x < self.xdim:
                            for nodeplusprio in WaveforntGrid:                                                            
                                if nodeplusprio[0].getcoordinates()[0] == temp_x and nodeplusprio[0].getcoordinates()[1] == temp_y:
                                    if nodeplusprio[1] > temp_pathnode[1]:
                                        temp_pathnode = nodeplusprio
                                    
                                    if nodeplusprio[1] == temp_pathnode[1]:
                                        if nodeplusprio[2] > temp_pathnode[2]:
                                            temp_pathnode = nodeplusprio

            currentpathnode = temp_pathnode[0]


            Path.append(currentpathnode)
            for x in WaveforntGrid:                                                             # remove it from wavefront
                if x[0] == currentpathnode:
                    WaveforntGrid.remove(x)

           
            # ...........................................................................................................................................
            if errorcheck == currentpathnode:
              
                print("! Somthing went wrong !")
               
              # ................................................................................................................................................

        
        return Path

# ----------------------------------------------------------------------

    def GBWCpath_with_heuristic_and_restep(self,Field, StartX, StartY, EndX, EndY):

        currentnode = None

        for node in Field:                                                              # get the starting point for the wavefront (point with priority 0)
            if node.getcoordinates()[0] == EndX and node.getcoordinates()[1] == EndY:
                currentnode = node

        if currentnode == None:
            return "no endpoint found"
                
        fieldsize = len(Field)

        WaveforntGrid = []
        wavecounter = 0
        WaveforntGrid.append([currentnode, wavecounter,0])
        
        currentwave = []
        currentwave.append(currentnode)
        nextwave = []

        old_field_len = 0
        new_field_len = 1
        
        while len(Field) > 0 and old_field_len != new_field_len:

            old_field_len = copy.copy(len(Field))

            wavecounter += 1
            
            # -----------------------
            while len(currentwave) > 0:


                for temp_y in range(currentnode.getcoordinates()[1]-1,currentnode.getcoordinates()[1]+2):
                    if temp_y >= 0 and temp_y < self.ydim:
                        for temp_x in range(currentnode.getcoordinates()[0]-1,currentnode.getcoordinates()[0]+2):
                            if temp_x >= 0 and temp_x < self.xdim:
                                if Field.__contains__(self.world[temp_x][temp_y][0]) == True:
                                            if currentwave.__contains__(self.world[temp_x][temp_y][0]) != True:
                                                if nextwave.__contains__(self.world[temp_x][temp_y][0]) != True:
                                                    nextwave.append(self.world[temp_x][temp_y][0])
                                                    if WaveforntGrid.__contains__([self.world[temp_x][temp_y][0], wavecounter]) != True:
                                                        distance_to_endpoint = math.sqrt((temp_y - EndY)**2 + (temp_x - EndX)**2)
                                                        WaveforntGrid.append([self.world[temp_x][temp_y][0], wavecounter, distance_to_endpoint])
                
                for cube in Field:
                    if currentnode.getcoordinates()[0] == cube.getcoordinates()[0] and currentnode.getcoordinates()[1] == cube.getcoordinates()[1]:
                        Field.remove(cube)

                new_field_len = copy.copy(len(Field))

                currentwave.remove(currentnode)
                if len(currentwave) > 0:
                    currentnode = currentwave[0]

            # -------------------------        
            if len(nextwave) > 0:
                for node in nextwave:
                    currentwave.append(node)

                currentnode = currentwave[0]

                for node in currentwave:
                    if nextwave.__contains__(node) == True:
                        nextwave.remove(node)
   

        print("Wavegrid done")

        # path creation --------------------------

        
        Path = []

        for x in WaveforntGrid:                                                             # set end node
            if x[0].getcoordinates()[0] == EndX and x[0].getcoordinates()[1] == EndY:
                pathendnode = x[0]

        for x in WaveforntGrid:                                                             # set first node
            if x[0].getcoordinates()[0] == StartX and x[0].getcoordinates()[1] == StartY:
                currentpathnode = x[0]

        Path.append(currentpathnode)
        for x in WaveforntGrid:                                                             # set wavefront priority to negativ (x * (-1))
            if x[0] == currentpathnode:
                x[1] = (x[1]*(-1))

        errorcheck = 0

        while len(WaveforntGrid) > 0 and errorcheck != currentpathnode:


            errorcheck = currentpathnode

            temp_pathnode = [currentpathnode, (-fieldsize - 2)]

            for temp_y in range(currentpathnode.getcoordinates()[1]-1,currentpathnode.getcoordinates()[1]+2):
                if temp_y >= 0 and temp_y < self.ydim:
                    for temp_x in range(currentpathnode.getcoordinates()[0]-1,currentpathnode.getcoordinates()[0]+2):
                        if temp_x >= 0 and temp_x < self.xdim:
                            for nodeplusprio in WaveforntGrid:                                                            
                                if nodeplusprio[0].getcoordinates()[0] == temp_x and nodeplusprio[0].getcoordinates()[1] == temp_y:
                                    if nodeplusprio[1] > temp_pathnode[1]:
                                        temp_pathnode = nodeplusprio

                                    if nodeplusprio[1] == temp_pathnode[1]:
                                        if nodeplusprio[2] > temp_pathnode[2]:
                                            temp_pathnode = nodeplusprio

            currentpathnode = temp_pathnode[0]


            Path.append(currentpathnode)
            for x in WaveforntGrid:                                                             # set wavefront priority to negativ (x * (-1))
                if x[0] == currentpathnode:
                    if x[1] >= 0:
                        x[1] = (x[1]*(-1))
                        x[2] = (x[2]*(-1))

            if currentpathnode == pathendnode:
                #print(WaveforntGrid)
                break

        return Path
                        
# Tests -----------------------------------------------------------------------------------------------

#starttime = time.time()
#NewWorld = CreateWorld(26,13,1)

#NewWorld.setnofieldzone(9,0,0,9,9,0)
#NewWorld.setnofieldzone(0,9,0,9,9,0)
#NewWorld.setnofieldzone(4,4,0,8,8,0)
#NewWorld.setfieldzone(0,0,0,3,3,0)
#NewWorld.setnofieldzone(1,1,0,2,2,0)

#fields = NewWorld.getfield_lists()
#print(fields[0])
#GBWCthing = GBWC(NewWorld.getWorld())
#wavegrid = GBWCthing.GBWCpath_withrestep(fields[0],0,0,3,3)
"""
print(wavegrid)
for x in fields[0]:
    print(x.getcoordinates())
print("---")
for x in wavegrid:
    print(x[0].getcoordinates())

print(GBWCthing.getdim())
coount = 0
for x in wavegrid:
    coount += 1
print(coount)
"""

#print(wavegrid)

#for node in wavegrid:
   # print(node.getcoordinates())
#print(len(wavegrid))

#endtime = time.time()
#timedif = endtime - starttime
#print("Time: "+ str(timedif)+"sec")


