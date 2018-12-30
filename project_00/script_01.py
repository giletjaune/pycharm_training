#  * * * Import libraries * * *
import numpy as np

a = 5
b = 6
c = [i+44 for i in np.arange(a)]
d = "salut tu vas bien?"

#  * * * Define functions * * *
def add_prefix(target,prefix):
    return str(prefix) + "_" + str(target)

def build_sentence(number_of_items):
    sequence = np.arange(number_of_items)
    L = []
    for item in sequence:
        temp = add_prefix(item,"the_prefix")
        L.append(temp)
    return L


#  * * * Run * * *
master_result = build_sentence(10)
print(master_result)