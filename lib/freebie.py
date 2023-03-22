
class Freebie:
    
    all = []

    def __init__(self, company, dev, item, value):
        self.dev = dev
        self.company = company
        self.item_name = item
        self.value = value
        Freebie.all.append(self)

    @property
    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}."
    