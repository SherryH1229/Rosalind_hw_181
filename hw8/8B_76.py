def readInfo(data):
    t = map(int,data.readline().split())
    k = t[0]
    m = t[1]

    centers = []
    for i in range (k):
        centers.append(map(float,data.readline().split()))
    data.readline()
   
    points = []
    while True:
        p = map(float,data.readline().split())
        if len(p) == 0:
            break
        else:
            points.append(p)
    
    return k,m,centers,points

def d(dp,center,m):
    i = 0
    value = 0
    while i < m:
        value += (dp[i]-center[i])**2
        i += 1
    dist = value**(0.5)
    return dist

def nearest_Center(Centers,point,m):
    distance = [d(point,c,m) for c in Centers]
    ind = distance.index(min(distance))
    return Centers[ind]

def Distortion(Data, Centers,m):
    value = 0
    for dp in Data:
        nearestC = nearest_Center(Centers,dp,m)
        distance = d(dp,nearestC,m)
        value += distance**2
    
    finalVal = value/(len(Data))
    return finalVal
        
def exe(data):
    k,m,centers,points = readInfo(data)
    print Distortion(points,centers,m)

data = open("pattern","r")
exe(data)