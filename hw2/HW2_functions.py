#---------------packages----------
from random import *
#---------------extra functions----------
def getInfo(DnasFileName):
    Dnas = open('Dna','r')
    count = 0
    length = 0
    for line in Dnas:
        count = count+1
        length =  len(line)
    
    Dnas.close()
    return (count,length)
def buildDnasMatrix(DnasFileName,numDna,length):
    w, h = length, numDna
    Matrix = [[0 for x in range(w)] for y in range(h)] 
    
    Dnas = open('Dna','r')
    i = 0
    count = 0
    while (True):   
        character = Dnas.read(1)
        if not character:
            break
        else: 
            if (character != "\n"):
                
                Matrix[i][count] = character
                count = count+1
            else:
                count = 0  
                i = i+1  
            
        if (i == h):
            break
    
    return Matrix

def hammingDist(str1,str2):
    if (len(str1)!=len(str2)):
        print("the lengths of two strings are not the same!")
        return 0
    dist = 0
    for i in range (0,len(str1)):
        if (str1[i]!=str2[i]):
            dist = dist + 1
    return dist

def suffix(pattern):
    suffix = pattern[1:]
    return suffix
def firstSymbol(pattern):
    firstSymbol = pattern[0]
    return firstSymbol
def neighbors(pattern,d):
    nucleotide = "ACGT"
    if d == 0:
        return pattern
    
    if len(pattern)==1:
        return ["A","C","G","T"]
    
    neighborhood = []
    suffixNeighbors = neighbors(suffix(pattern),d)
    for string in suffixNeighbors:
        if (hammingDist(suffix(pattern),string) < d):
            for char in nucleotide:
                neighborString = char+string
                neighborhood.append(neighborString)    
        else:
            neighborString = firstSymbol(pattern)+string
            neighborhood.append(neighborString)
    return neighborhood

def apxPatternMatch(pattern,string,d):
    posList = []
    for i in range (0,len(string)-len(pattern)+1):
        substring = string[i:(i+len(pattern))]
        distance = hammingDist(substring,pattern)
        if (distance<=d):
            return True
    
    return False
#----------------2A----------------------
matrixInfo = getInfo("Dna")
dnaMatrix = buildDnasMatrix("Dna",matrixInfo[0],matrixInfo[1])

def checkExistance(dnaMatrix,pattern,d):
    #print(pattern)
    for i in range (0,len(dnaMatrix)):
        string = ''.join(dnaMatrix[i])
        if (apxPatternMatch(pattern,string,d)):
           
            continue
        else:
            return False
    
    return True
def motifEnumeration (Dna,k,d):
    patterns = []
    for i in range (0,len(Dna[0])-k+1):
        kmer =''.join(Dna[0][i:i+k])
        neighborhood = neighbors(kmer,d)
        if isinstance(neighborhood, str):
            if (checkExistance(Dna,neighborhood,d)):
                patterns.append(neighborhood)
        else:
            for pattern in neighborhood:
                if (checkExistance(Dna,pattern,d)):
                    patterns.append(pattern)
        
    patternString = ' '.join(list(set(patterns)))
    
    return (patternString)
            
#print (motifEnumeration(dnaMatrix,5,2))

#---------------2B------------------------
matrixInfo = getInfo("Dna")
dnaMatrix = buildDnasMatrix("Dna",matrixInfo[0],matrixInfo[1])
def medianString(Dna,k):
    distance = float("inf")
    median = []
    for i in range (0,4**k):
        pattern = numberToPattern(i,k)
        
        distInDnaString = distanceBetweenPatternAndString(pattern,Dna)
        if distance > distInDnaString:
            distance = distInDnaString
            median = pattern
    
    return (median)

#print (medianString(dnaMatrix,6))

#---------------2C------------------------
def getProfileInfo(profileFileName):
    Dnas = open(profileFileName,'r')
    count = 0
    length = 0
    lineSplit = []
    for line in Dnas:
        count = count+1
        length = len(line.split())
    Dnas.close()
    return (count,length)
def buildProfileMatrix(profileFileName,numDna,length):
    w, h = length, numDna
    Matrix = [[0 for x in range(w)] for y in range(h)] 
    
    Dnas = open(profileFileName,'r')
    i = 0
    count = 0
    while (True):   
        line = Dnas.readline()
        line = line.split()
        numberString = []
        for element in line:
            element = float(element)
            numberString.append(element)

        for j in range (0,len(numberString)):
            Matrix[i][j] = numberString[j]
        
        i = i+1

        if not line:
            break
     
        if (i == (w-1)):
            break

    Dnas.close()

    return Matrix

matrixInfo = getProfileInfo("profile")
profileMatrix = buildProfileMatrix("profile",matrixInfo[0],matrixInfo[1])

def symbolToPattern(symbol):
    if symbol == 'A':
        value = 0 
    elif symbol == 'C':
        value = 1
    elif symbol == 'G':
        value = 2
    else:
        value = 3
    
    return value
    
def mostProbableKmer(text,k,profileMatrix):
    maxProb = 0
    probableKmer = []
    #print ("profileMatrix",profileMatrix)
    for i in range (0,len(text)-k+1):
        patternInDna = text[i:i+k]
        #print(patternInDna)
        patternProb = float("inf")
        for j in range (0,k):
            x = symbolToPattern(patternInDna[j])
            y = j
            prob = profileMatrix[x][y]
            if patternProb == float("inf"):
                patternProb = prob
            else:
                patternProb = patternProb*prob
            #print (patternProb)
        if patternProb > maxProb:
            maxProb = patternProb
            probableKmer = patternInDna

        #print("probable",probableKmer)
    return probableKmer

#---------------2D------------------------
matrixInfo = getInfo("Dna")
dnaMatrix = buildDnasMatrix("Dna",matrixInfo[0],matrixInfo[1])

#matrixPInfo = getProfileInfo("profile")
#profileMatrix = buildProfileMatrix("profile",matrixPInfo[0],matrixPInfo[1])

def formProfile(dnaMatrix,numNue,length,numOfDna):
    w, h = length, numNue
    profileMatrix = [[0 for x in range(w)] for y in range(h)]
    #print ("dataMatrix",dnaMatrix)
    for i in range (0,length):
        col = [row[i] for row in dnaMatrix]
        for j in range (0,4):
            num = float(col.count(numberToSymbol(j)))
            profileMatrix[j][i] = num/numOfDna

    return profileMatrix

def score(motifs,k,t):
    profile = formProfile(motifs,4,k,t)
    consensusString = consensus(profile,k)
    score = 0
    for i in range (0,t):
        string = ''.join(motifs[i])
        dist = hammingDist(consensusString,string)
        score = score+dist
    return score

def consensus(profile,length):
    consensusString = []
    for i in range (0,length):
        col = [row[i] for row in profile]
        max_value = max(col)
        max_index = col.index(max_value)
        char = numberToSymbol(max_index)
        consensusString.append(char) 

    return (''.join(consensusString))

def greedyMotifSearch(DnaMatrix,k,t):
    BestMotifs  = [row[0:k] for row in dnaMatrix]
    tempMotifs = []
    for i in range (0,matrixInfo[1]-k+1):
        motif1  = (DnaMatrix[0][i:i+k])
        tempMotifs.append(motif1)
        
        for j in range (1,t):
            tempProfile = formProfile(tempMotifs,4,k,j)
            text = ''.join(DnaMatrix[j])
            tempMotif = mostProbableKmer(text,k,tempProfile)
            if len(tempMotif) == 0:
                tempMotif = text[0:k]
            #print ("temp",tempMotifs)
            tempMotifs.append(list(tempMotif))
        
        if (score(tempMotifs,k,t)) < (score(BestMotifs,k,t)):
            BestMotifs = tempMotifs

        tempMotifs = []

    for m in range (0,t):
        row = ''.join(BestMotifs[m])
        print (row)
    return BestMotifs

#result = greedyMotifSearch(dnaMatrix,12,25)
#---------------2E------------------------
matrixInfo = getInfo("Dna")
dnaMatrix = buildDnasMatrix("Dna",matrixInfo[0],matrixInfo[1])

def formProfileWP(dnaMatrix,numNue,length,numOfDna):
    w, h = length, numNue
    profileMatrix = [[0 for x in range(w)] for y in range(h)]
    #print ("dataMatrix",dnaMatrix)
    for i in range (0,length):
        col = [row[i] for row in dnaMatrix]
        for j in range (0,4):
            num = float(col.count(numberToSymbol(j)))+1
            profileMatrix[j][i] = num/numOfDna

    return profileMatrix

def score(motifs,k,t):
    profile = formProfile(motifs,4,k,t)
    consensusString = consensus(profile,k)
    score = 0
    for i in range (0,t):
        string = ''.join(motifs[i])
        dist = hammingDist(consensusString,string)
        score = score+dist
    return score

def consensus(profile,length):
    consensusString = []
    for i in range (0,length):
        col = [row[i] for row in profile]
        max_value = max(col)
        max_index = col.index(max_value)
        char = numberToSymbol(max_index)
        consensusString.append(char) 

    return (''.join(consensusString))

def greedyMotifSearch(DnaMatrix,k,t):
    BestMotifs  = [row[0:k] for row in dnaMatrix]
    tempMotifs = []
    for i in range (0,matrixInfo[1]-k+1):
        motif1  = (DnaMatrix[0][i:i+k])
        tempMotifs.append(motif1)
        
        for j in range (1,t):
            tempProfile = formProfile(tempMotifs,4,k,j)
            text = ''.join(DnaMatrix[j])
            tempMotif = mostProbableKmer(text,k,tempProfile)
            if len(tempMotif) == 0:
                tempMotif = text[0:k]

            #print ("temp",tempMotifs)
            tempMotifs.append(list(tempMotif))
        
        if (score(tempMotifs,k,t)) < (score(BestMotifs,k,t)):
            BestMotifs = tempMotifs

        tempMotifs = []

    for m in range (0,t):
        row = ''.join(BestMotifs[m])
        print (row)
    return BestMotifs

#result = greedyMotifSearch(dnaMatrix,5,8)

#---------------2F------------------------
matrixInfo = getInfo("Dna")
dnaMatrix = buildDnasMatrix("Dna",matrixInfo[0],matrixInfo[1])

def biasedRandomIndex (probList):
    sumProb = sum(map(float,probList))
    newProbList = [x / sumProb for x in probList]
    #print ("largst",newProbList.index(max(newProbList)))
    randomRoll = random()
    summation = 0
    index = 0
    for prob in newProbList:
        summation = summation + prob
        if randomRoll < summation:
            #print (index)
            return index
        index = index+1

def getAddbackKmer(dnaString,profile,k):
    possibleMotifs = []
    possibleMotifsProb = []
    for i in range (0,len(dnaString)-k+1):
        patternInDna = dnaString[i:i+k]
        patternProb = float("inf")
        for j in range (0,k):
            x = symbolToPattern(patternInDna[j])
            y = j
            prob = profile[x][y]
            if patternProb == float("inf"):
                patternProb = prob
            else:
                patternProb = patternProb*prob
        possibleMotifs.append(patternInDna)
        possibleMotifsProb.append(patternProb)

    addBackKmerIndex = biasedRandomIndex(possibleMotifsProb)
    addBackKmer = possibleMotifs[addBackKmerIndex]
    return list(addBackKmer)

def randomRemoveNformNewMotifs(motifs,dnaMatrix,k,t):
    removeLine = randint(0,t-1)
    text = motifs.pop(removeLine)
    removedDnaString = ''.join(dnaMatrix[removeLine])
    profile = formProfileWP(motifs,4,k,t)
    addBackKmer = getAddbackKmer(removedDnaString,profile,k)
    motifs.insert(removeLine,addBackKmer)
    return motifs

def GibbsSampler (dnaMatrix,k,t,N):
    motifs = []
    for i in range (0,t):
        startPos = randint(0,matrixInfo[1]-k)
        randomMotif  = (dnaMatrix[i][startPos:startPos+k])
        motifs.append(randomMotif)
    BestMotifs = motifs
    for i in range (N):
        motifs = randomRemoveNformNewMotifs(motifs,dnaMatrix,k,t)
        if score(motifs,k,t) < score(BestMotifs,k,t):
            BestMotifs = motifs
    
    return BestMotifs

GibbsSampler(dnaMatrix,8,5,1000)

def runTest(times,k,t,N):
    minScore = 1000000
    bestRes = []
    for i in range (0,times):
        print ("times",i)
        resultMotif = GibbsSampler(dnaMatrix,k,t,N)
        resultScore = score(resultMotif,k,t)
        if resultScore < minScore:
            bestRes = resultMotif
            minScore = resultScore
    print(minScore)
    for m in range (0,t):
        row = ''.join(bestRes[m])
        print (row)
    return bestRes

#runTest(40,15,20,1000)

#--------------2H--------------
def distanceBetweenPatternAndString(pattern,Dna):
    k = len(pattern)
    distance  = 0
    for i in range (0,matrixInfo[0]):
        string = ''.join(dnaMatrix[i])
        HamDist = float("inf")
        for j in range (0,matrixInfo[1]-k+1):
            patternInDna = string[j:j+k]
            HamDistInDna = hammingDist(pattern,patternInDna)
            if HamDist > HamDistInDna:
                HamDist = HamDistInDna
        distance = distance + HamDist
    
    return (distance)

#print(distanceBetweenPatternAndString("ATCAA",dnaMatrix))


def buildMatrix (dataset):
    edgeDict = dict()
    for lines in dataset:
        input = lines.split()  
        preNode = input[0]
        #suffs = input[2]
        suffs = input[2].split(",")
        suffNode = []
        for suff in suffs:
            suffNode.append(suff)
            edgeDict[preNode] = suffNode
            
    nodes = sorted(edgeDict.keys())
    Matrix = [[0 for x in range(len(nodes))] for y in range(len(nodes))] 
    
    for i in range (len(nodes)):
        suffNodes =  edgeDict[nodes[i]]
        for suffNode in suffNodes:
            #print int(suffNode)
            Matrix[i][int(suffNode)] = Matrix[i][int(suffNode)]+1

    return Matrix

def getEdges (dataset):
    edgeList = []
    nodeList = []
    for lines in dataset:
        input = lines.split()
        preNode = input[0]
        suffs = input[2].split(",")
        suffNode = []
        for suff in suffs:
            edge = []
            edge.append(preNode+suff) 
            edgeList.append(edge)
    return edgeList

print (getEdges(dataset))