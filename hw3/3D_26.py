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

#-------------3D-------------------
def buildDebruijnMatrix(KmerList):
    #remove duplicates
    KmerList = set(KmerList)
    KmerList  = list(KmerList)
    KmerList.sort()
    
    length = len(KmerList)
    Matrix = [[0 for x in range(length)] for y in range(length)] 

    return (KmerList,Matrix)
    
def DeBruijnGraph (num,string):
    nameList = kmerComp(num-1,string)
    colnames, DebruijnMatrix = buildDebruijnMatrix(nameList)
    KmerList = kmerComp(num,string)
    for kmer in KmerList:
        preNode = prefix(kmer)
        sufNode = suffix(kmer)
        i = colnames.index(preNode)
        j = colnames.index(sufNode)

        DebruijnMatrix[i][j] = DebruijnMatrix[i][j]+1

    return DebruijnMatrix, colnames

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

matrix,colnames = DeBruijnGraph(12,"AAGATTCTCTAC")
printDeBruijnGraph(matrix,colnames)