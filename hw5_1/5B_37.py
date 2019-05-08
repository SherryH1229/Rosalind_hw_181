def readInfo(data):
    firstLine = (((data.readline()).splitlines())[0]).split()
    downRowNum = int(firstLine[0])
    rightRowNum = int(firstLine[1])

    downWeight_col = []
    for i in range (int(downRowNum)):
        downWeight = map(int,((data.readline()).splitlines())[0].split())
        downWeight_col.append(downWeight)
    data.readline()

    rightWeight_row = []
    for i in range (int(downRowNum)+1):
        rightWeight = map(int,((data.readline()).splitlines())[0].split())
        rightWeight_row.append(rightWeight)
   
    return int(downRowNum), int(rightRowNum),downWeight_col,rightWeight_row


def ManhattanTourist(n,m,down,Right):
    Matrix = [[0 for x in range(m+1)] for y in range(n+1)]
    for i in range (1,n+1):
        Matrix[i][0] = Matrix[i-1][0]+down[i-1][0]
    
    for j in range (1,m+1):
        Matrix[0][j] = Matrix[0][j-1]+Right[0][j-1]

    for i in range (1,n+1):
        for j in range (1,m+1):
            Matrix[i][j] = max((Matrix[i-1][j]+down[i-1][j]),(Matrix[i][j-1]+Right[i][j-1]))

    return Matrix[n][m]


data = open("pattern","r")
def exe(data):
    n,m,downMatrix,rightMarix = readInfo(data)
    print(ManhattanTourist(n,m,downMatrix,rightMarix))

exe(data)

