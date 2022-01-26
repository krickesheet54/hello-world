"""
Author: Kricketune54
Date: 1/26/2022
File Description: Based off Pierian Data OOP homework.  
Classes for Line and Cylinders, with attributes for several different equations.
"""

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        # create separate x and y coordinate pairs
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2 - y1) / (x2 - x1)
      
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius 
        
    def volume(self):
        return 3.14 * (self.radius ** 2) * self.height 
    
    def surface_area(self):
        return (2 * 3.14 * self.radius * self.height) + 2 * 3.14 * (self.radius ** 2)     
      
      
# Example Line Output

coordinate1 = (1,5)
coordinate2 = (6,9)

li = Line(coordinate1,coordinate2)
li.coor1
li.distance()


# Example Cylinder Output
c = Cylinder(6,7)
c.radius
c.volume()
c.surface_area()
