class character:
    def __init__(self,name,house):
        self.name=name
        self.house=house
        print("fucku but i am made at start")

    def speak(self):
        print(f"my name is {self.name} and my house is {self.house}")

jon = character("jon","targeryan")
jon.speak()

arya=character("arya","start")