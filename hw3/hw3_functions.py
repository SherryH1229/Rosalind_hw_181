#-------------extra_functions----------
import random
#-------------3A-------------------
def kmerComp(k,string):
    kmerList = []
    for i in range (len(string)-k+1):
        kmerList.append(string[i:i+k])
    
    kmerList.sort()
    #print(kmerList) 

    for m in kmerList:
        print (m)
#kmerComp(5,"CAATCCAAC")

#-------------3B-------------------
patterns = open("pattern","r")
patternString = []
for line in patterns:
    patternString.append(line.splitlines())

def stringCompByPath(string):
    outputString = string[0]
    for i in range (1,len(string)):
        tempStr = (string[i])[0]
        outputString.append(tempStr[-1])
    print (''.join(outputString))
    
#stringCompByPath(patternString)

#-------------3C-------------------
patterns = open("pattern","r")
patternList = []
for line in patterns:
    patternList.append(line.splitlines())

def prefix(pattern):
    prefix = pattern[0:-1]
    return prefix

def suffix(pattern):
    suffix = pattern[1:]
    return suffix

def overlapGraph (kmerList):
    kmerList.sort()
    graph = []
    for i in range (len(kmerList)):
        tempPattern = ''.join(kmerList.pop(i))
        for pattern in kmerList:
            collection = []
            patternJ = ''.join(pattern)
            if suffix(''.join(tempPattern)) == prefix(patternJ):
                collection.append(''.join(tempPattern) + " -> " + ''.join(pattern))
            graph.append(collection)
        kmerList.insert(i,tempPattern)
        graph =  filter(None, graph)
    
    for s in graph:
        print ''.join(s)

#overlapGraph(patternList)

#-------------3D-------------------
def buildDebruijnMatrix(KmerList):
    #remove duplicates
    KmerList = set(KmerList)
    KmerList  = list(KmerList)
    KmerList.sort()
    
    length = len(KmerList)
    Matrix = [[0 for x in range(length)] for y in range(length)] 

    return (KmerList,Matrix)
    
def DeBruijnGraph (num,string):
    nameList = kmerComp(num-1,string)
    colnames, DebruijnMatrix = buildDebruijnMatrix(nameList)
    KmerList = kmerComp(num,string)
    for kmer in KmerList:
        preNode = prefix(kmer)
        sufNode = suffix(kmer)
        i = colnames.index(preNode)
        j = colnames.index(sufNode)

        DebruijnMatrix[i][j] = DebruijnMatrix[i][j]+1

    return DebruijnMatrix, colnames

def printDeBruijnGraph(DebruijnMatrix,colnames):
    i = 0
    for row in DebruijnMatrix:
        output = (colnames[i]+" ->").split()
        j = [k for k, e in enumerate(row) if e != 0]
        suff = []
        if len(j) != 0:
            for index in j:
                for k in range (row[index]):
                    suff.append(colnames[index])
            suff = (','.join(suff)).split()   
            outString = output+suff
            print (' '.join(outString))
        i = i+1
#matrix,colnames = DeBruijnGraph(12,"")
#printDeBruijnGraph(matrix,colnames)

#----------------3F-----------------------
def getEdges (dataset):
    edgeDict = dict()
    
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

def EulerianCycleByMatrix (dataset):
    edgeDict = getEdges(dataset)
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
    
    path = '->'.join(eulerCycle)
    return path

    
#dataset = open("pattern","r")
#print (EulerianCycleByMatrix(dataset))

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
            #suff = (','.join(suff)).split()   
            #outString = output+suff
            #print outString


            #print (' '.join(outString))
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