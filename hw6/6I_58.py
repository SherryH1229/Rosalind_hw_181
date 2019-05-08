def readInfo(data):
    info  = map(int,data.read().replace("(","").replace(")","").replace(",","").split())
    return info

def CycleToChromosome(Nodes):
    Chromosome = [0] * (len(Nodes)/2)
    for j in range (len(Nodes)/2):
        if Nodes[2*j] < Nodes[2*j+1]:
            Chromosome[j] = "+"+str(Nodes[2*j+1]/2)
        else:
            Chromosome[j] = str(-Nodes[2*j]/2)

    return Chromosome

def GraphToGenome(edges):
    chroms = []
    chrom = []
    i = 0

    while (i < (len(edges)-1)):
        chrom.append(edges[i])
        chrom.append(edges[i+1])
        if edges[i+1] < edges[i]:
            num = chrom.pop(len(chrom)-1)
            chrom.insert(0,num)
            chroms.append(chrom)
            chrom = []
        i +=2
    
    chromList = []
    for chrom in chroms:
        Chromosome = CycleToChromosome(chrom)
        chromList.append("("+str(' '.join(Chromosome))+")")
    
    return ''.join(chromList)

def exe(data):
    oriChroms = readInfo(data)
    print oriChroms
    #print(GraphToGenome(oriChroms))
    
data = open("pattern","r")
exe(data)