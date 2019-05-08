def readInfo(data):
    info  = map(int,((data.read())[1:-1]).split())
    return info

def CycleToChromosome(Nodes):
    Chromosome = [0] * (len(Nodes)/2)
    for j in range (len(Nodes)/2):
        if Nodes[2*j] < Nodes[2*j+1]:
            Chromosome[j] = "+"+str(Nodes[2*j+1]/2)
        else:
            Chromosome[j] = str(-Nodes[2*j]/2)
    
    return Chromosome

def exe(data):
    oriList = readInfo(data)
    #print oriList
    #print(CycleToChromosome(oriList))
    CycleToChromosome(oriList)

data = open("pattern","r")
exe(data)