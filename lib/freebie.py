
class Freebie:
    
    all = []

    def __init__ (self, c_instance, d_instance, item, value=0):
        self.company = c_instance
        self.dev = d_instance
        self.item = item
        self.value = value
        Freebie.all.append(self)

    @property
    def print_details(self):
        print(f"{self.dev.name} owns a {self.item} from {self.company.name}")