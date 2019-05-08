def readInfo(data):
    info  = map(int,((data.read())[1:-1]).split())
    return info

def NumOfBreakpoints(numList):
    if numList[0] != 1:
        numBreaks = 1
    else:
        numBreaks = 0
    for k in range (1,len(numList)):
        if numList[k]-numList[k-1] !=1:
            numBreaks+=1

    return numBreaks

def exe(data):
    oriList = readInfo(data)
    print(NumOfBreakpoints(oriList))

data = open("pattern","r")
exe(data)