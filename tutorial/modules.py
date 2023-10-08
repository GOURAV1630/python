## Two ways to import  module

# method 1 - 
import utils

a = utils.kg_to_lbs(73.5)
b = utils.lbs_to_kg(165)
print(b)
print(a)

# method 2 - 
from utils import kg_to_lbs

print(kg_to_lbs(74))