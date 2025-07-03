class vehicle():
    def __init__(self):
        print("i am parent of everyone")

    def has(self):
        print("petrol")

    def have(self):
        print("no fule")

class newvehicle():
    def has(self):
        print("putol")

class car(vehicle):
    def __init__(self):
        self.has()
        self.have()
        print("i am car")

    def have(self):
        print("i am having")
    
   

class bike(vehicle,newvehicle):
    def __init__(self):
        self.have()
        print(" i am bike")
        super().has()
        newvehicle.has(self)

    


v=vehicle()
c=car()
b=bike()
