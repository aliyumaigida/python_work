
# import time
# class Car: 
#     def __init__(self):
#         self.owner = "John Smith"
#         self.location = "Lagos"
#         self.name = "Toyota"
#         self.color = "Brown"
#         self.brand = "2023 model"
#         self.trafficator = "straight"
#         self.tyre  = 4
#         self.stiring = 1
#         self.gear = "0"
#         self.speed = "10km/h"
        
#         self.details()

#     def details(self):
#         print("This car is owned by "+self.owner+ " and is located in "+self.location+".\n This car was built by "+self.name+" and is "+self.color+" in color and the model is "+self.brand)
#         time.sleep(2)
        
#         self.startEnging()

#     def startEnging(self):
#         print("the engine is started")
#         time.sleep(2)
#         self.gear = input("Enter gear 1 to take off")
#         if self.gear == "1":
#                 self.movecar()
#         else:
#             print("that is not the right gear to take off")
#             self.startEnging()
#     def moveCar(self):
#         print(self.name+' is in gear '+self.gear +" and the car is moving "+ self.trafficator+ " at a speed of "+self.speed)
#         self.driver = input("press Y to change gear, D to change direction, S to change speed and P to pack")
#         if self.driver.upper() == "Y":
#             self.changeGear()
#         elif self.driver.upper() == "D":
#             self.direction()
#         elif self.driver.upper() == "S":
#             self.changeSpeed()
#         elif self.driver.upper() == "P":
#             self.park()
#         else:
#             self.moveCar()

#     def changeGear(self):
#         self.gear = input("Enter gear number ")
#         self.moveCar()

#     def direction(self):
#         self.trafficator = input("please enter your direction ")
#         self.moveCar()

#     def changeSpeed(self):
#         newSpeed = int(input("Enter you speed "))
#         if self.gear == "1" and newSpeed > 30:
#             print("incompatible speed. Gear must not be greater than 30 when on gear 1")
#             self.moveCar()
#         elif self.gear == "2" and newSpeed > 60:
#             print("incompatible speed. Gear must not be greater than 60 when on gear 2")
#             self.moveCar()
#         elif self.gear == "3" and (newSpeed > 120 or newSpeed < 60):
#             print("incompatible speed. Gear must be between 60 and 120 when on gear 3")
#             self.moveCar()
#         else:
#             self.speed = str(newSpeed) + "km/h"
#             self.moveCar()

#     def park(self):
#         print('the car is parking now ...')
#         time.sleep(2)
#         print("The car has finished parking and appliction exited")
        
# if __name__ == '__main__':
#     cr = Car()




# Python Inheritance 

class Father:

  def __init__(self):
      self.family_name = "Adeowo"
      self.name = "Owolabi"
      self.skin_color = "dark skin"
      self.height = "tall"
      self.language = "Yoruba"

  def walk(self):
      print(self.name+ " from "+self.family_name+" is walking")
  
  def talk(self):
      print(self.name +' from '+self.family_name+' is talking')

  def sleep(self):
      print(self.name +' is still sleeping')


class Child(Father):
   pass

ch = Child()
# # ch.walk()
# print(ch.skin_color)
# ch.talk()
# ch.name = "Micheal"
# print(ch.name)


class Child(Father):
    def __init__(self):
        self.name = "Charse"
        self.height = "short"
    
    def jump(self):
        print(self.name+ " is jumping up and down")

ch = Child()

ch.sleep()
ch.jump()


class Child1(Father):
    def __init__(self):
        Father__init__(self)
        # either father or super is the same
        super().__init__()
        self.name = "Charse"
        self.height = "short"
        self.hair_style = "Afro"
    
    def jump(self):
        print(self.name+ " is jumping up and down")


class Child2(Father):
    def __init__(self):
        super().__init__()
        self.name = "Micheal"
        self.height = "Half-short"
        self.foot_size = "small foot"
    def run(self):
        print(self.name+ " is running up and down")

# fd = Father()
# ch = Child1()
# ch2 = Child2()
# fd.talk()
# print(ch.name)
# ch.talk()
# fd.jump()
# print(fd.hair_style)
# ch2.talk()
# print(ch2.family_name)
# ch2.walk()
# print(ch2.height)
# ch2.jump()

# class GrandChild(Child1):
#     def __init__(self):
#         super().__init__()
#         self.name = "Sunday"
    
#     def jump(self):
#         print(self.name + " is jumping at the olympic")

# ch = Child1()
# print(ch.language)
# ch.walk()
# gd = GrandChild()
# print(gd.height)
# print(gd.foot_size)
# print(gd.hair_style)
# print(gd.skin_color)
# gd.jump()
# gd.walk()

# class Dog:
    
#     def __init__(self):
#         self.breed = "Bingo"
#         self.name = "Dog"
        
#     def bark(self):
#         print(self.breed + "is barking.")
    
# class Bird:
    
#     def __init__(self):
#         self.name = "Bird"
#         self.species = "Flamingo"
        
#     def fly(self):
#         print(self.breed + "is flying.")
        
# class FlyingDog(Dog, Bird):
#     def __init__(self):
#         Dog.__init__(self)
#         Bird.__init__(self)


    