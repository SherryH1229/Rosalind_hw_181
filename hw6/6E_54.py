def readInfo(data):
    str1 = data.readline().rstrip('\n')
    str2 = data.readline().rstrip('\n')
   
    return str1,str2

def reversCom(string):
    revString = string[::-1]
    comString = []
    for char in revString:
        if char == 'A':
            comString.append("T")
        elif char == 'T':
            comString.append("A")
        elif char == 'C':
            comString.append("G")
        else:
            comString.append("C")
    str_comString = ''.join(comString)
    return str_comString

def buildDict(string,k):
    kmerDict = dict()
    for i in range (len(string)-k+1):
        kmer = string[i:i+k]
        if kmer not in kmerDict:
            kmerDict[kmer] = [i]
        else:
            kmerDict[kmer].append(i)
    
    return kmerDict

def printPair(pos1,pos2):
    i  = 0
    while i < len(pos1):
        posLis1 = pos1[i]
        posLis2 = pos2[i]
        for position1 in posLis1:
            for position2 in posLis2:
                print (position1,position2)
        i+=1
    return 0

def getPosList(dict1,dict2):
    posList1 = []
    posList2 = []
    
    for key,value in dict1.iteritems():
        reversKey = reversCom(key)
        if key in dict2:
            posList1.append(dict1[key])
            posList2.append(dict2[key])
        
        if reversKey in dict2:
            posList1.append(dict1[key])
            posList2.append(dict2[reversCom(key)])
        
    return posList1,posList2

def exe(data,k):
    str1,str2 = readInfo(data)
    dict1 = buildDict(str1,k)
    dict2 = buildDict(str2,k)

    posList1,posList2 = getPosList(dict1,dict2)
    printPair(posList1,posList2)

data = open("pattern","r")
exe(data,15)