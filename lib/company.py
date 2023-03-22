from lib.freebie import Freebie

class Company:
    
    all = []

    def __init__(self, name, year):
        self.name = name
        self.fy = year
        Company.all.append(self)

    @property
    def freebies(self):
        return [f for f in Freebie.all if f.company == self]
    
    @property
    def devs(self):
        return [f.dev for f in self.freebies]
    

    def give_freebie(self, dev, item_name, value):
        Freebie(self, dev, item_name, value)

    @classmethod
    def oldest_company(cls):
        earliest_year = 99999
        found_company = ''
        for c in cls.all:
            if c.fy < earliest_year:
                earliest_year = c.fy
                found_company = c.name
        return found_company
    