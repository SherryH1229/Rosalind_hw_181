#----------------Extra packages------------
import random

def readInfo(data):
    edgeDict = dict()
    for lines in data:
        line  = (lines.splitlines())[0].split(" -> ")
        infos = line[1].split(":")
        source = line[0]
        sink = line[1].split(",")
        if source in edgeDict:    
            edgeDict[source].append(sink)
        else:
            edgeDict[source] = sink
    return edgeDict

def has_no_incoming_Edges(node,Graph):
    edges = []
    for key, value in Graph.iteritems():
        edges = edges+value

    if node in edges:
        return False
    else: 
        return True

def toplogicalOrdering(Graph):
    listNode = []
    inedges = []
    Candidates = []
    for key,value in Graph.iteritems():
        inedges = inedges+value
    
   
    for key,value in Graph.iteritems():
        if key not in inedges:
            Candidates.append(key)
    
    while len(Candidates) != 0:

        arbi_node = random.choice(Candidates)
        listNode.append(arbi_node)
        Candidates.remove(arbi_node)
        if arbi_node not in Graph:
            continue

        outGoingEdges = list(Graph[arbi_node])
       
        for outGoingEdge in  outGoingEdges:
            Graph[arbi_node].remove(outGoingEdge)
            if has_no_incoming_Edges(outGoingEdge,Graph):
                Candidates.append(outGoingEdge)

    return ', '.join(listNode)

def exe(data):
    edgedict = readInfo(data)
    print (toplogicalOrdering(edgedict))

data = open("pattern","r")
exe(data)