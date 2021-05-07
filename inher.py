# class Vehicle:
#     def general_usage(self):
#         print("general use: transportation")
# class Car(Vehicle):
#     def __init__(self):
#         print("I am car")
#         self.wheels=4
#         self.has_roof=True
#     def specefic_usage(self):
#         print("specific use: commute to work, vacation with family")

# class MotorCycle(Vehicle):
#     def __init__(self):
#         print("I am motor cycle")
#         self.wheels=2
#         self.has_roof=False
    
#     def specefic_usage(self):
#         print("specific use: road trip. racing")


# c=Car()
# c.general_usage()
# c.specefic_usage()

# m=MotorCycle()
# m.general_usage()
# m.specefic_usage()

# class Vehicle:
#     def general_usage(self):
#         print("general use: transportation")
# class Car(Vehicle):
#     def __init__(self):
#         print("I am car")
#         self.wheels=4
#         self.has_roof=True
#     def specefic_usage(self):
#         self.general_usage()
#         print("specific use: commute to work, vacation with family")

# class MotorCycle(Vehicle):
#     def __init__(self):
#         print("I am motor cycle")
#         self.wheels=2
#         self.has_roof=False
    
#     def specefic_usage(self):
#         self.general_usage()
#         print("specific use: road trip. racing")


# c=Car()

# c.specefic_usage()

# m=MotorCycle()

# m.specefic_usage()

class Vehicle:
    def general_usage(self):
        print("general use: transportation")
class Car(Vehicle):
    def __init__(self):
        print("I am car")
        self.wheels=4
        self.has_roof=True
    def specefic_usage(self):
        self.general_usage()
        print("specific use: commute to work, vacation with family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I am motor cycle")
        self.wheels=2
        self.has_roof=False
    
    def specefic_usage(self):
        self.general_usage()
        print("specific use: road trip. racing")


c=Car()
m=MotorCycle()
isinstance(c,Car)
print(isinstance(c,MotorCycle))
print(issubclass(Car,Vehicle))
print(issubclass(Car,MotorCycle))
