from CubeClass import CubeinSpace

class CreateWorld:
    def __init__(self, xdim, ydim, zdim):
        self.xdim = int(xdim)
        self.ydim = int(ydim)
        self.zdim = int(zdim)

        x = xdim
        y = ydim
        z = zdim


        temp_World = [[[0]* z for i in range(y) ] for j in range(x)]

        #print(temp_World)
        #print(temp_World[0][0][0])
        #temp_World[0][1][2] = 2
        #print(temp_World[0][1][2])
        #print(temp_World)

        cubecounter = int(0)  # counter for totalnumber of cubes at the end. Mostly just for testing


        #print(temp_World)

        #temp_World[0][0][0] = 1
        #temp_World[2][1][1] = 2
        #print(temp_World)
        #print(temp_World[0][0][0])
        #print(temp_World[2][1][1])

        #self.World = zworld


        
        for z in range(zdim):                                       # fills the world with cubes (all walkable/flyable)
                for y in range(ydim):
                        for x in range(xdim):
                            cubecounter += int(1)
                            temp_World[x][y][z] = CubeinSpace(x,y,z,0,0,0,0,0,cubecounter)
        
        self.cubenumber = cubecounter
        
        self.World = temp_World
    
    def getWorld(self):
        return (self.World)

    def getcube(self, x, y, z):
        return(self.World[x][y][z])

    def gettotalcubenumber(self):
        return(self.cubenumber)

    def getdimesions(self):
        #print("X-dim: " + str(self.xdim) +" Y-dim: "+ str(self.ydim) + " Z-dim: "+ str(self.zdim))
        return([self.xdim,self.ydim,self.zdim])

    def move_Ground_Object_to(self,x,y,z):
        for Z in self.World:
            for Y in Z:
                for cube in Y:
                    if cube.getGround_Object() == 1:
                        cube.setGround_Object(0)
                        cube.setVLOS(0)
        self.World[x][y][z].setGround_Object(1)
        self.World[x][y][z].setVLOS(1)


    def setflyzone(self,a,b,c,i,j,k):    # creates flyzone (shape: cube).  a,b,c = start coordinates  i,j,k = end coordinates (!) and makes the cubes also unwalkable / no field
        if i >= self.xdim or j >= self.ydim or k >= self.zdim:
            print("noflyzone out of bounds")
        else:
            for z in range(c,k+1):
                for y in range(b,j+1):
                    for x in range(a,i+1):
                        self.World[x][y][z].setflyable(1)
                        #self.World[x][y][z].setwalkable(0)
                        #self.World[x][y][z].setfield(0)

    def setnoflyzone(self,a,b,c,i,j,k):    # creates no flyzone (shape: cube).  a,b,c = start coordinates  i,j,k = end coordinates (!) and makes the cubes also unwalkable / no field
        if i >= self.xdim or j >= self.ydim or k >= self.zdim:
            print("noflyzone out of bounds")
        else:
            for z in range(c,k+1):
                for y in range(b,j+1):
                    for x in range(a,i+1):
                        self.World[x][y][z].setflyable(0)
                        #self.World[x][y][z].setwalkable(0)
                        #self.World[x][y][z].setfield(0)

    def setwalkzone(self,a,b,c,i,j,k):   # creates no walkzone (shape: cube).  a,b,c = start coordinates  i,j,k = end coordinates (!) and no fields
        if i >= self.xdim or j >= self.ydim or k >= self.zdim:
            print("nowalkzone out of bounds")
        else:
            for z in range(c,k+1):
                for y in range(b,j+1):
                    for x in range(a,i+1):
                        self.World[x][y][z].setwalkable(1)
                        #self.World[x][y][z].setfield(0)

    def setfieldzone(self,a,b,c,i,j,k):   # creates fieldzone (shape: cube).  a,b,c = start coordinates  i,j,k = end coordinates  (!) pot. useless (!)
            if i >= self.xdim or j >= self.ydim or k >= self.zdim:
                print("field set out of bounds")
            else:
                for z in range(c,k+1):
                    for y in range(b,j+1):
                        for x in range(a,i+1):
                            self.World[x][y][z].setfield(1)
                    
    def setnofieldzone(self,a,b,c,i,j,k):   # creates no fieldzone (shape: cube).  a,b,c = start coordinates  i,j,k = end coordinates  (!) pot. useless (!)
            if i >= self.xdim or j >= self.ydim or k >= self.zdim:
                print("nofield set out of bounds")
            else:
                for z in range(c,k+1):
                    for y in range(b,j+1):
                        for x in range(a,i+1):
                            self.World[x][y][z].setfield(0)

    def getfield_lists(self):              # Generates list of the individual fields and puts them in a list. e.g.: Fields: [X][In here are all nodes of field Nr. X]

        fields = []
        allfieldnodes = []                 # only nodes marked as fields are relevant the rest is sorted out
        for z in range(self.zdim):                                       
             for y in range(self.ydim):
                    for x in range(self.xdim):
                        if self.World[x][y][z].getfield() == 1:
                            allfieldnodes.append(self.World[x][y][z])
        
        if len(allfieldnodes) == 0:       # in case there are no nodes marked as fields
            print("no fields found")

        else:
            #runs = 0
            #fields = []
            currentnode = allfieldnodes[0]
            #neigboringfieldnodes = []
            #allfieldnodes.remove(currentnode)

            while len(allfieldnodes) > 0 and currentnode != None:
                #runs += 1
                #print("whileruns starts:" + str(runs))
                #currentnode = allfieldnodes[0]
                #allfieldnodes.remove(currentnode)
                temp_field_list = []
                temp_field_list.append(currentnode)
                neigboringfieldnodes = []
                #print("wbefor for")
                neigbors = 1
                #ran = 0
                while neigbors > 0  and currentnode != None:             # collectes all neigboring nodes form the currednode and then there neigbors until none are left

                    for temp_z in range(currentnode.getcoordinates()[2]-1,currentnode.getcoordinates()[2]+2):
                            if temp_z >= 0 and temp_z < self.zdim:
                                for temp_y in range(currentnode.getcoordinates()[1]-1,currentnode.getcoordinates()[1]+2):
                                    if temp_y >= 0 and temp_y < self.ydim:
                                        for temp_x in range(currentnode.getcoordinates()[0]-1,currentnode.getcoordinates()[0]+2):
                                            if temp_x >= 0 and temp_x < self.xdim:
                                                if self.World[temp_x][temp_y][temp_z].getfield() == 1:
                                                    if temp_field_list.__contains__(self.World[temp_x][temp_y][temp_z]) != True:
                                                        if neigboringfieldnodes.__contains__(self.World[temp_x][temp_y][temp_z]) != True:
                                                            neigboringfieldnodes.append(self.World[temp_x][temp_y][temp_z])

                    for x in neigboringfieldnodes:
                        if temp_field_list.__contains__(x) != True:
                            temp_field_list.append(x)                                        

                    if len(neigboringfieldnodes) == 0:        # all neigboring nodes are entered in to Fields as one and removed from the pool(allfieldnodes)
                        neigbors = 0
                        fields.append(temp_field_list)
                        
                        for x in temp_field_list:
                            if allfieldnodes.__contains__(x) == True:
                                allfieldnodes.remove(x)
                        if len(allfieldnodes) > 0:        
                            currentnode = allfieldnodes[0]
                        else:
                            currentnode = None

                    else:            
                        currentnode = neigboringfieldnodes[0]
                        neigboringfieldnodes.remove(currentnode)  
                                            

        return fields

    def get2dflymatrixoflevel(self, zlevel):

        matrix = []

        for y in range(self.ydim):
            temp_list=[]
            for x in range(self.xdim):
                temp_list.append(self.World[x][y][zlevel].getflyable())
            matrix.append(temp_list)

        #matrix.reverse()

        return matrix

    def get2dwalkmatrixoflevel(self, zlevel):

        matrix = []

        for y in range(self.ydim):
            temp_list=[]
            for x in range(self.xdim):
                temp_list.append(self.World[x][y][zlevel].getwalkable())
            matrix.append(temp_list)

        #matrix.reverse()

        return matrix

    def get2dpaintmatrixoflevel(self, zlevel):

        matrix = []

        for y in range(self.ydim):
            temp_list=[]
            for x in range(self.xdim):
                if self.World[x][y][zlevel].getGround_Object() == 1:
                    temp_list.append(8)
                else:
                    if self.World[x][y][zlevel].getwalkable() == 1:
                        temp_list.append(2)
                    else: 
                        if self.World[x][y][zlevel].getfield() == 1:
                            temp_list.append(1)
                        else: 
                            temp_list.append(0)
            matrix.append(temp_list)

        #matrix.reverse()

        return matrix
        

               


# TESTS -----------------------------------------------
"""
NewWorld = CreateWorld(50,25,1) 
print(NewWorld.getdimesions())
NewWorld.setflyzone(1,1,0,20,20,0)
#NewWorld.setnoflyzone(1,1,0,20,20,0)
flyable = NewWorld.get2dflymatrixoflevel(0)

print(flyable)
#"""
"""
NewWorld = CreateWorld(50,25,1) 
print(NewWorld.getdimesions())
#print(NewWorld.getWorld())
#print(NewWorld.getcube(0,1,2).getcoordinates())

# 2D matrix Tests -------

NewWorld.setnoflyzone(0,0,0,49,0,0)
NewWorld.setnoflyzone(0,0,0,0,24,0)
NewWorld.setnoflyzone(49,0,0,49,24,0)
NewWorld.setnoflyzone(0,24,0,49,24,0)
NewWorld.setnoflyzone(19,8,0,22,11,0)
NewWorld.setnowalkzone(1,1,0,22,11,0)
NewWorld.setnowalkzone(25,1,0,49,11,0)
NewWorld.setnowalkzone(1,14,0,22,23,0)
NewWorld.setnowalkzone(25,14,0,49,23,0)
#NewWorld.setnoflyzone(3,3,0,4,4,0)
# print(NewWorld.getcube(0,0,0).getflyable())
#testmatrixforpainting = NewWorld.get2dpaintmatrixoflevel(0)
for list in NewWorld.get2dpaintmatrixoflevel(0):
    print(list) 


#print(NewWorld.getfield_lists())
for x in NewWorld.getfield_lists():
    print("---- new field ----")
    for y in x:
        print(y.getcoordinates())


# Field listing tests -----------
"""
"""
NewWorld.setfield(0,0,0,0,0,0)
NewWorld.setfield(3,0,0,4,1,0)
NewWorld.setfield(6,0,0,7,1,0)
NewWorld.setfield(9,0,0,9,1,0)
print(NewWorld.getfield_lists())
for x in NewWorld.getfield_lists():
    print("---- new field ----")
    for y in x:
        print(y.getcoordinates())
"""

"""
print("Test Worldcreation")

NewWorld = CreateWorld(3,3,3)                     # NewWorld = CreateWorld(3,3,3)  -->  x: {0,1,2} y: {0,1,2} ....
print(NewWorld.getcube(0,0,0).getcubenummber())
print(NewWorld.getcube(2,1,2).getcoordinates())
print(NewWorld.getcube(2,1,2).getcubenummber())
print(NewWorld.getdimesions())
print("Cubes: "+str(NewWorld.gettotalcubenumber()))
#print(NewWorld.getWorld())
print("Cube(0,0,0): "+NewWorld.getcube(0,0,0).getflyable())
print("Cube(1,1,1): "+NewWorld.getcube(1,1,1).getflyable())
print("Cube(2,2,2): "+NewWorld.getcube(1,1,1).getflyable())
NewWorld.setnoflyzone(0,0,0,1,1,1)
print(NewWorld.getcube(0,0,0).getflyable())
print(NewWorld.getcube(1,1,1).getflyable())
print(NewWorld.getcube(2,2,2).getflyable())

print("Cube(0,0,0): "+NewWorld.getcube(0,0,0).getwalkable())
print("Cube(1,1,1): "+NewWorld.getcube(1,1,1).getwalkable())
print("Cube(2,2,2): "+NewWorld.getcube(1,1,1).getwalkable())
NewWorld.setnowalkzone(1,1,1,2,2,2)
print(NewWorld.getcube(0,0,0).getwalkable())
print(NewWorld.getcube(1,1,1).getwalkable())
print(NewWorld.getcube(2,2,2).getwalkable())

print("Cube(0,0,0): "+NewWorld.getcube(0,0,0).getfield())
print("Cube(1,1,1): "+NewWorld.getcube(1,1,1).getfield())
print("Cube(2,2,2): "+NewWorld.getcube(1,1,1).getfield())
NewWorld.setfield(1,1,1,2,2,2)
print(NewWorld.getcube(0,0,0).getfield())
print(NewWorld.getcube(1,1,1).getfield())
print(NewWorld.getcube(2,2,2).getfield())

"""
