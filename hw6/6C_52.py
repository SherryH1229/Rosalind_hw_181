#----------------Extra packages------------
import random

def readInfo(data):
    info  = str((data.readline())[1:-2]).split(")(")
    info2 = str((data.readline())[1:-1]).split(")(")
    #info2 = data.read()
    chroms1 = []
    chroms2 = []
    for chrom1 in info:
        #print chrom1.split()
        chroms1.append(map(int,chrom1.split()))
    
    for chrom2 in info2:
        chroms2.append(map(int,chrom2.split()))
    
    return chroms1,chroms2

def Eulerian (edgeDict):
    path = []

    if len(edgeDict) == 0:
        return "Break"

    startNode = random.choice(edgeDict.keys())
    avalNode = [startNode]
    while len(avalNode) != 0:
        node = avalNode[-1]
        if node not in edgeDict:
            path.append(avalNode.pop())
            continue

        if len(edgeDict[node]) != 0:
            nextNode = random.choice(edgeDict[node])
    
            avalNode.append(nextNode)
            edgeDict[node].remove(nextNode)
            if len(edgeDict[node]) == 0:
                edgeDict.pop(node,None)
          
        else:
            path.append(avalNode.pop())
    
    return path[::-1]

def ChromosomeToCycle(chroms):
    Node = [0] * (len(chroms)*2+1)
    for j in range (len(chroms)):
        i = chroms[j]
        if i > 0:
            Node[2*(j+1)-1] = 2*i-1
            Node[2*(j+1)] = 2*i
        else:
            Node[2*(j+1)-1] = -2*i
            Node[2*(j+1)] = -2*i-1
    
    return Node[1:]

def ColoredEdges(chroms):
    Edges = []
    num = 1
    for chrom in chroms:
        nodes = ChromosomeToCycle(chrom)
        firstNum = nodes.pop(0)
        nodes.append(firstNum)
        Edges.append(nodes)
    
    i = 0
    edgeList = []
    for edge in Edges:
        while i < len(edge):
            edgeList.append((edge[i],edge[i+1]))
            i = i+2
        i = 0
    
    return edgeList

def build_EdgeDict(colorEdge1,colorEdge2):
    edgeDict = dict()
    
    for edge in colorEdge1:
        if edge[0] in edgeDict:
            edgeDict[edge[0]].append(edge[1])
        else:
            edgeDict[edge[0]] = [edge[1]]
        
        if edge[1] in edgeDict:
            edgeDict[edge[1]].append(edge[0])
        else:
            edgeDict[edge[1]] = [edge[0]]
    
    for edge2 in colorEdge2:
        if edge2[0] in edgeDict:
            edgeDict[edge2[0]].append(edge2[1])
        else:
            edgeDict[edge2[0]] = [edge2[1]]
        
        if edge2[1] in edgeDict:
            edgeDict[edge2[1]].append(edge2[0])
        else:
            edgeDict[edge2[1]] = [edge2[0]]
   
    return edgeDict

def two_Breaks_dist(colorEdge1,colorEdge2,chr1,chr2):
    edges = build_EdgeDict(colorEdge1,colorEdge2)
    count = 0
    i = 0
    while True:
        test = Eulerian(edges)
        if test == "Break":
            break
        count+=1
    
    length = 0
    for chr in chr1:
        length = length+len(chr)

    return length-count
    
def exe(data):
    chr1,chr2 = readInfo(data)
    colorEdge1 = ColoredEdges(chr1)
    colorEdge2 = ColoredEdges(chr2)
    count = two_Breaks_dist(colorEdge1,colorEdge2,chr1,chr2)

    print count
  
    
  
data = open("pattern","r")
exe(data)