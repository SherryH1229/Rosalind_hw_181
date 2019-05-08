import math

def readInfo(data):
    t = map(int,data.readline().split())
    k = t[0]
    m = t[1]
    beta = data.readline().rstrip("\n")
    points = []
    while True:
        p = map(float,data.readline().split())
        if len(p) == 0:
            break
        else:
            points.append(tuple(p))

    return k,m,float(beta),points

def d(dp,center,m):
    i = 0
    value = 0
 
    while i < m:
        value += (dp[i]-center[i])**2
        i += 1
    #dist = math.sqrt(value)
    dist = value**(0.5)
    return dist

def HiddenMatrix(centers,beta,points,m):
    hidden_matrix = []
    for center in centers:
        hm = []
        for p in points:
            value = math.exp(-beta*(d(p,center,m)))
            hm.append(value)
        hidden_matrix.append(hm)
    summation = [sum(x) for x in zip(*hidden_matrix)]
    res = []
    for hmx in hidden_matrix:
        res.append([x/y for x,y in zip(hmx,summation)])
    return res

def update_center(hm,points):
    value = sum(hm)
    points_theta = []
    for h,p in zip(hm,points):
        theta = []
        for subPos in p:
            theta.append((subPos*h)/value)
        points_theta.append(theta)
    
    summation = [sum(x) for x in zip(*points_theta)]
    return tuple(summation)

def soft_Kmeans(k,m,beta,points):
    centers = points[:k]
    count = 0
    while count < 100:
        hm =  HiddenMatrix(centers,beta,points,m)
        centers = [update_center(sub_hm,points) for sub_hm in hm]
        count += 1
    return centers

def exe(data):
    k,m,beta,points = readInfo(data)
    center = soft_Kmeans(k,m,beta,points)
    for c in center:
        print ' '.join(map(str,c))
    
data = open("pattern","r")
exe(data)