""" this first file contains inhertance: class definition, methos ,attributes, validation and rhis docstring   """
from math import pi #this is maths modules
class Shape: #parent class
    def __init__(self,name):
        self.name=name
    def Area(self):# method definition
        pass
    def __str__(self):
        return("the shape name is: ",self.name)

class Circle(Shape): #child class circle inhert fron parent class
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius=radius
        if radius<=0:
            raise ValueError("The radius must be positive number")
    def Area(self):
        return (self.radius **2) *  pi
    def __str__(self):
        return (f"the Area of Circle is: {self.Area()}") 
class Rectangle(Shape): #child class Rectangle inhert from parent class "Shape"
    def __init__(self,length,width):
        super().__init__("Rectangle") 
        if length==0 or width ==0:
            raise ValueError("invalid sizes")
        if length == width:
           raise ValueError("This is a square, not a rectangle")  
             
        self.length=length 
        self.width=width 
    def Area(self):
        return self.length * self.width
    def __str__(self):
       return f"the Area of Rectangle is {self.Area()}" 
        
class Triangle(Shape): # child class Triangle 
    def __init__(self,A,B,C):
        super().__init__("Triangle")   
        if A<=0 or B<=0 or C<=0:
            raise ValueError("invalid Triangle sides")
        if A+B == C:
            raise ValueError("Invalid Triangle")
        
        self.A=A
        self.B=B
        self.C=C
    def Area(self):
        return (self.A * self.B)/2
    def __str__(self):
        return (f" The Area of Triangle is {self.Area()}")
