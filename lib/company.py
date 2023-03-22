from lib.freebie import Freebie

class Company:
    
    def __init__(self, name, year):
        self.name = name
        self.fy = year

    @property
    def freebies(self):
        return [f for f in Freebie.all if f.company == self]
    
    @property
    def devs(self):
        return [f.dev for f in self.freebies]
    