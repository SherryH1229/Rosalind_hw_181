#--------------------extra functions----------------
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
#--------------------6G---------------------------
def readInfo(data):
    info  = str((data.read())[1:-1]).split(")(")
    chroms = []
    for chrom in info:
        chroms.append(map(int,chrom.split()))
    
    #print chroms
    return chroms

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
            edgeList.append("("+str(edge[i])+", "+str(edge[i+1])+")")
            i = i+2
        i = 0
    
    return ', '.join(edgeList)
    
def exe(data):
    oriChroms = readInfo(data)
    print(ColoredEdges(oriChroms))

data = open("pattern","r")
exe(data)