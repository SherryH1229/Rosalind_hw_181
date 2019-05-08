def readInfo(data):
    edgeDict = dict()
    for lines in data:
        line = ((lines.splitlines())[0]).split("->")
        info1 = line[0]
        info2 = line[1]
        
    edgeDict[info1] = info

def exe(data):
    edgeDict = readInfo(data)

data = open("pattern","r")
exe(data)