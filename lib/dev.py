from .freebie import Freebie

class Dev:
    
    def __init__(self, name):
        self.name = name

    @property
    def freebies(self):
        return [f for f in Freebie.all if f.dev == self]
    
    @property
    def companies(self):
        return [f.company for f in self.freebies]
    