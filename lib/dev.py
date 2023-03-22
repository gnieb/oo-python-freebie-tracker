from .freebie import Freebie

class Dev:
    
    all = []

    def __init__(self, name):
        self.name = name
        Dev.all.append(self)

    @property
    def freebies(self):
        return [f for f in Freebie.all if f.dev == self]
    
    @property
    def companies(self):
        return [f.company for f in self.freebies]
    
    def received_one(self, item_name):
        for f in self.freebies:
            if f.item_name == item_name:
                return True
            else:
                return False
    
    def give_away(self, dev, freebie):
        if freebie.dev == self:
            freebie.dev = dev
        else:
            print("THAT DOESN'T BELONG TO YOU")