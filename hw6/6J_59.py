def readInfo(data):
    info  = map(int,data.readline().replace("(","").replace(")","").replace(",","").split())
    breakPos = map(int,data.readline().split(","))
    #print breakPos
    return info,breakPos

'''def twoBreak_onGenomeGraph(genomeGraph,breakPos):
    a = breakPos[0]
    b = breakPos[1]
    c = breakPos[2]
    d = breakPos[3]

    breakList = [a,b,c,d]
    
    out = []
    i = 0
    indicator = 0
    while (i< len(genomeGraph)-1):
        if genomeGraph[i] == a:
            if a in breakList:
                out.append((a,c))
                breakList.remove(a)
                breakList.remove(c)
            else:
                if genomeGraph[i+1] == b:
                    out.append((d,b))
                elif genomeGraph[i+1] == d:
                    out.append((b,d))
                breakList.remove(b)
                breakList.remove(d)
        
        elif genomeGraph[i] == b:
            if b in breakList:
                out.append((b,d))
                breakList.remove(b)
                breakList.remove(d)
            else:
                if genomeGraph[i+1] == a:
                    out.append((c,a))                 
                elif genomeGraph[i+1] == c:
                    out.append((a,c))
                    
                breakList.remove(a)
                breakList.remove(c)
        
        elif genomeGraph[i] == c:
            if c in breakList:
                out.append((c,a))
                breakList.remove(c)
                breakList.remove(a)
            else:
                if genomeGraph[i+1] == b:
                    out.append((d,b))                 
                elif genomeGraph[i+1] == d:
                    out.append((b,d))
                    
                breakList.remove(b)
                breakList.remove(d)
        
        elif genomeGraph[i] == d:
            if d in breakList:
                out.append((d,b))
                breakList.remove(b)
                breakList.remove(d)
            else:
                if genomeGraph[i+1] == a:
                    out.append((c,a))                 
                elif genomeGraph[i+1] == c:
                    out.append((a,c))
                    
                breakList.remove(a)
                breakList.remove(c)
        
        else:
            out.append((genomeGraph[i],genomeGraph[i+1]))
        

        i = i+2
    print out'''
    
def twoBreak_onGenomeGraph(genomeGraph,breakPos):
    a = breakPos[0]
    b = breakPos[1]
    c = breakPos[2]
    d = breakPos[3]

    combination = [(a,b),(b,a),(c,d),(d,c)]
    out = []
    i = 0
    while (i< len(genomeGraph)-1):
        if (genomeGraph[i],genomeGraph[i+1]) not in combination:
            out.append((genomeGraph[i],genomeGraph[i+1]))
        i = i+2
    out.append((a,c))
    out.append((b,d))
    print out

def exe(data):
    genomeGraph,breakPos = readInfo(data)
    twoBreak_onGenomeGraph(genomeGraph,breakPos)
    #print(GraphToGenome(oriChroms))
    
data = open("pattern","r")
exe(data)