# "Source" codingwithruss.com
from CubeClass import CubeinSpace
from Worldcreation import CreateWorld
import pygame
from pygame.locals import *
from pathfinding.core.grid import Grid
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.finder.a_star import AStarFinder
from GBWCpathfinder import GBWC
from pathwitklos import Path_with_VLOS
#import copy

pygame.init()

screen_width = 1500
screen_heigth = 750

screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption("PyGameTest")

# define game variables ----
tile_size = 30

class paintworld():
    def __init__(self, data2d): 
        self.tile_list = []

        # Loading images -----------
        field_img = pygame.image.load("Images/Feld.png")
        forestNoFlyzone_img = pygame.image.load("Images/WaldNoFlyzone.png")
        walkableground_img = pygame.image.load("Images/WegWalkable.png")
        dronepath_img = pygame.image.load("Images/abgeflogenerweg.png")
        Drohne_img = pygame.image.load("Images/Drohne.png")
        reusedflypath_img = pygame.image.load("Images/doppeltabgeflogenerweg.png")
        Ground_obj_img = pygame.image.load("Images/Bodenperson.png")

        row_count = 0
        for row in data2d:          # 0 = noflyzone  1 = field   2 = ground path   3 = drone path  4 = double drone path  5 = drone  8 = Groundobject 
            col_count = 0
            for tile in row:
                if tile == 8:
                    img = pygame.transform.scale(Ground_obj_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(Drohne_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(reusedflypath_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(dronepath_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(walkableground_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 1:
                    img = pygame.transform.scale(field_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 0:
                    img = pygame.transform.scale(forestNoFlyzone_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def drawworld(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])




# grid of screen ----
def draw_gird():
    for line in range(0, 50):   # because 1000/50 (tile_size) is 20
        pygame.draw.line(screen, (0,0,0), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (0,0,0), (line * tile_size, 0), (line * tile_size, screen_heigth))


NewWorld = CreateWorld(50,25,1) 
print(NewWorld.getdimesions())

# 2D matrix Tests -------
""" # World 1
NewWorld.setflyzone(1,1,0,48,23,0)
NewWorld.setwalkzone(1,11,0,48,12,0)
NewWorld.setwalkzone(23,1,0,24,23,0)
NewWorld.setfieldzone(19,1,0,22,7,0)
NewWorld.setfieldzone(1,1,0,19,10,0)
NewWorld.setfieldzone(1,13,0,22,23,0)
NewWorld.setfieldzone(27,1,0,48,10,0)
NewWorld.setfieldzone(27,13,0,48,23,0)
NewWorld.setnofieldzone(7,21,0,9,23,0)
NewWorld.setnofieldzone(37,15,0,39,16,0)
NewWorld.setnoflyzone(7,21,0,9,23,0)
NewWorld.setnoflyzone(37,15,0,39,16,0)
NewWorld.setnoflyzone(25,1,0,26,10,0)
NewWorld.setnoflyzone(25,13,0,26,23,0)
NewWorld.setnoflyzone(20,8,0,22,10,0)
#"""
#""" # World 2
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
#NewWorld.setnofieldzone(31,1,0,32,10,0)
#NewWorld.setnofieldzone(33,1,0,34,10,0)
#NewWorld.setnofieldzone(31,13,0,32,23,0)
#NewWorld.setnofieldzone(33,13,0,34,23,0)
#NewWorld.setnoflyzone(14,1,0,15,10,0)
#NewWorld.setnoflyzone(31,1,0,31,10,0)
#NewWorld.setnoflyzone(34,1,0,34,10,0)
#NewWorld.setnoflyzone(31,13,0,31,23,0)
#NewWorld.setnoflyzone(34,13,0,34,23,0)
NewWorld.setnofieldzone(1,1,0,2,4,0)
NewWorld.setnoflyzone(1,1,0,2,4,0)
NewWorld.setnofieldzone(1,1,0,4,3,0)
NewWorld.setnoflyzone(1,1,0,4,3,0)
NewWorld.setnofieldzone(20,15,0,22,16,0)
NewWorld.setnoflyzone(20,15,0,22,16,0)
NewWorld.setnofieldzone(5,5,0,9,9,0)
NewWorld.setnoflyzone(5,5,0,9,9,0)
NewWorld.setnofieldzone(19,5,0,22,7,0)
NewWorld.setnoflyzone(19,5,0,22,7,0)
NewWorld.setnofieldzone(25,5,0,27,7,0)
NewWorld.setnoflyzone(25,5,0,27,7,0)

#NewWorld.setnofieldzone(46,20,0,46,20,0)
#NewWorld.setnoflyzone(46,20,0,46,20,0)

#NewWorld.setnofieldzone(43,1,0,48,10,0)
#NewWorld.setnoflyzone(43,1,0,48,10,0)
#NewWorld.setnofieldzone(43,13,0,48,23,0)
#NewWorld.setnoflyzone(43,13,0,48,23,0)




#"""
# pathfinding ----------------------------------------------------------------
""" # World 1
Airgrid = Grid(matrix = NewWorld.get2dflymatrixoflevel(0))
Groundgrid = Grid(matrix = NewWorld.get2dwalkmatrixoflevel(0))

Airstart1 = Airgrid.node(22,7)
Airend1 = Airgrid.node(27,10)
Airstart2 = Airgrid.node(48,10)
Airend2 = Airgrid.node(48,13)
Airstart3 = Airgrid.node(27,13)
Airend3 = Airgrid.node(22,13)

finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path1,runs1 = finder.find_path(Airstart1,Airend1,Airgrid)
Airgrid.cleanup()
path2,runs2 = finder.find_path(Airstart2,Airend2,Airgrid)
Airgrid.cleanup()
path3,runs3 = finder.find_path(Airstart3,Airend3,Airgrid)
Astarpaths = []
Astarpaths.append(path1)
Astarpaths.append(path2)
Astarpaths.append(path3)
#"""

#""" # World 2
Airgrid = Grid(matrix = NewWorld.get2dflymatrixoflevel(0))
Groundgrid = Grid(matrix = NewWorld.get2dwalkmatrixoflevel(0))

Airstart1 = Airgrid.node(12,10)
Airend1 = Airgrid.node(15,11)
Airstart2 = Airgrid.node(31,11)
Airend2 = Airgrid.node(34,11)
Airstart3 = Airgrid.node(48,11)
Airend3 = Airgrid.node(48,12)
Airstart4 = Airgrid.node(34,12)
Airend4 = Airgrid.node(31,12)
Airstart5 = Airgrid.node(13,13)
Airend5 = Airgrid.node(12,13)

finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path1,runs1 = finder.find_path(Airstart1,Airend1,Airgrid)
Airgrid.cleanup()
path2,runs2 = finder.find_path(Airstart2,Airend2,Airgrid)
Airgrid.cleanup()
path3,runs3 = finder.find_path(Airstart3,Airend3,Airgrid)
Airgrid.cleanup()
path4,runs4 = finder.find_path(Airstart4,Airend4,Airgrid)
Airgrid.cleanup()
path5,runs5 = finder.find_path(Airstart5,Airend5,Airgrid)

Astarpaths = []
Astarpaths.append(path1)
Astarpaths.append(path2)
Astarpaths.append(path3)
Astarpaths.append(path4)
Astarpaths.append(path5)
#"""
#-----------------------------------------------------------------------------

prepaintmatrix = NewWorld.get2dpaintmatrixoflevel(0)
Backupprepaintmatrix = NewWorld.get2dpaintmatrixoflevel(0)
Backupprepaintmatrix_Nr2 = NewWorld.get2dpaintmatrixoflevel(0)


""" # World 1
fields = NewWorld.getfield_lists()
GBWCthing = GBWC(NewWorld.getWorld())
fieldcoveragepath = []
fieldcoveragepath.append(GBWCthing.GBWCpath(fields[0],1,10,22,7))
fieldcoveragepath.append(GBWCthing.GBWCpath(fields[1],27,10,48,10))
fieldcoveragepath.append(GBWCthing.GBWCpath(fields[3],48,13,27,13))
fieldcoveragepath.append(GBWCthing.GBWCpath(fields[2],22,13,1,13))
#fieldcoveragepath.append(GBWCthing.GBWCpath(fields[3],48,13,27,13))
#"""
#""" # World 2  Path creation --------------------------------------------
fields = NewWorld.getfield_lists()
GBWCthing = GBWC(NewWorld.getWorld())
fieldcoveragepath = []
groundwalkpath = []
#fieldcoveragepath.append(GBWCthing.GBWCpath(fields[0],1,10,11,10))
testest = Path_with_VLOS(NewWorld)
fields = NewWorld.getfield_lists()
#print(testest.of_Field_from_Groundstartpoint(fields[3],27,12,0))
groundstartpoint = [1,12,0]                                                                                                           # <--- Ground start point 
for x in range(0,6):
    y = x
    if x == 3:
        y = 5
    if x == 5:
        y = 3
    for double in testest.of_Field_from_Groundstartpoint(fields[y],groundstartpoint[0],groundstartpoint[1],groundstartpoint[2], 25):  # <---  view range 
        if len(double[0]) > 2 and len(double) > 1:
            NewWorld.move_Ground_Object_to(double[0][0],double[0][1],double[0][2])
            fieldcoveragepath.append(double[1])
            groundwalkpath.append(double[0])
            #print(double[0])
            groundstartpoint = double[0]
#fieldcoveragepath.append(GBWCthing.GBWCpath_with_heuristic_and_restep(fields[0],1,10,11,10))
#fieldcoveragepath.append(GBWCthing.GBWCpath_with_heuristic_and_restep(fields[1],16,10,30,10))
#fieldcoveragepath.append(GBWCthing.GBWCpath_with_heuristic_and_restep(fields[2],35,10,48,10))
#fieldcoveragepath.append(GBWCthing.GBWCpath_withheuristic(fields[5],48,13,35,13))
#fieldcoveragepath.append(GBWCthing.GBWCpath_withheuristic(fields[4],30,13,14,13))
#fieldcoveragepath.append(GBWCthing.GBWCpath_withheuristic(fields[3],11,13,1,13))
#"""


#worldtopaint = paintworld(prepaintmatrix)

#------------------------------------------ build the complete path for painting via key press


#print("Ground stop points: ")
#print(groundwalkpath)

completepath = []
#"""
print("Ground stop points: ")
print(groundwalkpath)
for l in range(0, len(fieldcoveragepath)):

    for cube in fieldcoveragepath[l]:
        y = cube.getcoordinates()[1]
        x = cube.getcoordinates()[0]
        completepath.append([x, y, groundwalkpath[l]])
    #"""
"""
    if len(Astarpaths) > l:
        for x in Astarpaths[l]:
            completepath.append(x)
#"""


lastdouble = [0]

lastgroundposx = -1
lastgroundposy = -1



def updateviakey():
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] == True:
        if len(completepath) > 0:
            double = completepath[0]
            #""" #-----------  #ads ground object path
            if len(double) > 2:
                global lastgroundposx
                global lastgroundposy
                if double[2][0] != lastgroundposx or double[2][1] != lastgroundposy: 
                    if lastgroundposx >= 0 and lastgroundposy >= 0:
                        prepaintmatrix[lastgroundposy][lastgroundposx] = Backupprepaintmatrix[lastgroundposy][lastgroundposx]
                prepaintmatrix[double[2][1]][double[2][0]] = 8
                lastgroundposx = double[2][0]
                lastgroundposy = double[2][1]
            #""" #-----------
            y = double[1]
            x = double[0]
            if prepaintmatrix[y][x] == 3:
                Backupprepaintmatrix[y][x] = 3
            if lastdouble[0] != 0:
                if Backupprepaintmatrix[lastdouble[0][1]][lastdouble[0][0]] == 3:
                    prepaintmatrix[lastdouble[0][1]][lastdouble[0][0]] = 4
                else:
                    prepaintmatrix[lastdouble[0][1]][lastdouble[0][0]] = 3
            prepaintmatrix[y][x] = 5 
            lastdouble.insert(0, [x, y])
            completepath.remove(double)

    if key[pygame.K_LEFT] == True:
            if lastdouble[0] != 0:
                double = lastdouble[0]
                y = double[1]
                x = double[0]
                prepaintmatrix[y][x] = Backupprepaintmatrix[y][x]
                if len(lastdouble) > 2:
                     prepaintmatrix[lastdouble[1][1]][lastdouble[1][0]] = 5
                completepath.insert(0, [x, y])
                lastdouble.remove(double)
                if Backupprepaintmatrix[y][x] == 3:
                    Backupprepaintmatrix[y][x] = Backupprepaintmatrix_Nr2[y][x]
# ------------------------------------------------------------------------

#worldtopaint = paintworld(prepaintmatrix)

run = True
while run == True:

    worldtopaint = paintworld(prepaintmatrix)

    worldtopaint.drawworld()

    draw_gird()
    
    updateviakey()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()