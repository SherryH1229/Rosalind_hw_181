def readInfo(data):
    reads = []
    num = 0
    for lines in data:
        line = lines.splitlines()[0]
        reads.append(list(line))
        #num+=1

    return reads

def LCSBacktrack(v,w):
    Matrix = [[0 for x in range(len(w)+1)] for y in range(len(v)+1)]
    backtrack = [[0 for x in range(len(w)+1)] for y in range(len(v)+1)]
    
    for i in range (1,len(v)+1):
        for j in range (1,len(w)+1):
            Matrix[i][j] = max((Matrix[i-1][j]),(Matrix[i][j-1]),(Matrix[i-1][j-1]+1 if v[i-1]==w[j-1] else 0))
            if Matrix[i][j] == Matrix[i-1][j]:
                backtrack[i][j] = "down" 
            elif Matrix[i][j] == Matrix[i][j-1]:
                backtrack[i][j] = "right"
            elif Matrix[i][j] == Matrix[i-1][j-1]+1 and v[i-1]==w[j-1]:
                backtrack[i][j] = "dia"
    return backtrack

'''def outputLCS(Backtrack,v,i,j):
    if i == 0 or j == 0:
        return 
    if Backtrack[i][j] == 
    if Backtrack[i][j] == "down":
        outputLCS(Backtrack,v,i-1,j)
    elif Backtrack[i][j] == "right":
        outputLCS(Backtrack,v,i,j-1)
    else:
        outputLCS(Backtrack,v,i-1,j-1):
        
    return 0'''

def IterativeOutputLCS(Backtrack,v,w):
    LCS = []
    i = len(v)
    j = len(w)
    while i > 0 and j > 0:
        if Backtrack[i][j] == "down":
            i = i-1 
        elif Backtrack[i][j] == "dia":
            LCS.append(v[i-1])
            i = i-1
            j = j-1
        elif Backtrack[i][j] == "right":
            j = j-1  
    return ''.join(LCS[::-1])
          

def exe(data):
    reads = readInfo(data)
    backtrack = LCSBacktrack(reads[0],reads[1])
    LCS = IterativeOutputLCS(backtrack,reads[0],reads[1])
    print LCS
    
data = open("pattern","r")
exe(data)