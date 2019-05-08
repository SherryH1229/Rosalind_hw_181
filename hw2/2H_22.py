#-------------extra functions-------------
#build the DNAs matrix
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

matrixInfo = getInfo("Dna")
dnaMatrix = buildDnasMatrix("Dna",matrixInfo[0],matrixInfo[1])
#print (dnaMatrix)

def hammingDist(str1,str2):
    if (len(str1)!=len(str2)):
        print("the lengths of two strings are not the same!")
        return 0
    dist = 0
    for i in range (0,len(str1)):
        if (str1[i]!=str2[i]):
            dist = dist + 1
    return dist

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

print(distanceBetweenPatternAndString("ATCAA",dnaMatrix))
