class warrior:
    def __init__(self,name,weapon):
        self.name=name
        self.weapon=weapon
    
    def battle_cry(self):
        print("for glory")


class commandor(warrior):
    def __init__(self,name,weapon,rank):
        super.__init__(name,weapon)
        self.rank=rank
        print(f"by order of {self.rank}")

    
jon=commandor("jon","valerain stell","lord cmdr")
jon.battle_cry()


