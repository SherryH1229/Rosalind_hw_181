#----------------extra_functions-----------
def EulerCycle (preNode,edgeDict):
    cycle = []
    cycle.append(preNode)
    keys = edgeDict.keys()
    while True:
        if len(edgeDict[preNode]) > 0:
            suffNode = edgeDict[preNode].pop(0)
            cycle.append(suffNode)
            preNode = suffNode
        else:
            for key in keys:
                if len(edgeDict[key]) == 0:
                    edgeDict.pop(key,None)
           
            return cycle

def check_1_in_1_out(connectDict,node):
    if node not in connectDict:
        return False
        
    numOutEdge = len(connectDict[node])
    numInEdge = 0
    
    for key, value in connectDict.iteritems():
        numInEdge = numInEdge+(value.count(node))
    
    if numInEdge == 1 and numOutEdge == 1:
        return True
    
    return False

def prefix(pattern):
    prefix = pattern[0:-1]
    return prefix

def suffix(pattern):
    suffix = pattern[1:]
    return suffix

def getKmerList(data):
    KmerList = []
    for line in data:
        KmerList.append(''.join(line.splitlines()))
    
    #KmerList = set(KmerList)
    #KmerList = list(KmerList)

    return KmerList

def stringCompByPath(string):
    outputString = []
    outputString.append(string[0])
    for i in range (1,len(string)):
        tempStr = string[i]
        outputString.append(tempStr[-1])
    return (''.join(outputString))
#--------------------3K--------------------
def MaxNonBranchingPaths(connectDict):
    total = []
    k = 0
    pathSets = []
    nodeList = connectDict.keys()
    passedNode = []
    isolatedNode = []
    for node in nodeList:
        if check_1_in_1_out(connectDict,node) == False:        
            if len(connectDict[node]) > 0:
                for path in connectDict[node]:
                    nonBranchingPath = [node,path]  
                    while check_1_in_1_out(connectDict,path) == True:
                        nonBranchingPath.append(''.join(connectDict[path]))
                        passedNode.append(path)
                        path = ''.join(connectDict[path])
                    total.append(nonBranchingPath)                
        else:
            isolatedNode.append(node)
          
    for node in passedNode:
        for isoNode in isolatedNode:
            if node == isoNode:
                isolatedNode.remove(node)
    
    for node in isolatedNode:
        if node in connectDict:
            cycle = EulerCycle(node,connectDict)
           
            total.append(cycle)
    #for item in total:
        #print item
    
    return total
   
    
def build_dict(kmerList):
    connectDict = dict()
    for kmer in kmerList:
        kmer_pre = prefix(kmer)
        kmer_suff = suffix(kmer)
        connectDict[kmer_pre] = connectDict.get(kmer_pre, []) + [kmer_suff]
    
    #print connectDict
    return connectDict
   
def ContigGeneration(data):
    KmerList = getKmerList(data)
    connectDict = build_dict(KmerList)
    #print connectDict
    output = MaxNonBranchingPaths(connectDict)
    finalOut = []
    for out in output:
        string = stringCompByPath(out)
        finalOut.append(string)
    
    finalOut.sort()
    print (' '.join(finalOut))
    
data = open("pattern","r")
ContigGeneration(data)
