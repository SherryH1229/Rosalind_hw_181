#----------------Extra packages------------
import random
#----------------extra_functions-----------
def getEdges (dataset):
    edgeDict = dict()
    #outEdgeCount = dict()
    for lines in dataset:
        input = lines.split()  
        preNode = input[0]
        suffs = input[2]
        suffNode = []
        suffs = input[2].split(",")
        for suff in suffs:
            suffNode.append(suff)
        edgeDict[preNode] = suffNode

    return edgeDict

def prefix(pattern):
    prefix = pattern[0:-1]
    return prefix

def suffix(pattern):
    suffix = pattern[1:]
    return suffix

def kmerComp(k,string):
    kmerList = []
    for i in range (len(string)-k+1):
        kmerList.append(string[i:i+k])
    kmerList.sort()
    return kmerList
def buildDebruijnMatrix(KmerList):
    #remove duplicates
    KmerList = set(KmerList)
    KmerList  = list(KmerList)
    KmerList.sort()
    
    length = len(KmerList)
    Matrix = [[0 for x in range(length)] for y in range(length)] 

    return (KmerList,Matrix)

def DeBruijnGraph (num,KmerList,patterString):
    colnames, DebruijnMatrix = buildDebruijnMatrix(KmerList)
   
    for pattern in patternString:
        #print ''.join(pattern)
        preNode = prefix(''.join(pattern))
        sufNode = suffix(''.join(pattern))
        i = colnames.index(preNode)
        j = colnames.index(sufNode)
        DebruijnMatrix[i][j] = DebruijnMatrix[i][j]+1

    return DebruijnMatrix, colnames

def findStartNode(edgeDict):
    preNodes = edgeDict.keys()
    for preNode in preNodes:
        numOutEdge = len(edgeDict[preNode])
        numInEdge = 0
        for key, value in edgeDict.iteritems(): 
            numInEdge = numInEdge+(value.count(preNode))
        if numOutEdge > numInEdge:
            return preNode

def stringCompByPath(string):
    outputString = []
    outputString.append(string[0])
    for i in range (1,len(string)):
        tempStr = string[i]
        outputString.append(tempStr[-1])
    return (''.join(outputString))
#-------------3H-------------------
def getEdgeDict_BruijnGraph(DebruijnMatrix,colnames):
    i = 0
    edgeDict = dict()
    for row in DebruijnMatrix:
        preNode = colnames[i]
        
        j = [k for k, e in enumerate(row) if e != 0]
        suff = []
        if len(j) != 0:
            for index in j:
                for k in range (row[index]):
                    suff.append(colnames[index])
            
            edgeDict[preNode] = suff
        i = i+1
    
    return edgeDict

def EulerianPath_DNAString (edgeDict):
    path = []
    startNode = findStartNode(edgeDict)
    avalNode = [startNode]
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

patterns = open("pattern","r")
patternString = []
for line in patterns:
    patternString.append(line.splitlines())

#def getUniqKmer
length = len((patternString[0])[0])
flat_PatternString = ([item for sublist in patternString for item in sublist])

uniqueK_1_mers = []
for pattern in flat_PatternString:
    uniqueK_1_mers.append(prefix(pattern))
    uniqueK_1_mers.append(suffix(pattern))

matrix,colnames = DeBruijnGraph(length,uniqueK_1_mers,flat_PatternString)
edgeDict = getEdgeDict_BruijnGraph(matrix,colnames)

path = EulerianPath_DNAString(edgeDict)

#['GGC', 'GCT', 'CTT', 'TTA', 'TAC', 'ACC', 'CCA']
stringCompByPath(path)
