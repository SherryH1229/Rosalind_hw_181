#-------------extra Info--------------------
indelPenalty = 5
BLOSUM62 = {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}

#-------------extra functions--------------------
def readInfo(data):
    firstString = list(((data.readline()).splitlines())[0])
    secondString = list(((data.readline()).splitlines())[0])

    return firstString,secondString

#--------------------5K--------------------
def GlobalAlignment_linearSpace(Matrix,firstString,secondString): 
    times = 0
    Matrix[0][0] = -indelPenalty*times
    times +=1
    Matrix[0][1] = -indelPenalty*times
   
    for j in range (1,len(firstString)+1):
        for i in range (1,len(secondString)+1):
            Matrix[0][j%2] = -indelPenalty*times
            insertion = Matrix[i][(j-1)%2]-indelPenalty
            deletion = Matrix[i-1][j%2]-indelPenalty
            print firstString
            print [firstString[j-1]]
            print BLOSUM62[firstString[j-1]][secondString[i-1]]
            match = Matrix[i-1][(j-1)%2]+BLOSUM62[firstString[j-1]][secondString[i-1]]
            Matrix[i][j%2] = max(insertion,deletion,match)
        
        times +=1
    
    lastCol = [row[j%2] for row in Matrix]
    #print Matrix[i][j%2]
    return lastCol

def buildMatrix_linearSpace(firstString,secondString):
    i = len(secondString)+1
    j = 2
    Matrix = [[0 for x in range(j)] for y in range(i)]
    value = 0
    for i in range (len(secondString)):
        value -= indelPenalty
        Matrix[i+1][0] = value

    return Matrix

def splitStrings_N_buildMatrix(firstString,secondString):
    
    splitIndex_firstString = int(len(firstString)/2)
    firstString_firstHalf = firstString[0:splitIndex_firstString]
    firstString_secondHalf = (firstString[splitIndex_firstString:])[::-1]

    secondString_secondHalf = secondString[::-1]
    Matrix_firstHalf = buildMatrix_linearSpace(firstString_firstHalf,secondString)
    Matrix_seondHalf = buildMatrix_linearSpace(firstString_secondHalf,secondString_secondHalf)

    lastCol_firstHalf = GlobalAlignment_linearSpace(Matrix_firstHalf,firstString_firstHalf,secondString)
    lastCol_secondHalf = GlobalAlignment_linearSpace(Matrix_seondHalf,firstString_secondHalf,secondString_secondHalf)

    maxVlaue = float("-inf")
    mediumCol = []
    for i in range (0,len(lastCol_firstHalf)):
        currentValue = lastCol_firstHalf[i]+lastCol_secondHalf[len(lastCol_secondHalf)-1-i]
        mediumCol.append(currentValue)
        if  currentValue > maxVlaue:
            pos = i
            maxVlaue = currentValue
    
    if pos == len(firstString):
        secPos = pos
    else: 
        secPos = pos+1
    
    firstPos = (pos,splitIndex_firstString)
    secondPos = (secPos,splitIndex_firstString+1)
    
    return firstPos,secondPos
#---------------------exe----------------------------
def exe(data):
    firstString,secondString = readInfo(data)
    #firstPos,secondPos = splitStrings_N_buildMatrix(secondString,firstString)
    # print str(firstPos) + '  ' + str(secondPos)'
    matrix = buildMatrix_linearSpace(firstString,secondString)
    GlobalAlignment_linearSpace(matrix,firstString,secondString)
data = open("pattern","r")
exe(data)