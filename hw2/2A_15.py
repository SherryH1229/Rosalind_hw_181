#_________extra functions
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

#_____________2A
#requre to copy and paste all the DNA strings into a file and name it as Dna
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
            
print (motifEnumeration(dnaMatrix,5,2))
