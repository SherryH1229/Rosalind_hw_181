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

def numberToSymbol(index):
    if index == 0:
        symbol = "A"
    elif index == 1:
        symbol = "C"
    elif index == 2:
        symbol = "G"
    else:
        symbol = "T"
    return symbol
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

def hammingDist(str1,str2):
    if (len(str1)!=len(str2)):
        print("the lengths of two strings are not the same!")
        return 0
    dist = 0
    for i in range (0,len(str1)):
        if (str1[i]!=str2[i]):
            dist = dist + 1
    return dist
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

result = greedyMotifSearch(dnaMatrix,5,8)
