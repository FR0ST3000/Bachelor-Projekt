class CubeinSpace:
    def __init__ (self, x,  y,  z, flyable, walkable, VLOS, field, Ground_Object, cubenummber):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.flyable = int(flyable)
        self.walkable = int(walkable)
        self.VLOS = int(VLOS)
        self.field = int(field)
        self.Ground_Object = int(Ground_Object)
        self.cubenummber = int(cubenummber)
        #self.gcost = 0
        #self.hcost = 0
        #self.fcost = 0

    def getcoordinates(self):
        coordinates = [self.x,self.y,self.z]
        return(coordinates)
    
    def getflyable(self):
        if self.flyable == 1:
            return(1)
        else: 
            return(0)

    def setflyable(self, i):      # in True/False ?
        if i == 1:
            self.flyable = 1
        if i == 0:
            self.flyable = 0

    def getwalkable(self):
        if self.walkable == 1:
            return(1)
        else: 
            return(0)

    def setwalkable(self, i):     # in True/False ?
        if i == 1:
            self.walkable = 1
        if i == 0:
            self.walkable = 0

    def getVLOS(self):
        if self.VLOS == 1:
            return(1)
        else: 
            return(0)

    def setVLOS(self, i):     # in True/False ?
        if i == 1:
            self.VLOS = 1
        if i == 0:
            self.VLOS = 0

    def getfield(self):
        if self.field == 1:
            return(1)
        else: 
            return(0)

    def setfield(self, i):     # in True/False ?
        if i == 1:
            self.field = 1
        if i == 0:
            self.field = 0

    def getGround_Object(self):
        if self.Ground_Object == 1:
            return(1)
        else: 
            return(0)

    def setGround_Object(self, i):     # in True/False ?
        if i == 1:
            self.Ground_Object = 1
        if i == 0:
            self.Ground_Object = 0

    def getcubenummber(self):
        return(self.cubenummber)


    
   
# TESTS ---------------------------

"""
cube1 = CubeinSpace(1,2,3,1,0,1,0,0)
print(cube1.flyable)
print(cube1.getflyable())
print(cube1.getwalkable())
print(cube1.getVLOS())
print(cube1.getfield())
print(cube1.getcoordinates())
cube1.setflyable(0)
cube1.setwalkable(1)
print(cube1.getflyable())
print(cube1.getwalkable())
cube1.setflyable(1)
cube1.setwalkable(0)
print(cube1.getflyable())
print(cube1.getwalkable())
"""
