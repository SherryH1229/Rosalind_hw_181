def readInfo(data):
    info  = ((data.read())[1:-1]).split()
    return info

def GreedySorting(oriList):
    for k in range (0,len(oriList)):
        if oriList[k] != str("+"+str(k+1)):
            start = oriList[k]
            if (str("+"+str(k+1))) in oriList:
                endIndex = oriList.index(str("+"+str(k+1)))
            else:
                endIndex = oriList.index(str("-"+str(k+1)))
            oriList[k:endIndex+1] = oriList[k:endIndex+1][::-1]
            
            for i in range (k,endIndex+1):
                if oriList[i][0] == "+":
                    oriList[i] = str("-"+oriList[i][1:])
                elif oriList[i][0] == "-":
                    oriList[i] = str("+"+oriList[i][1:])
            print "("+' '.join(oriList)+")"
            if oriList[k] == str("-"+str(k+1)):
                oriList[k] = str("+"+oriList[k][1:])
                print "("+' '.join(oriList)+")"

def exe(data):
    oriList = readInfo(data)
    GreedySorting(oriList)

data = open("pattern","r")
exe(data)