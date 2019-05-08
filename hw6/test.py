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
    #print chroms
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
def twoBreak_onGenomeGraph(genomeGraph,breakPos):
    #print genomeGraph
    a = breakPos[0]
    b = breakPos[1]
    c = breakPos[2]
    d = breakPos[3]

    combination = [(a,b),(b,a),(c,d),(d,c)]
    #print "combination is"+str(combination)
    #print "genomeGraph" + str(genomeGraph)
    out = []
    for genome in genomeGraph:
        if genome not in combination:
            out.append(genome)
    
    out.append((a,c))
    out.append((b,d))
    #print out
    return out
    
def CycleToChromosome(Nodes):
    Chromosome = [0] * (len(Nodes)/2)
    for j in range (len(Nodes)/2):
        if Nodes[2*j] < Nodes[2*j+1]:
            Chromosome[j] = "+"+str(Nodes[2*j+1]/2)
        else:
            Chromosome[j] = str(-Nodes[2*j]/2)

    return Chromosome

def graph_to_genome(genomes):
    genomeDict = dict(genomes)
    
    cycles = []
    while len(genomeDict) > 0:
        cycle = []
        currValue = genomeDict[genomeDict.keys()[0]]
        cycle.append(genomeDict.keys()[0])
        cycle.append(currValue)
        del genomeDict[genomeDict.keys()[0]]

        while True:
            if currValue%2 == 0:
                nextValue = currValue-1
            else:
                nextValue = currValue+1
        
            if nextValue in cycle:
                break
            for key,value in list(genomeDict.iteritems()):
                if key == nextValue:
                    cycle.append(key)
                    cycle.append(genomeDict[key]) 
                    del genomeDict[key]
                elif value == nextValue:
                    cycle.append(value)
                    cycle.append(key)
                    del genomeDict[key]

            currValue = cycle[-1]
    
        cycles.append(cycle)
    
    chromList = []
    for cycle in cycles:
        index = cycle.pop(len(cycle)-1)
        cycle.insert(0,index)
        Chromosome = CycleToChromosome(cycle)
        #print Chromosome
        chromList.append(map(int,Chromosome))
    
    return chromList

def twoBreak_onGenome(oriChroms,breakPos):
    GenomeGraph = ColoredEdges(oriChroms)
    #print GenomeGraph
    twoBreak_genome = twoBreak_onGenomeGraph(GenomeGraph,breakPos)
    return graph_to_genome(twoBreak_genome)
    

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
#-----------------------6D-------------------------
def colored_Edge_cycles(BreakpointGraph):
    cycles = []
    while True:
        cycle = Eulerian(BreakpointGraph)
        if cycle == "Break":
            break
        cycles.append(cycle)

    return cycles
def check_Nontrivial(cycle):
    item = [cycle[0],cycle[1]]
    for c in cycle:
        if c not in item:
            return True
    
    return False

def shortest_Rearrangement_Scenaria(P,Q):
    RedEdges = ColoredEdges(P)
    BlueEdges = ColoredEdges(Q)
    path = []
    path.append(P)
   
    while two_Breaks_dist(ColoredEdges(P),ColoredEdges(Q),P,Q) > 0:
      
        BreakpointGraph = build_EdgeDict(ColoredEdges(P),ColoredEdges(Q))
        cycles = colored_Edge_cycles(BreakpointGraph)

        for cycle in cycles:
           
            if check_Nontrivial(cycle) == True:
                
                aval_edges = [edge for edge in ColoredEdges(Q) if edge[0] in cycle]
                (i1,j1) = random.choice(aval_edges)
                edgesRed = ColoredEdges(P)
                
                for edge in edgesRed:
                    if edge[0] == i1: 
                        i2 = edge[1]
                    elif edge[1] == i1:
                        i2 = edge[0]   
                    elif edge[0] == j1:   
                        j2 = edge[1]
                    elif edge[1] == j1:   
                        j2 = edge[0]
                
                breakPos = [i1,i2,j1,j2]
                P = twoBreak_onGenome(P,breakPos)
                path.append(P)
                
                break

    return path

def printPath(path):
    for p in path:
        string = []
        for p1 in p:
            sub_string = []
            for p11 in p1:
                if p11 > 0:
                    sub_string.append("+"+str(p11))
                else:
                    sub_string.append(str(p11))
            string.append("("+' '.join(sub_string)+")")
        print (''.join(string))


def exe(data):
    chr1,chr2 = readInfo(data)
    path = shortest_Rearrangement_Scenaria(chr1,chr2)
    printPath(path)
    #colorEdge1 = ColoredEdges(chr1)
    #colorEdge2 = ColoredEdges(chr2)
    #count = two_Breaks_dist(colorEdge1,colorEdge2,chr1,chr2)

    #print count
  
    
  
data = open("pattern","r")
exe(data)