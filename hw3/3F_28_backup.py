#-------------extra_functions----------
import random
#-------------3F-------------------
def buildMatrix (dataset):
    numOutEdge = dict()
    edgeDict = dict()
    
    for lines in dataset:
        input = lines.split()  
        preNode = input[0]
        suffs = input[2]
        suffNode = []
        suffs = input[2].split(",")
        k = 0
        for suff in suffs:
            k = k+1
            suffNode.append(suff)
        
        numOutEdge[preNode] = k
        edgeDict[preNode] = suffNode
    nodes = sorted(edgeDict.keys())
    Matrix = [[0 for x in range(len(nodes))] for y in range(len(nodes))] 
    
    for i in range (len(nodes)):
        suffNodes =  edgeDict[nodes[i]]
        for suffNode in suffNodes:
            Matrix[i][int(suffNode)] = Matrix[i][int(suffNode)]+1
    
    return Matrix,numOutEdge


def EulerianCycleByMatrix (dataset):
    path = []
    pathset = []
    Matrix,numOutEdge = buildMatrix(dataset)
    
    numoutEdgeCountCP = numOutEdge.values()
    iniRowNum = 0
    path.append(str(iniRowNum))

    numOutEdge[str(iniRowNum)] = numOutEdge[str(iniRowNum)]-1
    preNode = next((i for i, x in enumerate(Matrix[iniRowNum]) if x), None)
    path.append(str(preNode))
    
    while True:
        if numOutEdge[str(preNode)] > 0:
            tempRow = Matrix[preNode]
            suffNodes = [i for i, e in enumerate(tempRow) if e != 0]
            for suff in suffNodes:
                if numOutEdge[str(suff)] > 0:
                    suffNode = suff
                    break            
                suffNode = suff
            numOutEdge[str(preNode)] = numOutEdge[str(preNode)]-1
            path.append (str(suffNode))
            preNode = suffNode
            
        
        else:
            if (all(value == 0 for value in numOutEdge.values())) == True:
                path = '->'.join(path)
                print path
                return path
            for node, count in numOutEdge.iteritems():
                choiseList = []
                if count != 0:
                    choiseList.append(int(node))
            firstNode = random.choice(choiseList)
            
            for i, v in enumerate(numOutEdge):
                numOutEdge[v] = numoutEdgeCountCP[i]  
            
            numOutEdge[str(firstNode)] = numOutEdge[str(firstNode)]-1
            preNode = next((i for i, x in enumerate(Matrix[firstNode]) if x), None)
            #possPreNode = [i for i, e in enumerate(tempRow) if e != 0]

            path = []
            path.append(str(firstNode))
            path.append(str(preNode))
    
dataset = open("pattern","r")
EulerianCycleByMatrix(dataset)


#print (all(v == 0 for v in myList))


#[mydict[x] for x in mykeys]