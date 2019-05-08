def hammingDist(str1,str2):
    if (len(str1)!=len(str2)):
        print("the lengths of two strings are not the same!")
        return 0
    dist = 0
    for i in range (0,len(str1)):
        if (str1[i]!=str2[i]):
            dist = dist + 1
    return dist


def suffix(pattern):
    suffix = pattern[1:]
    return suffix
def firstSymbol(pattern):
    firstSymbol = pattern[0]
    return firstSymbol
def neighbors(pattern,d):
    nucleotide = "ACGT"
    if d == 0:
        return pattern
    
    if len(pattern)==1:
        return ["A","C","G","T"]
    
    neighborhood = []
    
    suffixNeighbors = neighbors(suffix(pattern),d)
    #print (suffixNeighbors)
    for string in suffixNeighbors:
        if (hammingDist(suffix(pattern),string) < d):
            for char in nucleotide:
                neighborString = char+string
                neighborhood.append(neighborString)    
        else:
            print (pattern, "pattern",string,"string")
            neighborString = firstSymbol(pattern)+string
            print (neighborString)
            neighborhood.append(neighborString)
    return neighborhood



result = neighbors("ACT",1)

for string in result:
    print (string)

    