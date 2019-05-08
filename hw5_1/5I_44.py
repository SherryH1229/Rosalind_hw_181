indelPenalty = 2
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

def GlobalAlignment(Matrix,firstString,secondString,traceback): 
    for i in range (1,len(secondString)+1):
        for j in range (1,len(firstString)+1):
            insertion = Matrix[i][j-1]-indelPenalty
            deletion = Matrix[i-1][j]-indelPenalty
            match = Matrix[i-1][j-1]+1 if secondString[i-1] == firstString[j-1] else Matrix[i-1][j-1]-indelPenalty
            Matrix[i][j] = max(insertion,deletion,match)
            
            if Matrix[i][j] == insertion:
                traceback[i][j] = "right"
            elif Matrix[i][j] == deletion:
                traceback[i][j] = "down"
            elif Matrix[i][j] == match:
                traceback[i][j] = "dia"
        
    return Matrix, traceback

def tracingBack_localAlignment(Backtrack,v,w,startPos):
    firstString = []
    secondString = []
    i = startPos[0]
    j = startPos[1]
    while i > 0 and j > 0:
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
#--------------------5I--------------------
def exe(data):
    firstString,secondString = readInfo(data)
    Matrix,traceback = buildMatrix(firstString,secondString)
    Matrix,traceBack = GlobalAlignment(Matrix,firstString,secondString,traceback)
    lastCol = [item[-1] for item in Matrix]
    x = lastCol.index(max(lastCol))
    y = len(firstString)
    startPos = (x,y)
    first,second = tracingBack_localAlignment(traceBack,secondString,firstString,startPos)
    print max(lastCol)
    print first
    print second
   

data = open("pattern","r")
exe(data)