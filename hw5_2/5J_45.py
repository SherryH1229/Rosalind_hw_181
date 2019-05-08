#-------------extra Info--------------------
sigma = 11
epsilon = 1
BLOSUM62 = {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}
#-------------extra functions--------------------
def readInfo(data):
    firstString = list(((data.readline()).splitlines())[0])
    secondString = list(((data.readline()).splitlines())[0])

    return firstString,secondString
#--------------------5J--------------------
def buildMatrix(firstString,secondString):
    i = len(secondString)+1
    j = len(firstString)+1

    MatrixLower = [[0 for x in range(j)] for y in range(i)]
    MatrixMiddle = [[0 for x in range(j)] for y in range(i)]
    MatrixUpper = [[0 for x in range(j)] for y in range(i)]
    
    tracebackLower = [[0 for x in range(j)] for y in range(i)]
    tracebackMiddle = [[0 for x in range(j)] for y in range(i)]
    tracebackUpper = [[0 for x in range(j)] for y in range(i)]
    
    multiple = 0
    for i in range (len(secondString)): 
        MatrixMiddle[i+1][0] = -sigma-multiple*epsilon
        MatrixLower[i+1][0] = -sigma-multiple*epsilon
        MatrixUpper[i+1][0] = float("-inf")
        multiple += 1
    
    multiple = 0
    for j in range (len(firstString)):
        MatrixMiddle[0][j+1] = -sigma-multiple*epsilon
        MatrixUpper[0][j+1] = -sigma-multiple*epsilon
        MatrixLower[0][j+1] = float("-inf")
        multiple += 1
    
    return MatrixUpper,MatrixMiddle,MatrixLower,tracebackUpper,tracebackMiddle,tracebackLower         

def GlobalAlignment_withGapPenalties(MatrixUpper,MatrixMiddle,MatrixLower,tracebackUpper,tracebackMiddle,tracebackLower,firstString,secondString): 
    for i in range (1,len(secondString)+1):
        for j in range (1,len(firstString)+1):
            MatrixLower[i][j] = max(MatrixLower[i-1][j]-epsilon,MatrixMiddle[i-1][j]-sigma)
            if MatrixLower[i][j] == MatrixMiddle[i-1][j]-sigma:
                tracebackLower[i][j] = "Middle"
            elif MatrixLower[i][j] == MatrixLower[i-1][j]-epsilon:
                tracebackLower[i][j] = "down"
            

            MatrixUpper[i][j] = max(MatrixUpper[i][j-1]-epsilon,MatrixMiddle[i][j-1]-sigma)
            if MatrixUpper[i][j] == MatrixMiddle[i][j-1]-sigma:
                tracebackUpper[i][j] = "Middle"
            elif MatrixUpper[i][j] == MatrixUpper[i][j-1]-epsilon:
                tracebackUpper[i][j] =  "right"
            

            MatrixMiddle[i][j] = max(MatrixLower[i][j],MatrixMiddle[i-1][j-1]+BLOSUM62[firstString[j-1]][secondString[i-1]],MatrixUpper[i][j])
            if MatrixMiddle[i][j] == MatrixUpper[i][j]:
                tracebackMiddle[i][j] = "Upper"
            elif MatrixMiddle[i][j] == MatrixLower[i][j]:
                tracebackMiddle[i][j] = "Lower"
            else:
                tracebackMiddle[i][j] = "dia"
   
    maxScore = MatrixMiddle[i][j]
    return tracebackLower,tracebackUpper,tracebackMiddle,maxScore

def tracingBack_withGapPenalties(traceL,traceM,traceU,v,w):
    firstString = []
    secondString = []
    i = len(v)
    j = len(w)
    current = traceM
    #print traceM[i][j]
    while i > 0 and j > 0:
        if current[i][j] == "Upper":
            #print 1
            current = traceU
            firstString.append(w[j-1])
            secondString.append("-")
            j = j-1

        elif current[i][j] == "right":
            #print 2
            firstString.append(w[j-1])
            secondString.append("-")
            j = j-1

        elif current[i][j] == "Middle":
            #print 3
            current = traceM

        elif current[i][j] == "dia":
            #current = traceM
            #print 4
            firstString.append(w[j-1])
            secondString.append(v[i-1])
            i = i-1
            j = j-1
        elif current[i][j] == "Lower":
            #print 5
            current = traceL
            firstString.append("-")
            secondString.append(v[i-1])
            i = i-1 
        elif current[i][j] == "down":
            #print 6
            firstString.append("-")
            secondString.append(v[i-1])
            i = i-1 
            
    firstString = ''.join(firstString[::-1])
    secondString = ''.join(secondString[::-1])
    print firstString
    print secondString
    return firstString,secondString
#---------------------exe----------------------------
def exe(data):
    firstString,secondString = readInfo(data)
    MatrixUpper,MatrixMiddle,MatrixLower,tracebackUpper,tracebackMiddle,tracebackLower = buildMatrix(firstString,secondString)
    traceL,traceU,traceM,maxScore = GlobalAlignment_withGapPenalties(MatrixUpper,MatrixMiddle,MatrixLower,tracebackUpper,tracebackMiddle,tracebackLower,firstString,secondString)
    print maxScore
    tracingBack_withGapPenalties(traceL,traceM,traceU,secondString,firstString)
    
data = open("pattern","r")
exe(data)