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
#-----------------------3F-----------------
def findStartNode(edgeDict):
    preNodes = edgeDict.keys()
    for preNode in preNodes:
        numOutEdge = len(edgeDict[preNode])
        numInEdge = 0
        for key, value in edgeDict.iteritems(): 
            numInEdge = numInEdge+(value.count(preNode))
        if numOutEdge > numInEdge:
            return preNode

def EulerianPath (dataset):
    path = []
    edgeDict = getEdges(dataset)
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
    
    eulerPath = '->'.join(path[::-1])
    return eulerPath


dataset = open("pattern","r")
print(EulerianPath(dataset))