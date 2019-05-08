#----------------Extra packages------------
import random
#-------------extra_functions----------
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

def DeBruijnGraph (num,KmerList,patternString):
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
            print preNode
            return preNode

def stringCompByPath(string):
    outputString = []
    outputString.append(string[0])
    for i in range (1,len(string)):
        tempStr = string[i]
        outputString.append(tempStr[-1])
    return (''.join(outputString))

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
#-------------3I-------------------
def generateBinaryStrings(k):
    binaries = []
    for i in range(2**k):
        binaryString =  bin(i)[2:]
        binaryString = "0"*(k-len(binaryString))+binaryString
        binaries.append(binaryString)

    return binaries

def EulerCycle (preNode,edgeDict):
    cycle = []
    cycle.append(preNode)
    keys = edgeDict.keys()
    while True:
        if len(edgeDict[preNode]) > 0:
            suffNode = edgeDict[preNode].pop(0)
            cycle.append(suffNode)
            preNode = suffNode
        else:
            for key in keys:
                if len(edgeDict[key]) == 0:
                    edgeDict.pop(key,None)
           
            return cycle
        
def EulerianCycle_string (edgeDict): 
    firstNode = random.choice(edgeDict.keys())

    eulerCycle = EulerCycle(firstNode,edgeDict)    
    while len(edgeDict) != 0:
        avalNode = edgeDict.keys()
        possNode = []
        for node in eulerCycle:
            if node in avalNode:
                possNode.append(node)
        nextFirstNode = random.choice(possNode)
        connetIndex = eulerCycle.index(nextFirstNode)
        nextCyle = EulerCycle(nextFirstNode,edgeDict)
        
        eulerCycle = eulerCycle[connetIndex:] + eulerCycle[1:connetIndex+1] + nextCyle[1:]

    return eulerCycle


def K_universal (k):
    binaryList = generateBinaryStrings(k)
    uniqueK_1_mers = []
    for pattern in binaryList:
        uniqueK_1_mers.append(prefix(pattern))
        uniqueK_1_mers.append(suffix(pattern))

    matrix,colnames = DeBruijnGraph(k,uniqueK_1_mers,binaryList)
    edgeDict = getEdgeDict_BruijnGraph(matrix,colnames)
    
    path = EulerianCycle_string(edgeDict)
    stringPath = stringCompByPath(path)[:-(k-1)]
    print stringPath
    
K_universal(8)


