def readInfo(data):
    source = ((data.readline()).splitlines())[0]
    sink = ((data.readline()).splitlines())[0]
    edgeDict_withWeight = dict()
    edgeDict = dict()
    for lines in data:
        line  = (lines.splitlines())[0].split("->")
        infos = line[1].split(":")
        if line[0] not in edgeDict_withWeight:
            edgeDict_withWeight[line[0]] = {infos[0]:int(infos[1])}
        else:
            edgeDict_withWeight.get(line[0])[infos[0]] = int(infos[1])
        
        if line[0] in edgeDict:
            #edgeDict_withWeight[line[0]].append((infos[0],infos[1]))
            edgeDict[line[0]].append(infos[0])
            
        else:
            #edgeDict_withWeight[line[0]] = [(infos[0],infos[1])]
            edgeDict[line[0]] = [infos[0]]

    #print edgeDict_withWeight.get("1")
    #print edgeDict_withWeight
    return edgeDict_withWeight,edgeDict,source,sink

def check_predecessors(node,edgeDict,checkedNode):
    for key,value in edgeDict.iteritems():
        if node in value:
            if key not in checkedNode:
                return False
    
    return True

def top_orders(source,sink,edgeDict):
    ordered = [source]+edgeDict[source]
    #print ordered
    

    
    #check_predecessors("2",edgeDict,checkedNode)
    '''while (len(ori_from_source) > 0):
        node = ori_from_source.pop()
        if node not in edgeDict:
            continue
        nextNodes = edgeDict[node]
        #print nextNodes
        inNode = []
        for nextNode in nextNodes: 
            if check_predecessors(node,edgeDict,checkedNode):
                print "??????"
                if nextNode == sink:
                    for key,value in edgeDict.iteritems():
                        if nextNode in value:
                            inNode.append(key)
                    sinkNode = sink   
                else:       
                    print "???"
                    print nextNode     
                    checkedNode.append(nextNode)
                    inNode.append(nextNode)
                    sinkNode = node
                    #topOrder.append((node,edgeDict[node]))
                for key,value in edgeDict.iteritems():
                    if nextNode in value:
                        inNode.append(key)
                sinkNode = nextNode
                checkedNode.append(nextNode)

                topOrder.append((sinkNode,inNode))
            else:
                print edgeDict[node]
    #print checkedNode
    print topOrder
    #topOrder[sinkNode] = inNode'''
    return 0

       
def calculate_weight(source,topOrder,edgeDict_withWeight,edgeDict):
    weight = []
    record = dict()
    #print topOrder
    for tup in topOrder:
        if tup[1][0] == source and len(tup[1]) == 1:
            #print tup
            record[tup[0]] = edgeDict_withWeight[tup[1][0]][tup[0]]
        else:
            preds = tup[1]
            #print preds
            maxValue = 0
            for pred in preds:
                if edgeDict_withWeight[pred][tup[0]]+record[pred]>maxValue:
                    maxValue = edgeDict_withWeight[pred][tup[0]]+record[pred]
            record[tup[0]] = maxValue
       
    #print record
    return 0  

def test(edgeDict,source):
    print edgeDict
    sorted = []
    sorted.append((source,edgeDict[source]))
    edgeDict.pop(source,None)
    #print edgeDict
    for node,edges in list(edgeDict.items()):
        for edge in edges:
            if edge in edgeDict:
                break
            else:
                del edgeDict[node]
                sorted.append((node,edges))

    #    print node
    #    print edges
    #sorted = []
   # sorted_graph[]
    #sorted.append((source,edgeDict[source]))
    print sorted
    return 0
    
def exe(data):
    edgeDict_withWeight,edgeDict,source,sink = readInfo(data)
    topOrder = top_orders(source,sink,edgeDict)
    #test(edgeDict,source)
    #calculate_weight(source,topOrder,edgeDict_withWeight,edgeDict)
    #print topOrder

data = open("pattern","r")
exe(data)
   