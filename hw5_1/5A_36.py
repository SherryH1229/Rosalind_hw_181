def readInfo(data):
    info = []
    for lines in data:
        info.append(lines.splitlines())
    totlAmount = int(info[0][0])
    coinSet = map(int,info[1][0].split(","))
    #print coinSet
    return totlAmount,coinSet

def miniCoins(data):
    totalAmount,coinSet = readInfo(data)
    minimumCoin = []
    for i in range (totalAmount+1):
        minimumCoin.append(0)
    for m in range (1,totalAmount+1):
        minimumCoin[m] = float("inf")
        for coin in coinSet:
            if m >= coin:
                if (minimumCoin[m-coin]+1) < minimumCoin[m]:
                    minimumCoin[m] =  minimumCoin[m-coin]+1

    print minimumCoin[totalAmount]
    print minimumCoin

data = open("pattern","r")
miniCoins(data)