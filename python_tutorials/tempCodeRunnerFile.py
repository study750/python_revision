class vehicle():
    def __init__(self):
        print("i am parent of everyone")

    def has(self):
        print("petrol")

    def have(self):
        print("no fule")

class car(vehicle):
    def __init__(self):
        self.has()
        self.have()
        print("i am car")

    def have(self):
        print("i am having")
    
   

class bike(vehicle):
    def __init__(self):
        self.have()
        print(" i am bike")


v=vehicle()
c=car()
b=bike()