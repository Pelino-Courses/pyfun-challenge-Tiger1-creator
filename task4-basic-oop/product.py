#docstring
""" this is a class which uses methods to add product, removing product, calculating
 the total amount product and displaying the output
"""
class Product: #class definition
    def __init__(self,name,price,quantity):# this is a constructor
        self.name=name
        self.price=price
        self.quantity=quantity
        if price <0: #validation of inputs
            raise ValueError("price must be a positive") #error handling
    def adding(self,amount):
        if amount <0:
            raise ValueError("amount must be positive")
        self.quantity +=amount
    def removing(self,amount):
        if amount <0:
            raise ValueError("insuffient amount")
        self.quantity -=amount
    def total(self):
        return self.quantity*self.price
    # displaying the output
    def displaying(self):
        print("product name is: ",self.name)
        print("Product's price is: ",self.price)
        print("Product's Quantity: ",self.quantity)
        print("Total value is: ",self.total())
#object declaration is on the shapes_demo file