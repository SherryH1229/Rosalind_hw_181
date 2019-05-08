#-------------extra_functions----------
def prefix(pattern):
    prefix = pattern[0:-1]
    return prefix

def suffix(pattern):
    suffix = pattern[1:]
    return suffix

def kmerComp(k,string):
    kmerList = []
    for i in range (len(string)-k+1):
        kmerList.append(string[i:i+k])
    kmerList.sort()
    return kmerList
def buildDebruijnMatrix(KmerList):
    #remove duplicates
    KmerList = set(KmerList)
    KmerList  = list(KmerList)
    KmerList.sort()
    
    length = len(KmerList)
    Matrix = [[0 for x in range(length)] for y in range(length)] 

    return (KmerList,Matrix)

def printDeBruijnGraph(DebruijnMatrix,colnames):
    i = 0
    for row in DebruijnMatrix:
        output = (colnames[i]+" ->").split()
        j = [k for k, e in enumerate(row) if e != 0]
        suff = []
        if len(j) != 0:
            for index in j:
                for k in range (row[index]):
                    suff.append(colnames[index])
            suff = (','.join(suff)).split()   
            outString = output+suff
            print (' '.join(outString))
        i = i+1

def DeBruijnGraph (num,KmerList,patterString):
    colnames, DebruijnMatrix = buildDebruijnMatrix(KmerList)
   
    for pattern in patternString:
        #print ''.join(pattern)
        preNode = prefix(''.join(pattern))
        sufNode = suffix(''.join(pattern))
        i = colnames.index(preNode)
        j = colnames.index(sufNode)
        DebruijnMatrix[i][j] = DebruijnMatrix[i][j]+1

    return DebruijnMatrix, colnames

#-------------3E-------------------
patterns = open("pattern","r")
patternString = []
for line in patterns:
    patternString.append(line.splitlines())

#def getUniqKmer
length = len((patternString[0])[0])
flat_PatternString = ([item for sublist in patternString for item in sublist])


uniqueK_1_mers = []
for pattern in flat_PatternString:
    uniqueK_1_mers.append(prefix(pattern))
    uniqueK_1_mers.append(suffix(pattern))

matrix,colnames = DeBruijnGraph(length,uniqueK_1_mers,flat_PatternString)
printDeBruijnGraph(matrix,colnames)

#print (colnames)

