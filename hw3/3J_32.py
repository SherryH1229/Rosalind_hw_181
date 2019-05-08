#----------------Extra packages------------
import random

#----------------Extra functions------------
def prefix(pattern):
    prefix = pattern[0:-1]
    return prefix

def suffix(pattern):
    suffix = pattern[1:]
    return suffix

def getPairs (data):
    pairList = []
    for lines in data:
        pair = []
        info = lines.split("|")
        pair.append(info[0])
        pair.append(''.join(info[1].split()))
        pairList.append(pair)
    return pairList

def findStartNode(edgeDict):
    preNodes = edgeDict.keys()
    for preNode in preNodes:
        numOutEdge = len(edgeDict[preNode])
        numInEdge = 0
        for key, value in edgeDict.iteritems(): 
            numInEdge = numInEdge+(value.count(preNode))
        if numOutEdge > numInEdge:
            return preNode

def EulerianPath (edgeDict):
    startNode = findStartNode(edgeDict)
    avalNode = [startNode]
    path = []
    while len(avalNode) != 0:
        if len(avalNode) > 0:
            node = avalNode[-1]
            if node not in edgeDict:
                path.append(avalNode.pop())
                continue
            possNodes = edgeDict[node]
            if len(possNodes) > 0:
                nextNode = random.choice(possNodes)
                edgeDict[node].remove(nextNode)
                avalNode.append(nextNode)
            elif len(possNodes) == 0:
                path.append(avalNode.pop())
    
    eulerPath = path[::-1]
    return eulerPath

def stringCompByPath(string):
    outputString = []
    #print string[0]
    outputString.append(string[0])
    for i in range (1,len(string)):
        tempStr = string[i]
        outputString.append(tempStr[-1])
    return (''.join(outputString))

def stringSpelledByGappedPatterns(GappedPatterns,k,d):
    firstPatterns = [x[0] for x in GappedPatterns]
    secondPatterns = [x[1] for x in GappedPatterns]

    PrefixString = stringCompByPath(firstPatterns)
    SuffixString  = stringCompByPath(secondPatterns)
    
    for i in range ((k+d+1),len(PrefixString)):
        if (PrefixString[i]) != (SuffixString[(i-k-d)]):
            return "there is No String Spelled By th Gapped Patterns"
    
    return PrefixString+SuffixString[len(SuffixString)-(k+d):]
#----------------3J----------------
def reConstruct(pairList):
    edgeDict_pair = dict()
    for pair in pairList:
        newPre = prefix(pair[0])+prefix(pair[1])
        newSuff = suffix(pair[0])+suffix(pair[1])
        if newPre in edgeDict_pair:
            edgeDict_pair[newPre].append([newSuff])
        else:
            edgeDict_pair[newPre] = [newSuff] 
    return edgeDict_pair

def pair_reform(pathList,k):
    path_pair = []
    length = len(pathList[0])
    k = k-1
    for i in range (1,len(pathList)):
        pair = []
        read1 = pathList[i-1][0:k]+pathList[i][length-k-1]
        read2 = pathList[i-1][length-k:length]+pathList[i][length-1]
        
        pair.append(read1)
        pair.append(read2)
        path_pair.append(pair)

    return path_pair
        
def stringConstruction_readPair(data,k,d):
    pairs = getPairs(data)
    edgeDict_pair = reConstruct(pairs)
    path = EulerianPath(edgeDict_pair)
    path_pair = pair_reform(path,k)
    string = stringSpelledByGappedPatterns(path_pair,k,d)
    print string
    

data = open("pattern","r")
stringConstruction_readPair(data,30,100)
