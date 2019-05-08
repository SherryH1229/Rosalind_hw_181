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
            points.append(tuple(p))
    
    return k,m,points

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

def center_of_gravity(cluster):
    centers_num = []
    centers_str = []
    for key,value in cluster.iteritems():
        points  = []
        points.append(key)
        points += value
        string = []
        number = []
        for j in range (len(points[0])):
            string.append(format(sum([i[j] for i in points])/len(points), '.3f'))
            number.append(round(sum([i[j] for i in points])/len(points),3))
        centers_str.append(tuple(string))
        centers_num.append(tuple(number))
 
    return tuple(centers_num),centers_str

def Lloyd(k,m,points):
    centers = points[:k]
    
    while True:
        cluster = dict()
        for c in centers:
            cluster[c] = []
        for dp in points:
      
            cluster[nearest_Center(centers,dp,m)].append(dp)

        centers_update_num,centers_update_str = center_of_gravity(cluster)
    
        if centers_update_num == centers:
            return centers_update_str
        
        else:
            centers = centers_update_num
 

def exe(data):
    k,m,points = readInfo(data)

    centers = Lloyd(k,m,points)
    for c in centers:
        print ' '.join(c)
    
data = open("pattern","r")
exe(data)