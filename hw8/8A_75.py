#import math

def readInfo(data):
    t = map(int,data.readline().split())
    k = t[0]
    m = t[1]
    points = []
    while True:
        p = map(float,data.readline().split())
        if len(p) == 0:
            break
        else:
            points.append(p)
    
    return k,m,points

def d(dp,center,m):
    i = 0
    value = 0
    while i < m:
        value += (dp[i]-center[i])**2
        i += 1
    #dist = math.sqrt(value)
    dist = value**(0.5)
    return dist

def maxDist(Data,Centers,m):
    value = []
    for dp in Data:
        minValue = min([d(dp,c,m) for c in Centers])
        value.append(minValue)
    index = value.index(max(value))
    return index

def farthestFirstTraversal(Data,k,m):
    Centers = [Data[0]]
    while len(Centers) < k:
        Index = maxDist(Data,Centers,m)
        Centers.append(Data[Index])

    return Centers
   
def exe(data):
    k,m,points = readInfo(data)
    Centers = farthestFirstTraversal(points,k,m)
    for c in Centers:
        print ' '.join(map(str,c))

data = open("pattern","r")
exe(data)
  