#---------------extra functions----------

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
    for i in range (0,len(text)-k+1):
        patternInDna = text[i:i+k]
        #print (patternInDna)
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
            #print (maxProb)
            probableKmer = patternInDna
            #print (probableKmer)
    return probableKmer

print (mostProbableKmer("CCCTAGCATTCGCTTGTACCTGCTCGTTGTCCTTAAGGATAGTGCGCCCGATTTAAGTAGTTAACATTTGCAGCTACTAACTCTCTCCTGTCCAAGGAAAGCGCTGACAGTCAACTCCAGGTTCTACGATGGAGCGTTGGCTCAGGGTACTAGGTAGTAGCCCGGCTGAGAGGGAGAGGTATCGTCCCGTACAGGCTCGG",7,profileMatrix))