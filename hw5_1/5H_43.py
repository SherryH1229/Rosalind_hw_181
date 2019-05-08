indelPenalty = 1
#-------------extra functions--------------------
def readInfo(data):
    firstString = list(((data.readline()).splitlines())[0])
    secondString = list(((data.readline()).splitlines())[0])

    return firstString,secondString

def buildMatrix(firstString,secondString):
    i = len(secondString)+1
    j = len(firstString)+1
    Matrix = [[0 for x in range(j)] for y in range(i)]
    traceback = [[0 for x in range(j)] for y in range(i)]
    value = 0
    for i in range (len(secondString)):
        value -= 1
        Matrix[i+1][0] = value
    
    #value = 0
    #for j in range (len(firstString)):
    #    value -= 1
    #    Matrix[0][j+1] = value
        
    return Matrix,traceback

def localAlignment(Matrix,firstString,secondString,traceback):
    #maxScore = 0
    for i in range (1,len(secondString)+1):
        for j in range (1,len(firstString)+1):
            insertion = Matrix[i][j-1]-indelPenalty
            deletion = Matrix[i-1][j]-indelPenalty
            match = Matrix[i-1][j-1]+1 if secondString[i-1] == firstString[j-1] else Matrix[i-1][j-1]-indelPenalty
            Matrix[i][j] = max(insertion,deletion,match,0)            
            if Matrix[i][j] == 0:
                traceback[i][j] = "break"
            elif Matrix[i][j] == deletion:
                traceback[i][j] = "down"
            elif Matrix[i][j] == insertion:
                traceback[i][j] = "right"
            elif Matrix[i][j] == match:
                traceback[i][j] = "dia"
    for row in Matrix:
        print row
    return Matrix,traceback

def tracingBack_localAlignment(Backtrack,v,w,startPos):
    firstString = []
    secondString = []
    i = startPos[0]
    j = startPos[1]
    while i > 0 and j > 0:
        if Backtrack[i][j] == "break":
           firstString.append("-")
           secondString.append("-")
           i = i-1
           j = j-1

        if Backtrack[i][j] == "down":
            firstString.append("-")
            secondString.append(v[i-1])
            i = i-1
        elif Backtrack[i][j] == "right":
            firstString.append(w[j-1])
            secondString.append("-")
            j = j-1
        elif Backtrack[i][j] == "dia":
            firstString.append(w[j-1])
            secondString.append(v[i-1])
            i = i-1
            j = j-1
         
        if i == 0:
            #firstString.append(w[j-1])
           # secondString.append("-")
            break
        #elif j == 0 and i != 0:
        #    firstString.append("-")
        #    secondString.append(v[i-1])
     
    firstString = ''.join(firstString[::-1])
    secondString = ''.join(secondString[::-1])

    return firstString,secondString
#--------------------5H--------------------
def exe(data):
    firstString,secondString = readInfo(data)
    Matrix,traceback = buildMatrix(firstString,secondString)
    Matrix,traceBack = localAlignment(Matrix,firstString,secondString,traceback)
    x = len(secondString)
    maxValue = max(Matrix[-1])
    for i in range (len(Matrix[-1])):
        if Matrix[-1][i] >= maxValue:
            y = i
    startPos = (x,y)
    first,second = tracingBack_localAlignment(traceBack,secondString,firstString,startPos)
    print maxValue
    print first
    print second
   
data = open("pattern","r")
exe(data)