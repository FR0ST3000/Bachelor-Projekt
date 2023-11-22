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
from pathfinding.core.grid import Grid
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.finder.a_star import AStarFinder
from Randomfillingfield import medium_and_standartabweichung



random.seed(9000)

combienelist = []               # combinelist[x] = [2dflymap, field as list of cubes, GBWCpath of the field, time of GBWCpath creation, GBWCpath_heuristic/restep of the field, time of GBWCpath_heuristic/restep creation, HR doubled covered cubes, VLOS path, VLOS time, extra len for VLOS]
faild_fields = 0                # 87 max for VLOS no error by 2 and 3 Obstacles
ASfinder = AStarFinder(diagonal_movement=DiagonalMovement.always)

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


    Amount_of_Obstacles = 0                                 # Number of Obstacles

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

        GBWCobj = GBWC(NewWorld.getWorld()) 
        path_w_VLOS = Path_with_VLOS(NewWorld)


        # startpoint determination

        startpoint_for_GBWC = 0
        startpoint_for_GBWC_distance = 100000

        old_cube_distance = startpoint_for_GBWC_distance
        for cube in fields[0]:
            if cube.getflyable() == 1:
                distance_cube = math.sqrt(cube.getcoordinates()[0]**2 + cube.getcoordinates()[1]**2)
                if distance_cube < old_cube_distance:
                    old_cube_distance = distance_cube
                    startpoint_for_GBWC = cube.getcoordinates()
                    

        # endpoint determination

        endpoint_for_GBWC = 0
        endpoint_for_GBWC_distance = 0

        old_cube_distance_end = endpoint_for_GBWC_distance
        for cube in fields[0]:
            if cube.getflyable() == 1 and (startpoint_for_GBWC != cube.getcoordinates()):
                distance_cube = math.sqrt(cube.getcoordinates()[0]**2 + cube.getcoordinates()[1]**2)
                if distance_cube > old_cube_distance_end:
                    old_cube_distance_end = distance_cube
                    endpoint_for_GBWC = cube.getcoordinates()

        #endpoint_for_GBWC = startpoint_for_GBWC

               
                

       

        copyed_field_1 = copy.copy(fields[0])
        copyed_field_2 = copy.copy(fields[0])
        copyed_field_3 = copy.copy(fields[0])
        copyed_field_4 = copy.copy(fields[0])

        #path creation
        print("-------------------------------------")
        print("Run nr. " +str(len(combienelist) + 1))

        starttime_GBWCpath = time.time()
        GBWCpath = GBWCobj.GBWCpath(copyed_field_1,startpoint_for_GBWC[0],startpoint_for_GBWC[1],endpoint_for_GBWC[0],endpoint_for_GBWC[1])
        endtime_GBWCpath = time.time()
        totaltime_GBWCpath = (endtime_GBWCpath - starttime_GBWCpath)
        temp_list.append(GBWCpath)
        temp_list.append(totaltime_GBWCpath)

        print("Time for path creation: " + str(round(temp_list[3], 2)) + " sec")

        if len(temp_list[1]) - len(temp_list[2]) > 0:
            print("Field len(): " + str(len(fields[0])))
            print("missing squares: " + str(len(temp_list[1]) - (len(temp_list[2])-1)))

        starttime_GBWCpath_hr = time.time()
        GBWCpath_hr = GBWCobj.GBWCpath_with_heuristic_and_restep(copyed_field_2,startpoint_for_GBWC[0],startpoint_for_GBWC[1],endpoint_for_GBWC[0],endpoint_for_GBWC[1])
        endtime_GBWCpath_hr = time.time()
        totaltime_GBWCpath_hr = (endtime_GBWCpath_hr - starttime_GBWCpath_hr)
        temp_list.append(GBWCpath_hr)
        temp_list.append(totaltime_GBWCpath_hr)

        print("Time for path_HR creation: " + str(round(temp_list[5], 2)) + " sec")

        path_without_duplicates = list(dict.fromkeys(copy.copy(GBWCpath_hr)))
        
        if len(temp_list[1]) - len(path_without_duplicates) > 0:
            print("Field len(): " + str(len(fields[0])))
            print("missing squares: " + str(len(temp_list[1]) - (len(path_without_duplicates))))
        else:
            print("missing squares: " + str(len(temp_list[1]) - (len(path_without_duplicates))))

        copyed_path_1 = copy.copy(GBWCpath_hr)
        for cube in copyed_field_3:
            if copyed_path_1.__contains__(cube):
                copyed_path_1.remove(cube)
        
        doubled_covered_cubes = len(copyed_path_1)
        temp_list.append(doubled_covered_cubes)

        print("doubled_covered_cubes: " + str(doubled_covered_cubes))

        # -------------------------------- with VLOS
        #"""
        groundstartpoint = [8,0,0]

        starttime_path_VLOS = time.time()
        paths_VLOS = path_w_VLOS.of_Field_from_Groundstartpoint(fields[0],groundstartpoint[0],groundstartpoint[1],groundstartpoint[2], 20) # <- view range 
        endtime_path_VLOS = time.time()
        totaltime_paths_vlos = (endtime_path_VLOS - starttime_path_VLOS)

        total_VLOS_path = []
        for double in paths_VLOS:
            for cube in double[1]:
                total_VLOS_path.append(cube)

        extra_dc_len = 0                      # adds the extra path len if start/end point is not next to the "person" looking at the drone 
        airgrid = Grid(matrix = temp_list[0])
        for double in paths_VLOS:
            dis_start = math.sqrt((double[0][0] - double[1][0].getcoordinates()[0])**2 + (double[0][1] - double[1][0].getcoordinates()[1])**2)
            dis_end = math.sqrt((double[0][0] - double[1][len(double[1])-1].getcoordinates()[0])**2 + (double[0][1] - double[1][len(double[1])-1].getcoordinates()[1])**2)
            
            if dis_start > 1.5:
                start1 = airgrid.node(double[0][0], double[0][1])
                end1 = airgrid.node(double[1][0].getcoordinates()[0], double[1][0].getcoordinates()[1])
                path1, runs = ASfinder.find_path(start1, end1, airgrid)
                airgrid.cleanup()
                extra_dc_len += (len(path1)-2)
            
            if dis_end > 1.5:
                start2 = airgrid.node(double[0][0], double[0][1])
                end2 = airgrid.node(double[1][len(double[1])-1].getcoordinates()[0], double[1][len(double[1])-1].getcoordinates()[1])
                path2, runs = ASfinder.find_path(start2, end2, airgrid)
                airgrid.cleanup()
                extra_dc_len += (len(path2)-2)

        print("extra dc len: " + str(extra_dc_len))

        temp_list.append(total_VLOS_path)
        temp_list.append(totaltime_paths_vlos)
        temp_list.append(extra_dc_len)

        print("Time for paths_VLOS creation: " + str(round(temp_list[8], 2)) + " sec")
        #"""


        combienelist.append(temp_list)

    """     # prints the fields out
    for x in NewWorld.get2dflymatrixoflevel(0):
        print(x)
    print("-------------------------------------------")
    #"""
"""
for list in combienelist:
    print("--------------------------------")
    for x in list[0]:
        print(x)

print("faild fields: " + str(faild_fields))
#"""

#--------------------------------------------------------- ploting values: -----------------

print("---------------------------------------------")

#Time:

#base implementiation:
Baseline_wavefront_time = []
for list in combienelist:
    Baseline_wavefront_time.append(list[3])

total_time_baseline = 0
for t in Baseline_wavefront_time:
    total_time_baseline += t

arith_Medium_baseline = (total_time_baseline/(len(Baseline_wavefront_time)))

print("baseline medium: " + str(round(arith_Medium_baseline, 5)) + "sec")

Abweichungsquadratsumme_baseline = 0
for x in Baseline_wavefront_time:
    Abweichungsquadratsumme_baseline += (x - arith_Medium_baseline)**2
korrigierte_empirische_Varianz_baseline = Abweichungsquadratsumme_baseline/(len(Baseline_wavefront_time) - 1)
Standardabweichung_baseline = math.sqrt(korrigierte_empirische_Varianz_baseline)
Standardabweichung_baseline_rounded = round(Standardabweichung_baseline, 5)
#print("korrigierte_empirische_Varianz for baseline: " + str(korrigierte_empirische_Varianz_baseline) + "sec")
print("Standardabweichung for baseline rounded: " + str(Standardabweichung_baseline_rounded) + "sec")

#improved implementiation: 
Improved_wavefront_time = []
for list in combienelist:
    Improved_wavefront_time.append(list[5])

total_time_improved = 0
for t in Improved_wavefront_time:
    total_time_improved += t

arith_Medium_improved = (total_time_improved/(len(Improved_wavefront_time)))

print("improved medium: " + str(round(arith_Medium_improved, 5)) + "sec")

Abweichungsquadratsumme_improved = 0
for x in Improved_wavefront_time:
    Abweichungsquadratsumme_improved += (x - arith_Medium_improved)**2
korrigierte_empirische_Varianz_improved = Abweichungsquadratsumme_improved/(len(Improved_wavefront_time) - 1)
Standardabweichung_improved = math.sqrt(korrigierte_empirische_Varianz_improved)
Standardabweichung_improved_rounded = round(Standardabweichung_improved, 5)
#print("korrigierte_empirische_Varianz for improved: " + str(korrigierte_empirische_Varianz_improved) + "sec")
print("Standardabweichung for improved rounded: " + str(Standardabweichung_improved_rounded) + "sec")


# cover percent  -------------------------

#baseline:

list_field_copys_1 = []
for list in combienelist:
    list_field_copys_1.append(copy.copy(list[1]))

paths_on_fields = []
for list in combienelist:
    paths_on_fields.append(copy.copy(list[2]))

#z = 0
list_cover_percent = []
for x in range(0, len(paths_on_fields)):
    cover_percent = round((len(paths_on_fields[x]) / len(list_field_copys_1[x])) * 100 , 2)
    list_cover_percent.append(cover_percent)
    #print("%: " +str(cover_percent))
    #z += 1
    #print("Nr. " + str(z))

total_percent_baseline = 0
for p in list_cover_percent:
    total_percent_baseline += p

arith_Medium_baseline_perstent = (total_percent_baseline/(len(list_cover_percent)))

print("baseline medium: " + str(round(arith_Medium_baseline_perstent, 2)) + "%")

Abweichungsquadratsumme_baseline = 0
for x in list_cover_percent:
    Abweichungsquadratsumme_baseline += (x - arith_Medium_baseline_perstent)**2
korrigierte_empirische_Varianz_baseline = Abweichungsquadratsumme_baseline/(len(list_cover_percent) - 1)
Standardabweichung_baseline = math.sqrt(korrigierte_empirische_Varianz_baseline)
Standardabweichung_baseline_rounded = round(Standardabweichung_baseline, 2)
#print("korrigierte_empirische_Varianz for baseline: " + str(korrigierte_empirische_Varianz_baseline) + "sec")
print("Standardabweichung for baseline rounded: " + str(Standardabweichung_baseline_rounded) + "%")


# improved: 

list_field_copys_2 = []
for list in combienelist:
    list_field_copys_2.append(copy.copy(list[1])) 


paths_on_fields_HR = []
for list in combienelist:
    paths_on_fields_HR.append(copy.copy(list[4]))

    


list_cover_percent_HR = []
for x in range(0, len(paths_on_fields_HR)):

    covered_cubes = 0
    for cube in list_field_copys_2[x]:
        if paths_on_fields_HR[x].__contains__(cube) == True:
            covered_cubes += 1


    cover_percent = round((covered_cubes / len(list_field_copys_2[x])) * 100 , 2)

    #if cover_percent > 100:
        #cover_percent = 100.0

    list_cover_percent_HR.append(cover_percent)
    #print("HR %: " +str(cover_percent))
    #z += 1
    #print("Nr. " + str(z))

total_percent_improved = 0
for p in list_cover_percent_HR:
    total_percent_improved += p

arith_Medium_improved_perstent = (total_percent_improved/(len(list_cover_percent_HR)))

print("improved medium: " + str(round(arith_Medium_improved_perstent, 2)) + "%")

Abweichungsquadratsumme_improved = 0
for x in list_cover_percent_HR:
    Abweichungsquadratsumme_improved += (x - arith_Medium_improved_perstent)**2
korrigierte_empirische_Varianz_improved = Abweichungsquadratsumme_improved/(len(list_cover_percent_HR) - 1)
Standardabweichung_improved = math.sqrt(korrigierte_empirische_Varianz_improved)
Standardabweichung_improved_rounded = round(Standardabweichung_improved, 2)
#print("korrigierte_empirische_Varianz for improved: " + str(korrigierte_empirische_Varianz_improved) + "sec")
print("Standardabweichung for improved rounded: " + str(Standardabweichung_improved_rounded) + "%")


# doubled covered cubes:

list_field_copys_3 = []
for list in combienelist:
    list_field_copys_3.append(copy.copy(list[1])) 


doubled_covered_cubes_on_fields = []
for list in combienelist:
    doubled_covered_cubes_on_fields.append(copy.copy(list[6]))

double_cover_percent = []
for x in range(0, len(list_field_copys_3)):
    dc_percent = round((doubled_covered_cubes_on_fields[x] / len(list_field_copys_3[x])) * 100 , 2)
    double_cover_percent.append(dc_percent)

#for x in double_cover_percent:
   # print("dc: " + str(x) + "%")

total_dc_percent = 0
for p in double_cover_percent:
    total_dc_percent += p

arith_Medium_double_percent = (total_dc_percent/(len(double_cover_percent)))

print("dc medium: " + str(round(arith_Medium_double_percent, 2)) + "%")

Abweichungsquadratsumme_dc = 0
for x in double_cover_percent:
    Abweichungsquadratsumme_dc += (x - arith_Medium_double_percent)**2
korrigierte_empirische_Varianz_dc = Abweichungsquadratsumme_dc/(len(double_cover_percent) - 1)
Standardabweichung_dc = math.sqrt(korrigierte_empirische_Varianz_dc)
Standardabweichung_dc_rounded = round(Standardabweichung_dc, 2)
#print("korrigierte_empirische_Varianz for dc: " + str(korrigierte_empirische_Varianz_dc) + "sec")
print("Standardabweichung for double covered cubes rounded: " + str(Standardabweichung_dc_rounded) + "%")



# VLOS time

VLOS_time_t = []
for list in combienelist:
    VLOS_time_t.append(list[8])


VLOS_time_medium, VLOS_time_standab = medium_and_standartabweichung(VLOS_time_t)

print("VLOS time medium: " + str(VLOS_time_medium))
print("Vlos time standartabweichung: " + str(VLOS_time_standab))




# cover percent VLOS


list_field_copys_4 = []
for list in combienelist:
    list_field_copys_4.append(copy.copy(list[1])) 


paths_on_fields_VLOS = []
for list in combienelist:
    paths_on_fields_VLOS.append(copy.copy(list[7]))

    
list_cover_percent_VLOS = []
for x in range(0, len(paths_on_fields_VLOS)):

    covered_cubes = 0
    for cube in list_field_copys_4[x]:
        if paths_on_fields_VLOS[x].__contains__(cube) == True:
            covered_cubes += 1


    cover_percent = round((covered_cubes / len(list_field_copys_4[x])) * 100 , 2)

    list_cover_percent_VLOS.append(cover_percent)


total_percent_vlos = 0
for p in list_cover_percent_VLOS:
    total_percent_vlos += p

arith_Medium_vlos_perstent = (total_percent_vlos/(len(list_cover_percent_VLOS)))

print("vlos cover medium: " + str(round(arith_Medium_vlos_perstent, 2)) + "%")

Abweichungsquadratsumme_vlos = 0
for x in list_cover_percent_VLOS:
    Abweichungsquadratsumme_vlos += (x - arith_Medium_vlos_perstent)**2
korrigierte_empirische_Varianz_vlos = Abweichungsquadratsumme_vlos/(len(list_cover_percent_VLOS) - 1)
Standardabweichung_vlos = math.sqrt(korrigierte_empirische_Varianz_vlos)
Standardabweichung_vlos_rounded = round(Standardabweichung_vlos, 2)
#print("korrigierte_empirische_Varianz for vlos: " + str(korrigierte_empirische_Varianz_vlos) + "sec")
print("Standardabweichung for vlos cover rounded: " + str(Standardabweichung_vlos_rounded) + "%")

# VLOS double cover

all_dc_percent_VLOS = []
for list in combienelist:
    copyed_VLOS_path = copy.copy(list[7])
    copyed_field_5 = copy.copy(list[1])
    for cell in copyed_field_5:
        if copyed_VLOS_path.__contains__(cell):
            copyed_VLOS_path.remove(cell)

    dc_percent = round(((len(copyed_VLOS_path) + list[9]) / len(copyed_field_5)) * 100 , 2)
    all_dc_percent_VLOS.append(dc_percent)


VLOS_dc_medium, VLOS_dc_standab = medium_and_standartabweichung(all_dc_percent_VLOS)

print("VLOS dc medium: " + str(VLOS_dc_medium) + "%")
print("Vlos dc standartabweichung: " + str(VLOS_dc_standab) +"%")


    








