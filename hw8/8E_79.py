def readInfo(data):
    n = map(int,data.readline().split())
    points = []
    while True:
        p = map(float,data.readline().split())
        if len(p) == 0:
            break
        else:
            points.append(p)

    return n, points

def find_minValue_index(matirx):
    index = 0
    minimum = float("inf")
    start_index = 1
    for row in matirx:
        r = row[start_index:]
        if len(r) < 1:
            break
        v = min(r)
        ind = row.index(v)
        if v < minimum:
            y = ind
            x = index
            smallestValue = v
            minimum  = v
        index+=1
        start_index+=1 
    return [x,y]

def reform_matrix(matrix,matrixRowName,p):
    
    pos = list(p)
    pos = sorted(pos, key=int,reverse=True) 
    len_a = float(len(matrixRowName[pos[0]]))
    len_b = float(len(matrixRowName[pos[1]]))
    newRow = [(a*len_a+b*len_b)/(len_a+len_b) for a,b in zip(matrix[pos[0]],matrix[pos[1]])]

    matrix[pos[1]] = newRow
    matrix.pop(pos[0])
    temp = list(newRow)
    temp.pop(pos[0])

    for i in range (len(matrix)):
        matrix[i].pop(pos[0])
        matrix[i][pos[1]] = temp[i]
    
    label1 = matrixRowName.pop(pos[0])
    label2 = matrixRowName.pop(pos[1])
    labels = label2+label1    
    matrixRowName.insert(pos[1],labels)
    
    return matrix,matrixRowName,labels

def Hierarchical_Clustering(n,matrix):
    matrixRowName = []
    for i in range (1,n[0]+1):
        matrixRowName.append([i])
    while len(matrixRowName) >1 :    
        pos = find_minValue_index(matrix)
        matrix,matrixRowName,cluster = reform_matrix(matrix,matrixRowName,pos)

def exe(data):
    n,distance_matrix = readInfo(data)
    Hierarchical_Clustering(n,distance_matrix)
    for v in tag_list:
        print ' '.join(map(str,v))
    
data = open("pattern","r")
exe(data)