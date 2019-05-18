def minMax(data):
    index = 0
    minimumValue = data[index]

    for i in range(len(data)):
        if (minimumValue > data[i]):
            minimumValue = data[i]
            index=i


    maximumValue=data[index]


    for r in range(index,len(data)):
        if (maximumValue < data[r]):
            maximumValue = data[r]


    return [minimumValue, maximumValue]

# contoh eksekusi

data = ['h','g','a','b','c','f']
print(minMax(data))
