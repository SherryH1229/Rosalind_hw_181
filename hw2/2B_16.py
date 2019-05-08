#build the DNAs matrix
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
def quotient(index,num):
    quotient = int(index/num)
    return quotient
def remainder(index,num):
    quot = quotient(index,num)
    remainder = index-quot*num

    return remainder
def numberToPattern(index,k):    
    if k == 1:
        return numberToSymbol(index)
    prefixIndx = quotient(index,4)
    r = remainder(index,4)
    symbol = numberToSymbol(r)
    prefixPattern = numberToPattern(prefixIndx,k-1)
    
    return prefixPattern+symbol

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

print (medianString(dnaMatrix,6))

