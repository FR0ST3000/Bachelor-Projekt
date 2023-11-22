import CubeClass
from CubeClass import CubeinSpace
from Worldcreation import CreateWorld 
import time
import math
import copy

#"""
#starttime = time.time()

NewWorld = CreateWorld(50,25,1)
#NewWorld.setflyzone(0,0,0,49,24,0)
#"""
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
NewWorld.setnofieldzone(14,1,0,15,10,0)
NewWorld.setnofieldzone(31,1,0,32,10,0)
NewWorld.setnofieldzone(33,1,0,34,10,0)
NewWorld.setnofieldzone(31,13,0,32,23,0)
NewWorld.setnofieldzone(33,13,0,34,23,0)
NewWorld.setnoflyzone(14,1,0,15,10,0)
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
NewWorld.setnofieldzone(5,5,0,9,9,0)
NewWorld.setnoflyzone(5,5,0,9,9,0)

NewWorld.move_Ground_Object_to(48,12,0)
#"""
class VLOScreation:

    def __init__(self, World):
        self.NewWorld = World

    def VLOS_from_point(self, Xpos, Ypos, Zpos, sight_range):

        sight_range = sight_range
        orginal_Xstart = copy.copy(Xpos)
        orginal_Ystart = copy.copy(Ypos)
        orginal_Zstart = copy.copy(Zpos)


        for z in self.NewWorld.getWorld():
            for y in z:
                for cube in y:
                    cube.setVLOS(0)

        self.NewWorld.move_Ground_Object_to(Xpos, Ypos, Zpos)


        Edgeofworld = []

        for X in range(0, self.NewWorld.getdimesions()[0]):
            temp_cube = self.NewWorld.getcube(X,0,0)
            if Edgeofworld.__contains__(temp_cube) != True:
                Edgeofworld.append(temp_cube)

        for X in range(0, self.NewWorld.getdimesions()[0]):
            temp_cube = self.NewWorld.getcube(X,self.NewWorld.getdimesions()[1]-1,0)
            if Edgeofworld.__contains__(temp_cube) != True:
                Edgeofworld.append(temp_cube)

        for Y in range(0, self.NewWorld.getdimesions()[1]):
            temp_cube = self.NewWorld.getcube(0,Y,0)
            if Edgeofworld.__contains__(temp_cube) != True:
                Edgeofworld.append(temp_cube)

        for Y in range(0, self.NewWorld.getdimesions()[1]):
            temp_cube = self.NewWorld.getcube(self.NewWorld.getdimesions()[0]-1,Y,0)
            if Edgeofworld.__contains__(temp_cube) != True:
                Edgeofworld.append(temp_cube)

        Ground_Object_coordinates = []

        for Z in self.NewWorld.getWorld():
            for Y in Z:
                for cube in Y:
                    if cube.getGround_Object() == 1:
                        Ground_Object_coordinates = cube.getcoordinates()


        for cube in Edgeofworld:
            Startx = Ground_Object_coordinates[0]
            StartY = Ground_Object_coordinates[1]

            Endx = cube.getcoordinates()[0]
            EndY = cube.getcoordinates()[1]

            if (Endx-Startx) != 0:
                line_values = []
                line_values.append((EndY-StartY) / (Endx-Startx)) 
                line_values.append(StartY - line_values[0]*Startx)

                if Endx > Startx:
                    
                    #"""
                    x = Startx
                    angle = math.degrees(math.atan(abs((EndY - StartY)/(Endx - Startx))))
                    cut = (1 - angle/90)/2
                    xstep = round(cut, 3)
                    ycut = (1 - (90 - angle)/90)/2
                    ystep = round(ycut, 3)
                    #"""------------------------------------------------------------------- # change formular to x depends on y
                    if angle > 45:
                        if EndY > StartY:
                            y = StartY
                            #cut = (1 - (90 - angle)/90)/2
                            #ystep = round(cut, 3)
                            while y < EndY:
                                y += ystep
                                temp_x = int(round(line_values[0]**(-1) * (y - line_values[1]), 0))
                                temp_y = int(round((y), 0))
                                #"""   #------------------------ check for sight range overstep/limit

                                distance_start_current = math.sqrt((orginal_Xstart - temp_x)**2 + (orginal_Ystart - temp_y)**2)
                                if distance_start_current > sight_range :
                                    break

                                #"""
                                if int(round(line_values[0]**(-1) * (y - line_values[1]), 0)) < self.NewWorld.getdimesions()[0] and int(round((y), 0)) < self.NewWorld.getdimesions()[1]:
                                    if self.NewWorld.getcube(temp_x, temp_y, 0).getflyable() == 1:
                                        self.NewWorld.getcube(temp_x, temp_y, 0).setVLOS(1)
                                    else:
                                        break
                        else:
                            y = StartY
                            #cut = (1 - (90 - angle)/90)/2
                            #ystep = round(cut, 3)
                            while y > EndY:
                                y -= ystep
                                temp_x = int(round(line_values[0]**(-1) * (y - line_values[1]), 0))
                                temp_y = int(round((y), 0))
                                #"""   #------------------------ check for sight range overstep/limit

                                distance_start_current = math.sqrt((orginal_Xstart - temp_x)**2 + (orginal_Ystart - temp_y)**2)
                                if distance_start_current > sight_range :
                                    break

                                #"""
                                if int(round(line_values[0]**(-1) * (y - line_values[1]), 0)) < self.NewWorld.getdimesions()[0] and int(round((y), 0)) < self.NewWorld.getdimesions()[1]:
                                    if self.NewWorld.getcube(temp_x, temp_y, 0).getflyable() == 1:
                                        self.NewWorld.getcube(temp_x, temp_y, 0).setVLOS(1)
                                    else:
                                        break

                    #""" #------------------------------------------------------------------------------------
                    #cut = (1 - angle/90)/5
                    #xstep = round(cut, 3)
                    else:
                        #xstep = round(cut, 3)
                        while x < Endx:
                            x += xstep
                            temp_x = int(round((x), 0))
                            temp_y = int(round(line_values[0] * (x) + line_values[1], 0))
                            #"""   #------------------------ check for sight range overstep/limit

                            distance_start_current = math.sqrt((orginal_Xstart - temp_x)**2 + (orginal_Ystart - temp_y)**2)
                            if distance_start_current > sight_range :
                                break

                            #"""
                            if int(round(line_values[0] * (x) + line_values[1], 0)) < self.NewWorld.getdimesions()[1] and int(round((x), 0)) < self.NewWorld.getdimesions()[0]:
                                if self.NewWorld.getcube(int(round((x), 0)), int(round(line_values[0] * (x) + line_values[1], 0)), 0).getflyable() == 1:
                                    self.NewWorld.getcube(int(round((x), 0)), int(round(line_values[0] * (x) + line_values[1], 0)), 0).setVLOS(1)
                                else:
                                    break
                    #"""
                else:
                    
                    #"""
                    x = Startx
                    angle = math.degrees(math.atan(abs((EndY - StartY)/(Endx - Startx))))
                    cut = (1 - angle/90)/2
                    xstep = round(cut, 3)
                    ycut = (1 - (90 - angle)/90)/2
                    ystep = round(ycut, 3)
                    #"""------------------------------------------------------------------- # change formular to x depends on y  
                    if angle > 45:
                        if EndY < StartY:
                            y = StartY
                            #cut = (1 - (90 - angle)/90)/2
                            #ystep = round(cut, 3)
                            while y > EndY:
                                y -= ystep
                                temp_x = int(round(line_values[0]**(-1) * (y - line_values[1]), 0))
                                temp_y = int(round((y), 0))
                                #"""   #------------------------ check for sight range overstep/limit

                                distance_start_current = math.sqrt((orginal_Xstart - temp_x)**2 + (orginal_Ystart - temp_y)**2)
                                if distance_start_current > sight_range :
                                    break

                                #"""
                                if temp_x < self.NewWorld.getdimesions()[0] and temp_y < self.NewWorld.getdimesions()[1]:
                                    if self.NewWorld.getcube(temp_x, temp_y, 0).getflyable() == 1:
                                        self.NewWorld.getcube(temp_x, temp_y, 0).setVLOS(1)
                                    else:
                                        break
                        else:
                            y = StartY
                            #cut = (1 - (90 - angle)/90)/2
                            #ystep = round(cut, 3)
                            while y < EndY:
                                y += ystep
                                temp_x = int(round(line_values[0]**(-1) * (y - line_values[1]), 0))
                                temp_y = int(round((y), 0))
                                #"""   #------------------------ check for sight range overstep/limit

                                distance_start_current = math.sqrt((orginal_Xstart - temp_x)**2 + (orginal_Ystart - temp_y)**2)
                                if distance_start_current > sight_range :
                                    break

                                #"""
                                if temp_x < self.NewWorld.getdimesions()[0] and temp_y < self.NewWorld.getdimesions()[1]:
                                    if self.NewWorld.getcube(temp_x, temp_y, 0).getflyable() == 1:
                                        self.NewWorld.getcube(temp_x, temp_y, 0).setVLOS(1)
                                    else:
                                        break

                    #""" #------------------------------------------------------------------------------------
                    #cut = (1 - angle/90)/5
                    #xstep = round(cut, 3)
                    else:
                        while x > Endx:
                            x -= xstep
                            temp_x = int(round((x), 0))
                            temp_y = int(round(line_values[0] * (x) + line_values[1], 0))
                            #"""   #------------------------ check for sight range overstep/limit

                            distance_start_current = math.sqrt((orginal_Xstart - temp_x)**2 + (orginal_Ystart - temp_y)**2)
                            if distance_start_current > sight_range :
                                break

                            #"""
                            if int(round(line_values[0] * (x) + line_values[1], 0)) < self.NewWorld.getdimesions()[1] and int(round((x), 0)) < self.NewWorld.getdimesions()[0]:
                                if self.NewWorld.getcube(int(round((x), 0)), int(round(line_values[0] * (x) + line_values[1], 0)), 0).getflyable() == 1:
                                    self.NewWorld.getcube(int(round((x), 0)), int(round(line_values[0] * (x) + line_values[1], 0)), 0).setVLOS(1)
                                else:
                                    break
                    #"""

            else:
                if EndY >= StartY:
                    for y in range(StartY, EndY+1):
                        #"""   #------------------------ check for sight range overstep/limit

                        distance_start_current = math.sqrt((orginal_Ystart - y)**2)
                        if distance_start_current > sight_range :
                            break

                        #"""
                        if self.NewWorld.getcube(Startx, y, 0).getflyable() == 1:
                                self.NewWorld.getcube(Startx, y, 0).setVLOS(1)
                        else:
                            break
                else:
                    temp_list = []
                    for n in range(EndY, StartY+1):
                        temp_list.append(n)
                    temp_list.reverse()
                    for y in temp_list:
                        #"""   #------------------------ check for sight range overstep/limit
                        
                        distance_start_current = math.sqrt((orginal_Ystart - y)**2)
                        if distance_start_current > sight_range :
                            break

                        #"""
                        if self.NewWorld.getcube(Startx, y, 0).getflyable() == 1:
                            self.NewWorld.getcube(Startx, y, 0).setVLOS(1)
                        else:
                            break




    def VLOSmatrix(self):

        VLOSmatrix = []

        for y in range(self.NewWorld.getdimesions()[1]):
            temp_list=[]
            for x in range(self.NewWorld.getdimesions()[0]):
                if self.NewWorld.getcube(x,y,0).getGround_Object() == 1:
                    temp_list.append(8)
                else:   
                    if  self.NewWorld.getcube(x,y,0).getflyable() == 0:
                        temp_list.append(3)
                    else:
                        temp_list.append(self.NewWorld.getcube(x,y,0).getVLOS())
            VLOSmatrix.append(temp_list)

                



        #print("sichtbare cubes: "+str(counter))

        #for xline in NewWorld.get2dflymatrixoflevel(0):
        #   print(xline)
        print("................................")
        for xline in VLOSmatrix:
            print(xline)

        #print(Ground_Object_coordinates)

    #endtime = time.time()
    #timedif = endtime - starttime
    #print("Time: "+ str(timedif)+"sec")
        #print(line_values)
        #for n in range(Startx, Endx+1):
            #print(round(line_values[0] * n + line_values[1], 0))

            # check if (n,round(line_values[0] * n + line_values[1], 0)) is no flyzone


# Tests ---------------------------
"""
VLOScre = VLOScreation(NewWorld)
starttime = time.time()
VLOScre.VLOS_from_point(20,11,0,20)
endtime = time.time()
VLOScre.VLOSmatrix()

#endtime = time.time()
timedif = endtime - starttime
print("Time: "+ str(timedif)+"sec")

#VLOScre.VLOS_from_point(48,12,0)
#VLOScre.VLOSmatrix()

#"""
