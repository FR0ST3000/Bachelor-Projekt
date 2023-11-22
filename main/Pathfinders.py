from CubeClass import CubeinSpace
from Worldcreation import CreateWorld
import math

class Astarpathfinder:
    def __init__(self, world):
        self.world = world.getWorld()
        self.worlddim = world.getdimesions()

    def findflypath(self,a,b,c,x,y,z):               # a,b,c = start coordinates     x,y,z = endcoordinates
        opennodelist = []
        closednodelist = []
        gcost = 0.0
        hcost = math.sqrt((a-x)**2 + (b-y)**2 + (c-z)**2)
        fcost = gcost + hcost
        opennodelist.append([self.world[a][b][c],gcost,hcost,fcost])

        print("Start coordinates: "+str(self.world[a][b][c].getcoordinates()))
        print(opennodelist)
        print(opennodelist[0][0])
        print(opennodelist[0][1])
        print(opennodelist[0][2])
        print(opennodelist[0][3])

        whileloopruns = 0
        endfound = 0

        while  0 < len(opennodelist)  and whileloopruns < 50 and endfound == 0:
            #print("start of while loop")
            #print(opennodelist)
            #print("len opennodelist:")
            #print(len(opennodelist))
            whileloopruns += 1

            currentnode_withghfcost = opennodelist[0]

            for list in opennodelist:

                if list[3] < currentnode_withghfcost[3]:
                    currentnode_withghfcost = list

            
            opennodelist.remove(currentnode_withghfcost)
            closednodelist.append(currentnode_withghfcost)

            print("current + end node: ")
            print(currentnode_withghfcost[0].getcoordinates())
            print(self.world[x][y][z].getcoordinates())

            if currentnode_withghfcost[0].getcoordinates() == self.world[x][y][z].getcoordinates():
                endfound = 1
                print("path found")
            
            rangenoderuns = 0
            # check neighbouringnodes: 

            for temp_z in range(currentnode_withghfcost[0].getcoordinates()[2],currentnode_withghfcost[0].getcoordinates()[2]+2):
                if temp_z >= 0 and temp_z < self.worlddim[2]:
                    for temp_y in range(currentnode_withghfcost[0].getcoordinates()[1],currentnode_withghfcost[0].getcoordinates()[1]+2):
                        if temp_y >= 0 and temp_y < self.worlddim[1]:
                            for temp_x in range(currentnode_withghfcost[0].getcoordinates()[0],currentnode_withghfcost[0].getcoordinates()[0]+2):
                                if temp_x >= 0 and temp_x < self.worlddim[0]:

                                    #print(self.world[temp_x][temp_y][temp_z].getflyable())
                                    #print(self.world[temp_x][temp_y][temp_z].getcoordinates())

                                    rangenoderuns += 1

                                    if self.world[temp_x][temp_y][temp_z].getflyable() == 1:
                                        #print("flyable checked")
                                       # temp_g = math.sqrt((currentnode_withghfcost[0].getcoordinates()[0] - a)**2 + (currentnode_withghfcost[0].getcoordinates()[1] - b)**2 + (currentnode_withghfcost[0].getcoordinates()[2] - c)**2)
                                       # temp_h = math.sqrt((currentnode_withghfcost[0].getcoordinates()[0] - x)**2 + (currentnode_withghfcost[0].getcoordinates()[1] - y)**2 + (currentnode_withghfcost[0].getcoordinates()[2] - z)**2)
                                        temp_g = math.sqrt((temp_x - a)**2 + (temp_y - b)**2 + (temp_z - c)**2)
                                        temp_h = math.sqrt((temp_x - x)**2 + (temp_y - y)**2 + (temp_z - z)**2)
                                        temp_f = temp_g + temp_h
                                        temp_node = [self.world[temp_x][temp_y][temp_z],temp_g,temp_h,temp_f]

                                        #print("temp_node: ")
                                        #print(temp_node)



                                        if  True != opennodelist.__contains__(temp_node):   # or 
                                            if temp_node != currentnode_withghfcost:
                                                opennodelist.append(temp_node)
                                                print("node added")


            print("rangenode runs: "+str(rangenoderuns))
            #print("opennodelist: ")
            #print(opennodelist)
            #print("closednodelist: ")
            #print(closednodelist)
            # for list in opennodelist:
            #    print(list[0].getcoordinates())
            print("len opennodelist at end:")
            print(len(opennodelist))
            

            #until:
                #print("No path found")
        print("open node list:")
        for list in opennodelist:
            print(list[0].getcoordinates())
        print("closed node list:")
        for list in closednodelist:
            print(list)
            print(list[0].getcoordinates())
        print("whileloopruns: " + str(whileloopruns))

# Tests ---------------------------------
newworld = CreateWorld(3,3,1)
#newworld.setnoflyzone(1,1,1,1,1,1)
ASpath = Astarpathfinder(newworld)
ASpath.findflypath(0,0,0,2,2,0)