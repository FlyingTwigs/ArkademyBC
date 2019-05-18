import random
import string

array = []
result = []
lettersAndDigits = string.ascii_letters + string.digits


def generateString(number_generated):
    for i in range(number_generated):
        art = ""
        stringLength=32
        art += ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
        array.append(art)
    return array


def uniqueCharacter():
    for y in array:
        if y not in result:
            result.append(y)
    return result


generateString(3)
print(uniqueCharacter())
