import random
import Worldcreation
import CubeClass
from CubeClass import CubeinSpace
from Worldcreation import CreateWorld
from GBWCpathfinder import GBWC
import time
import copy
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy as scipy
from scipy.interpolate import interp1d
from pathwitklos import Path_with_VLOS


random.seed(9000)

def gen_field_world_with_x_cells_removed(cut_cells):

    NewWorld = CreateWorld(17,12,1)
    NewWorld.setfieldzone(1,1,0,15,10,0)
    NewWorld.setflyzone(1,1,0,15,10,0)
    NewWorld.setwalkzone(0,0,0,16,0,0)
    NewWorld.setwalkzone(0,0,0,0,11,0)
    NewWorld.setwalkzone(0,11,0,16,11,0)
    NewWorld.setwalkzone(16,0,0,16,11,0)

    returnworld = 0

    org_field = NewWorld.getfield_lists()[0]

    x = 0
    runs = 0
    while x == 0 and runs < 100:
        runs += 1
        field = copy.copy(org_field)
        removed_cells = 0
        while removed_cells < cut_cells:
            nr_of_cell_to_remove = random.randrange(len(field))
            field.remove(field[nr_of_cell_to_remove])
            removed_cells += 1

        testworld = CreateWorld(17,12,1)
        for cube in field:
            cube_cor = cube.getcoordinates()
            testworld.setfieldzone(cube_cor[0], cube_cor[1], cube_cor[2], cube_cor[0], cube_cor[1], cube_cor[2])
            testworld.setflyzone(cube_cor[0], cube_cor[1], cube_cor[2], cube_cor[0], cube_cor[1], cube_cor[2])
        if len(testworld.getfield_lists()) == 1:
            x = 1
            returnworld = testworld

    if runs == 100:
        print("!!! runs over limit -> field is cut in half !!!")  
        return None   

    #"""       
    for line in testworld.get2dflymatrixoflevel(0):
        xline = []
        for cube in line:
            xline.append(cube) 
        print(xline)
    #"""

    return returnworld


def tests_with_single_cube_cut(test_per_field, max_cube_cut):

    cubes_cut = 0
    complete_list = []   # [combinelist for fields_missing_0_cells, combinelist for fields_missing_1_cells, ......]

    while cubes_cut < (max_cube_cut+1):
        

        combienelist = []               # combinelist[x] = [2dflymap, field as list of cubes, GBWCpath of the field, time of GBWCpath creation, GBWCpath_heuristic/restep of the field, time of GBWCpath_heuristic/restep creation, doubled covered cubes, HR path with no doubles]


        while len(combienelist) < test_per_field:

            NewWorld = gen_field_world_with_x_cells_removed(cubes_cut)

            fields = NewWorld.getfield_lists()
            NewWorld.getdimesions()

            
            temp_list = []
            temp_list.append(NewWorld.get2dflymatrixoflevel(0))
            temp_list.append(fields[0])

            GBWCobj = GBWC(NewWorld.getWorld()) 
            #path_w_VLOS = Path_with_VLOS(NewWorld.getWorld())

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

            endpoint_for_GBWC = startpoint_for_GBWC

                
            copyed_field_1 = copy.copy(fields[0])
            copyed_field_2 = copy.copy(fields[0])
            copyed_field_3 = copy.copy(fields[0])

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

        #"""



        complete_list.append(combienelist)

        cubes_cut += 1

    return complete_list

def medium_and_standartabweichung(input_list):

    total_input_list = 0
    for i in input_list:
        total_input_list += i

    arith_Medium = (total_input_list/(len(input_list)))

    print("medium form method: " + str(arith_Medium))

    Abweichungsquadratsumme= 0
    for x in input_list:
        Abweichungsquadratsumme += (x - arith_Medium)**2
    korrigierte_empirische_Varianz_improved = Abweichungsquadratsumme/(len(input_list) - 1)
    Standardabweichung = math.sqrt(korrigierte_empirische_Varianz_improved)
    #Standardabweichung_improved_rounded = round(Standardabweichung_improved, 5)
    #print("korrigierte_empirische_Varianz for improved: " + str(korrigierte_empirische_Varianz_improved) + "sec")
    print("Standardabweichung form method rounded: " + str(Standardabweichung))
    return [arith_Medium, Standardabweichung]

"""
total_list = tests_with_single_cube_cut(100, 50)

for cobine_list in total_list:
    for list in cobine_list:
        twodflymap = list[0]
        print("-----------------------")
        for xline in twodflymap:
            print(xline)
print("len comlete_list: " + str(len(list)))
print("len comlete_list[0]: " + str(len(list[0])))
print("len comlete_list[0][0]: " + str(len(list[0][0])))


all_mediums_for_double_cover = []
all_stanab_for_double_cover = []
for combine_list in total_list:
    double_covered_cube_list = []
    for list in combine_list:
        double_covered_cube_list.append(list[6])
    med, sta = medium_and_standartabweichung(double_covered_cube_list)
    all_mediums_for_double_cover.append(med)
    all_stanab_for_double_cover.append(sta)

print(all_mediums_for_double_cover)
print(all_stanab_for_double_cover)

x = []
for i in range(0, len(all_mediums_for_double_cover)):
    x.append(i)
y1 = all_mediums_for_double_cover
y1err = all_stanab_for_double_cover

  
# plot data in grouped manner of bar type
plt.plot(x, y1, color='purple' )#color=(0.0, 0.615, 0.505, 0.99))
plt.errorbar(x, y1, xerr = 0, yerr = y1err, ls = 'none', color='red')#color='purple')
plt.xlabel('Anzahl der entfernten Zellen', color='black')
plt.ylabel('Doppelte Abdeckung in %', color='black')
plt.ylim(0, 16)
plt.show()

#"""



