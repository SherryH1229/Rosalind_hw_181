def readInfo(data):
    info  = map(int,data.readline().replace("(","").replace(")","").split())
    breakPos = map(int,data.readline().split(","))
    
    return info,breakPos

def ChromosomeToCycle(chroms):
    #print chroms
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
    
    nodes = ChromosomeToCycle(chroms)
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
    a = breakPos[0]
    b = breakPos[1]
    c = breakPos[2]
    d = breakPos[3]

    combination = [(a,b),(b,a),(c,d),(d,c)]
    out = []
    for genome in genomeGraph:
        if genome not in combination:
            out.append(genome)
    
    out.append((a,c))
    out.append((b,d))
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
        chromList.append("("+str(' '.join(Chromosome))+")")
    
    return chromList

def twoBreak_onGenome(oriChroms,breakPos):
    GenomeGraph = ColoredEdges(oriChroms)
    twoBreak_genome = twoBreak_onGenomeGraph(GenomeGraph,breakPos)
    print twoBreak_genome
    print(graph_to_genome(twoBreak_genome))
    
def exe(data):
    oriChroms,breakPos = readInfo(data)
    twoBreak_onGenome(oriChroms,breakPos)
    
data = open("pattern","r")
exe(data)