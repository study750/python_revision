class character:
    kingdom="westros"
    def __init__(self,name,house):
        self.name=name
        self.house=house
        print("fucku but i am made at start")

    def speak(self):
        print(f"my name is {self.name} and my house is {self.house}")

jon = character("jon","targeryan")
print(jon.kingdom)

arya=character("arya","start")
character.kingdom="essos"
print(arya.kingdom)

cersi=character("cersi","baratheon")
print(cersi.kingdom)
cersi.kingdom="dhule"   # seprate for cersi