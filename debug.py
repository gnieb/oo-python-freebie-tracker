import ipdb
from lib import *



c1 = Company('Meta', 2000)
c2 = Company('Google', 1989)
d1 = Dev('Dakota')
d2 = Dev('Connor')
d3 = Dev('Grace')
f1 = Freebie( c1, d1, 'hoodie', 100)
f2 = Freebie( c1, d2, 'yeti', 400)
f3 = Freebie(c2, d3, 'house', 100000)
f4 = Freebie(c2, d2, 'car', 50000)


ipdb.set_trace()