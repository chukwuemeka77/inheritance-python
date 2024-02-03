class Vehicle:
 #super class 
 def __init__(self, wheel, color):
          self.wheel=wheel
          self.color=color


def movement(self):
     print("All vehicles can move")



class Car(Vehicle):
     def __init__(self, wheel, color):
          
          self.wheel=wheel
          self.color=color

     def transportation(self):
      print("A car can move from one place to another")

car=Car("4 wheels", "variety of colors")
car.transportation()