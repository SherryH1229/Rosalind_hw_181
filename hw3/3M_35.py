#----------------extra_functions-----------
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

#--------------------3M--------------------
def check_1_in_1_out(connectDict,node):
    if node not in connectDict:
        return False
    numOutEdge = len(edgeDict[node])
    numInEdge = 0
    
    for key, value in edgeDict.iteritems():
        numInEdge = numInEdge+(value.count(node))
    
    if numInEdge == 1 and numOutEdge == 1:
        return True
    
    return False

def MaxNonBranchingPaths(connectDict):
    total = []
    k = 0
    pathSets = []
    nodeList = connectDict.keys()
    passedNode = []
    isolatedNode = []
    for node in nodeList:
        if check_1_in_1_out(connectDict,node) == False:        
            if len(connectDict[node]) > 0:
                for path in connectDict[node]:
                    nonBranchingPath = [node,path]  
                    while check_1_in_1_out(connectDict,path) == True:
                        nonBranchingPath.append(''.join(edgeDict[path]))
                        passedNode.append(path)
                        path = ''.join(connectDict[path])
                    total.append(' -> '.join(nonBranchingPath))                  
        else:
            isolatedNode.append(node)
          
    for node in passedNode:
        for isoNode in isolatedNode:
            if node == isoNode:
                isolatedNode.remove(node)
    
    for node in isolatedNode:
        if node in connectDict:
            cycle = EulerCycle(node,connectDict)
           
            total.append(' -> '.join(cycle))
    for item in total:
        print item
   
data = open("pattern","r")
edgeDict = getEdges(data)
MaxNonBranchingPaths(edgeDict)
