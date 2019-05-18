def myCountChar(word,toCount):
    counter = 0
    for letter in word:
        if (letter==toCount):
            counter+=1

    return counter

# Contoh
print(myCountChar("wooooooooooo","o"))
