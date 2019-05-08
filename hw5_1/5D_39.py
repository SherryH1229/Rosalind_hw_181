def readInfo(data):
    source = ((data.readline()).splitlines())[0]
    sink = ((data.readline()).splitlines())[0]
    edgeDict_withWeight = dict()
    edgeDict = dict()
    for lines in data:
        line  = (lines.splitlines())[0].split("->")
        infos = line[1].split(":")
        if line[0] in edgeDict:
            edgeDict_withWeight[line[0]].append((infos[0],infos[1]))
            edgeDict[line[0]].append(infos[0])

        else:
            edgeDict_withWeight[line[0]] = [(infos[0],infos[1])]
            edgeDict[line[0]] = [infos[0]]
    return edgeDict_withWeight,edgeDict,source,sink

def checkNoIncomeEdge(edgeDict,node,source,checkedNode):
    numInEdge = 0
    for key, value in edgeDict.iteritems():
        if key != source and key not in checkedNode:
            inEdge = [item[0] for item in value].count(node)
            numInEdge = numInEdge+inEdge
    if numInEdge == 0:
        return True
    
    return False

def Predesesor_check(node,source,checkedNode,edgeDict):
    for key, value in edgeDict.iteritems():
        if key not in checkedNode:
            inEdge =  [item[0] for item in edgeDict[key]].count(node[0])
            if inEdge != 0:
                edges = edgeDict[source]
                for edge in edges:
                    if edge[0] == node[0]:
                        edgeDict[source].remove(edge)
                return False
    
    return True

def calculateWeight(edgeDict,path):
    totalWeight = 0
    for i in range (1,len(path)):
        preNode = path[i-1]
        suffNode = path[i]
        for key,value in edgeDict.iteritems():
            if len(value) > 0:
                inEdge = [item[0] for item in edgeDict[key]]
                if key == preNode and suffNode in inEdge:
                    index = inEdge.index(suffNode)
                    weight = int(edgeDict[key][index][1])
                    totalWeight = totalWeight+weight
    return totalWeight

def findTopOrders(edgeDict,source,sink):
    checkedNode = [source]
    oriSource = [item[0] for item in edgeDict[source]]
    #print oriSource
    checkedNode = checkedNode+oriSource
    path = [source]
    indicator = 0
    AllPaths = []
    while len(oriSource):
        sourceNode = oriSource.pop(0)
        if sourceNode not in edgeDict:
            continue
        nextNodes = [item[0] for item in edgeDict[sourceNode]]
        path.append(sourceNode)
        for nextNode in nextNodes:
            #if nextNode not in edgeDict:
                #continue
            if Predesesor_check(nextNode,sourceNode,checkedNode,edgeDict):
                checkedNode.append(nextNode)
                path.append(nextNode)
                sourceNode = nextNode
            else:
                print "???"
                #AllPaths.append(path)
                #print path
                #path = [source]
            
                print sourceNode
                break
        
        #if indicator == 1:
            #break

    #path.append(str(sink))
    #weight = calculateWeight(edgeDict,path)
    print checkedNode
    #print weight
    #print '->'.join(path)

def no_incoming_edges(node):
    return 0
def top_orders(source,sink,edgeDict):
    #topOrder = []
    #edges = edgeDict[source]
    #for edge in edges:
        #topOrder.append((source,edge))
    topOrder = [source]
    oriSource = [item for item in edgeDict[source]]
    #print oriSource
    topOrder = topOrder+oriSource
    #print topOrder
    '''checkedNode = checkedNode+oriSource
    path = [source]
    indicator = 0
    AllPaths = []'''
    while len(oriSource):
        sourceNode = oriSource.pop(0)
        #print edgeDict[sourceNode]
        nextNodes = [item[0] for item in edgeDict[sourceNode]]
        print nextNodes

        #path.append(sourceNode)
        for nextNode in nextNodes:
            if Predesesor_check(nextNode,sourceNode,topOrder,edgeDict):
                topOrder.append(nextNode)
                #path.append(nextNode)
                sourceNode = nextNode
                #print nextNode
        
    
    topOrder.append(sink)
    print topOrder
    return 0

def exe(data):
    edgeDict_withWeight,edgeDict,source,sink = readInfo(data)
    #topOrderPath(edgeDict,source,sink)
    top_orders(source,sink,edgeDict)
    #print edgeDict_withWeight
    #print edgeDict

    #findTopOrders(edgeDict,source,sink)

data = open("pattern","r")
exe(data)


