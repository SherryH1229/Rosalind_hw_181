import sys
sys.setrecursionlimit(50000)
#-------------extra Info--------------------
indelPenalty = 5
BLOSUM62 = {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}
#-------------extra functions--------------------
def readInfo(data):
    firstString = list(((data.readline()).splitlines())[0])
    secondString = list(((data.readline()).splitlines())[0])

    return firstString,secondString

def GlobalAlignment_linearSpace(Matrix,firstString,secondString,traceback): 
    times = 0
    Matrix[0][0] = -indelPenalty*times
    times +=1
    Matrix[0][1] = -indelPenalty*times
    traceback[0][1] = "right"
    traceback[0][0] = "right"

    for j in range (1,len(firstString)+1):
        for i in range (1,len(secondString)+1):
            Matrix[0][j%2] = -indelPenalty*times
            insertion = Matrix[i][(j-1)%2]-indelPenalty
            deletion = Matrix[i-1][j%2]-indelPenalty
            match = Matrix[i-1][(j-1)%2]+BLOSUM62[firstString[j-1]][secondString[i-1]]
            Matrix[i][j%2] = max(insertion,deletion,match)
            if Matrix[i][j%2] == insertion:
                traceback[i][j%2] = "right"
            elif Matrix[i][j%2] == deletion:
                traceback[i][j%2] = "down"
            elif Matrix[i][j%2] == match:
                traceback[i][j%2] = "dia"
        
        times +=1
    
    lastCol = [row[j%2] for row in Matrix]
    trace = [row[j%2] for row in traceback]
    return lastCol,trace

def buildMatrix_linearSpace(firstString,secondString):
    i = len(secondString)+1
    j = 2
    Matrix = [[0 for x in range(j)] for y in range(i)]
    TraceBack = [[0 for x in range(j)] for y in range(i)]
    value = 0
    for i in range (len(secondString)):
        value -= indelPenalty
        Matrix[i+1][0] = value
    for i in range (len(secondString)):
        TraceBack[i+1][0] = "down"
    return Matrix,TraceBack

def MiddleEdge(firstString,secondString):
    splitIndex_firstString = int(len(firstString)/2)
    firstString_firstHalf = firstString[0:splitIndex_firstString]
    firstString_secondHalf = (firstString[splitIndex_firstString:])[::-1]
    if len(firstString_firstHalf) == 0:
        firstString_firstHalf = firstString_secondHalf
    elif len(secondString) == 0:
        firstString_secondHalf = firstString_firstHalf
    #print (firstString,secondString)
    #print firstString_firstHalf
    #print firstString_secondHalf
    secondString_secondHalf = secondString[::-1]
    Matrix_firstHalf,trace_firstHalf = buildMatrix_linearSpace(firstString_firstHalf,secondString)
    Matrix_seondHalf,trace_secondHalf = buildMatrix_linearSpace(firstString_secondHalf,secondString_secondHalf)

    lastCol_firstHalf,lastCol_firstHalf_traceBack = GlobalAlignment_linearSpace(Matrix_firstHalf,firstString_firstHalf,secondString,trace_firstHalf)
    lastCol_secondHalf,lastCol_secondHalf_traceBack = GlobalAlignment_linearSpace(Matrix_seondHalf,firstString_secondHalf,secondString_secondHalf,trace_secondHalf)

    maxVlaue = float("-inf")
    mediumCol = []
    for i in range (1,len(lastCol_firstHalf)):
        currentValue = lastCol_firstHalf[i]+lastCol_secondHalf[len(lastCol_secondHalf)-1-i]
        if  currentValue > maxVlaue:
            info = (i,lastCol_secondHalf_traceBack[len(lastCol_secondHalf)-1-i])
            maxVlaue = currentValue

    MiddleEdge_ini = (info[0],splitIndex_firstString)
    if info[1] == "dia":
        MiddleEdge_term = (MiddleEdge_ini[0]+1,MiddleEdge_ini[1]+1)
    elif info[1] == "right":
        MiddleEdge_term = (MiddleEdge_ini[0],MiddleEdge_ini[1]+1)
    elif info[1] == "down":
        MiddleEdge_term = (MiddleEdge_ini[0]+1,MiddleEdge_ini[1])
    else:
        print info[1]
    #print MiddleEdge_ini
    #print MiddleEdge_term
    return MiddleEdge_ini,MiddleEdge_term,info[1]
#--------------------5L--------------------
def linearSpaceAlignment(v,w,top,bottom,left,right):
    print (v,w,top,bottom,left,right)
    if left == right: 
        print "???????????"
        #firstString = v[top:bottom]
        #secondString = ['-'*(bottom - top)]
        return [v[top:bottom], '-'*(bottom - top)]
    
    elif top == bottom:
        print "?????????????"
        #firstString = ['-'*(right - left)]
        #secondString = w[left:right]
        return ['-'*(right - left), w[left:right]]
   
    else:
        print "!!!!!!!"
        middle = int((left+right)/2)
        MiddleEdge_ini,MiddleEdge_termi,midEdge = MiddleEdge(v[top:bottom], w[left:right])
        midNode = tuple(map(sum, zip(MiddleEdge_ini, [top, left])))
        nextNode = tuple(map(sum, zip(MiddleEdge_termi, [top, left])))
        current = [['-', v[midNode[0] % len(v)]][nextNode[0] - midNode[0]], ['-', w[midNode[1] % len(w)]][nextNode[1] - midNode[1]]]
        
        A = linearSpaceAlignment(v,w,top, midNode[0], left, midNode[1])
        B = linearSpaceAlignment(v,w,nextNode[0], bottom, nextNode[1], right)

        return [A[i] + current[i] + B[i] for i in xrange(2)]
#---------------------exe----------------------------
def exe(data):
    firstString,secondString = readInfo(data)
    
    #firstPos,secondPos = MiddleEdge(secondString,firstString,0,len(firstString),0,len(secondString))
    linearSpaceAlignment(secondString,firstString,0,len(secondString),0,len(firstString))
    #print str(firstPos) + '  ' + str(secondPos)

data = open("pattern","r")
exe(data)