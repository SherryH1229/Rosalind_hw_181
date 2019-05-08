#----------------Extra packages------------
import random

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

    
dataset = open("pattern","r")
print (EulerianCycleByMatrix(dataset))