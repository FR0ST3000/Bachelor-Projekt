import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming
from Worldcreation import CreateWorld
from python_tsp.distances import great_circle_distance_matrix
from python_tsp.distances import euclidean_distance_matrix
import time

"""
dis_matrix  = np.array([
    [0,  5,  4, 10],
    [5,  0,  8,  5],
    [4,  8,  0,  3],
    [10, 5,  3,  0]
])
dis_matrix[:, 0] = 0
permutation, distance = solve_tsp_dynamic_programming(dis_matrix)
print(permutation)
print(distance)
#"""

newworld = CreateWorld(5,5,1)

newworld.setfieldzone(0,0,0,3,3,0)              # 3 x 4  =>  277 sec 
newworld.setflyzone(0,0,0,3,3,0)

fieldlists = newworld.getfield_lists()

"""
for x in fieldlists:
    print("new field -----")
    for y in x:
        print(y.getcoordinates())
#"""

cordlist = []

for cube in fieldlists[0]:
    cords = [cube.getcoordinates()[0], cube.getcoordinates()[1]]
    cordlist.append(cords)

#print(cordlist)
numpycordlist = np.array(cordlist)

# dismatrix2 = great_circle_distance_matrix(numpycordlist)
dismatrix2 = euclidean_distance_matrix(numpycordlist)
#print(len(dismatrix2))
#print(dismatrix2)

#for x in dismatrix2:
 #   print(x)

combotimelist = []
for x in range(0,10,1):
    start_time = time.time()
    permutation2, distance2 = solve_tsp_dynamic_programming(dismatrix2)
    end_time = time.time()
    print(permutation2)
    print(distance2)
    for x in newworld.get2dflymatrixoflevel(0):
        print(x)
    print("Time: " + str(round((end_time - start_time),2)) + " sec")
    combotimelist.append(round((end_time - start_time),2))

print(combotimelist)
#for x in permutation2:
 #   print(cordlist[x])

#for x in newworld.get2dflymatrixoflevel(0):
 #   print(x)

#print("Time: " + str(round((end_time - start_time),2)) + " sec")




