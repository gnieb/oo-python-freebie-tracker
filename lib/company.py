from lib.freebie import Freebie

class Company:
    
    all = []

    def __init__(self, c_name, founding_year):
        self.name = c_name
        self.founding_year = founding_year
        Company.all.append(self)

    @property
    def freebies(self):
        return [f for f in Freebie.all if f.company == self ]
    
    @property 
    def devs(self):
        return [f.dev for f in Freebie.all if f.company == self ]

        ## OR ###
        # use the above method to grab the list returned and go thru that
        # return [f.dev for f in self.freebies]
    
    def give_freebie(self, d_instance, item, value=0):
        return Freebie(self, d_instance, item, value)
    

    @classmethod
    def oldest_company(cls):
        company_years = [c.founding_year for c in Company.all]
        sorted_company_years = sorted(company_years)
        for c in Company.all:
            if c.founding_year == sorted_company_years[0]:
                return c
            
        ########## OR ###########

        #earliest_year = 3000 => we set it pretty low because we know ALL our years will be more than that
        #found_instance = ''
        #for c in cls.all:
            if c.founding_year < earliest_year:
                earliest_year = company.founding_year
                


