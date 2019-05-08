def readinfo(data):
    firstString = list(((data.readline()).splitlines())[0])
    secondString = list(((data.readline()).splitlines())[0])
    thirdString = list(((data.readline()).splitlines())[0])

    return firstString,secondString,thirdString

def buildMatrix(firstString,secondString,thirdString):
    i = len(firstString)+1
    j = len(secondString)+1
    k = len(thirdString)+1
    Matrix = [[[0 for z in range(k)] for y in range(j)] for x in range(i)]
    traceback = [[[0 for z in range(k)] for y in range(j)] for x in range(i)]
    
    return Matrix,traceback

def GlobalAlignment_multi(Matrix,firstString,secondString,thirdString,traceback): 
    for i in range (1,len(firstString)+1):
        for j in range (1,len(secondString)+1):
            for k in range (1,len(thirdString)+1):
                match = Matrix[i-1][j-1][k-1]+1 if firstString[i-1] == secondString[j-1] == thirdString[k-1] else Matrix[i-1][j-1][k-1]
                maxValue = max(Matrix[i-1][j][k],Matrix[i][j-1][k],Matrix[i][j][k-1],Matrix[i-1][j-1][k],Matrix[i-1][j][k-1],Matrix[i][j-1][k-1],match)
                Matrix[i][j][k] = maxValue
                if maxValue == match:
                    traceback[i][j][k] = 7
                elif maxValue == Matrix[i-1][j][k]:
                    traceback[i][j][k] = 1
                elif maxValue == Matrix[i][j][k-1]:
                    traceback[i][j][k] = 3
                elif maxValue == Matrix[i][j-1][k]:
                    traceback[i][j][k] = 2
                elif maxValue == Matrix[i-1][j-1][k]:
                    traceback[i][j][k] = 4
                elif maxValue == Matrix[i-1][j][k-1]:
                    traceback[i][j][k] = 5
                elif maxValue == Matrix[i][j-1][k-1]:
                    traceback[i][j][k] = 6
                       
    return Matrix[i][j][k], traceback

def TraceBack_multi(Backtrack,first,second,third):
    firstString = list(first)
    secondString = list(second)
    thirdString = list(third)
    i = len(first)
    j = len(second)
    k = len(third)
    while i > 0 and j > 0 and k > 0:
        if Backtrack[i][j][k] == 1:
            secondString.insert(j,"-")
            thirdString.insert(k,"-")
            i = i-1
        elif Backtrack[i][j][k] == 2:
            firstString.insert(i,"-")
            thirdString.insert(k,"-")
            j = j-1
        elif Backtrack[i][j][k] == 3:
            firstString.insert(i,"-")
            secondString.insert(j,"-")
            k = k-1
        elif Backtrack[i][j][k] == 4:
            thirdString.insert(k,"-")
            i = i-1
            j = j-1
        elif Backtrack[i][j][k] == 5:
            secondString.insert(j,"-")
            i = i-1
            k = k-1
        elif Backtrack[i][j][k] == 6: 
            firstString.insert(i,"-")
            j = j-1
            k = k-1
        elif Backtrack[i][j][k] == 7:
            i = i-1
            j = j-1
            k = k-1

    while len(firstString) != max(len(firstString),len(secondString),len(thirdString)):
        firstString.insert(0,"-")
    while len(secondString) != max(len(firstString),len(secondString),len(thirdString)):
        secondString.insert(0,"-")
    while len(thirdString) != max(len(firstString),len(secondString),len(thirdString)):
        thirdString.insert(0,"-")

    firstString = ''.join(firstString)
    secondString = ''.join(secondString)
    thirdString = ''.join(thirdString)

    return firstString,secondString,thirdString
    
def exe(data):
    first,second,third = readinfo(data)
    Matrix,traceBack = buildMatrix(first,second,third)
    maxScore,traceBack = GlobalAlignment_multi(Matrix,first,second,third,traceBack)
    print maxScore
    firstString,secondString,thirdString = TraceBack_multi(traceBack,first,second,third)
    print firstString
    print secondString
    print thirdString

data = open("pattern","r")
exe(data)

