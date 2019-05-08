import numpy as np
import math

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

def cluster_distance(ca,cb,dm):
    dab = 0.
    for i in ca:
        for j in cb:
            dab += dm[i-1,j-1]
    dab = dab / (1.*len(ca)*len(cb))
    return dab

def hierarchical_clustering(n,dm):
    c = [ [1+i,] for i in range(n)]
    #print c
    r = []
    odm = dm
    while len(dm)>2:
        n = len(dm)
        a,b = np.unravel_index(np.argmin(dm + np.eye(n)*dm.max()),(n,n))
        ca = c[a][:]
        cb = c[b][:]
        cc = ca+cb      
        c.remove(ca)
        c.remove(cb)
        c.append(cc)
        dm = np.delete(dm,(a,b),0)
        dm = np.delete(dm,(a,b),1)
        ndm = np.zeros((n-1,n-1))
        ndm[:-1,:-1] = dm
        #
        
        for i in range(n-2):
            dicc = cluster_distance(c[i],cc,odm)
            ndm[-1,i] = dicc
            ndm[i,-1] = dicc        
        r.append(cc)
        #print ndm
        #break
        dm = ndm
        
    r.append(c[0]+c[1])
    return r

def exe(data):
    n,distance_matrix = readInfo(data)
    dm = np.array(distance_matrix)
    r = hierarchical_clustering(len(dm),dm)
    for rs in r:
        print ' '.join(map(str,rs))
    #Hierarchical_Clustering(n,distance_matrix)
    #test = [1,2,3,4,5]
    #test2= test[:3]+test[4:]
    #print test2
    
data = open("pattern","r")
exe(data)
