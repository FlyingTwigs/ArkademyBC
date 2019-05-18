import random
import string
import numpy as np


array = []
lettersAndDigits = string.ascii_letters + string.digits

def randomUniqueStringDigits(stringLength=32):
    """Generate a random string of letters and digits """
    return ''.join(random.sample(lettersAndDigits, stringLength))

r = int(input())
for i in range(r):
    array = np.append(array, randomUniqueStringDigits(32))

print(array)
