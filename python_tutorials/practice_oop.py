class person:
    def __init__(self , rider , been_ridden) :
      self.rider = rider
      self.ridden = been_ridden
      print("here comes new couple")

    def riding(self):
       print(f"{self.rider} rides {self.ridden}")


first = person("drogo","danny")
second = person("tyrio","who*es")
third=person("jamie","cercie")

first.riding()
third.riding()
second.riding()
     