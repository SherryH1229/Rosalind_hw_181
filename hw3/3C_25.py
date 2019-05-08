#-------------extra_functions----------
patterns = open("pattern","r")
patternString = []
for line in patterns:
    patternString.append(line.splitlines())
    print (patternString,"patternString")

def stringCompByPath(string):
    outputString = string[0]
    for i in range (1,len(string)):
        tempStr = (string[i])[0]
        outputString.append(tempStr[-1])
    return (''.join(outputString))
#-------------3C-------------------
patterns = open("pattern","r")
patternList = []
for line in patterns:
    patternList.append(line.splitlines())

def prefix(pattern):
    prefix = pattern[0:-1]
    return prefix

def suffix(pattern):
    suffix = pattern[1:]
    return suffix

def overlapGraph (kmerList):
    kmerList.sort()
    graph = []
    for i in range (len(kmerList)):
        tempPattern = ''.join(kmerList.pop(i))
        for pattern in kmerList:
            collection = []
            patternJ = ''.join(pattern)
            if suffix(''.join(tempPattern)) == prefix(patternJ):
                collection.append(''.join(tempPattern) + " -> " + ''.join(pattern))
            graph.append(collection)
        kmerList.insert(i,tempPattern)
        graph =  filter(None, graph)
    
    for s in graph:
        print ''.join(s)

overlapGraph(patternList)