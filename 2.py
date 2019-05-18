import random
import string

array = []
lettersAndDigits = string.ascii_letters + string.digits

def generateString(number_generated):
    for i in range(number_generated):
        art = ""
        stringLength=32
        art += ''.join(random.sample(lettersAndDigits,stringLength))
        array.append(art)
    return array

print(generateString(3))
