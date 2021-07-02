import math

numBaseTen = int(input('Enter a number: '))

def function(baseTen):
    binaryNum = 0
    rootBaseTen = math.floor(math.log2(baseTen))

    while baseTen > 0:
        binaryNum += 10 ** rootBaseTen
        baseTen -= 2 ** rootBaseTen
        if (baseTen == 0):
            return binaryNum
        rootBaseTen = math.floor(math.log2(baseTen))

    return binaryNum

print(function(numBaseTen))