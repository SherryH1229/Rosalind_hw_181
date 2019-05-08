#1A
def patternCount (text,pattern):
    count = 0
    length = 1+len(text)-len(pattern)
    for i in range (0,length):
        if text[i:(i+len(pattern))] == pattern:
            count = count+1
    return count

#1B
def frequentWords (text,k):
    frequentPatterns = []
    count = []
    for i in range (0,len(text)-k):
        pattern = text[i:(i+k)]
        value = patternCount(text,pattern)
        count.append(value)
    
    maxCount = max(count)
    for i in range (0,len(text)-k):
        if count[i] == maxCount:
            frequentPatterns.append(text[i:(i+k)])
    frequentPatterns = set(frequentPatterns)
    frequentPatterns = list(frequentPatterns)
    return frequentPatterns

#1C
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

#1D
def matchString(pattern,string):
    revPattern = reversCom(pattern)
    testLength = len(pattern)
    posList = []
    for i in range (0,len(string)):
        testString = string[i:(i+testLength)]
        if testString == pattern:
            posList.append(i)
        elif testString == revPattern:
            posList.append(i)

    return(posList)

#1E
def betterClumpFinding(Genome,k,L,t):
    freqPatterns = []
    clump = []
    for i in range (0,4**k):
        clump.append(0)
    text = Genome[0:L]
    freqArray = computingFrequencies(text,k)
    for i in range (0,4**k-1):
        if freqArray[i] >= t:
            #print (i)
            clump[i] = 1
    for i in range (1,len(Genome)-L):
        firstPattern = Genome[i-1:i+k-1]
        index = patternToNum(firstPattern)
        freqArray[index] = freqArray[index]-1
        lastPattern = Genome[i+L-k:i+L]
        index = patternToNum(lastPattern)

        freqArray[index] = freqArray[index]+1
        if freqArray[index] >= t:
            clump[index] = 1
    
    for i in range (0,4**k-1):
        if clump[i] == 1:
            pattern  = numberToPattern(i,k)
            freqPatterns.append(pattern)
    
    freqPatternsString = ' '.join(freqPatterns)       
    return freqPatternsString

def clumpFinding(genome,k,L,t):
    freqPatterns = []
    clump = []
    for i in range (0,4**k):
        clump.append(0)
    for i in range (0,len(genome)-L):
        text = genome[i:i+L]
        #print (text)
        freqArray = computingFrequencies(text,k)
        for index in range (0,4**k-1):
            if freqArray[index] >=t:
                #print (index)
                clump[index] = 1
    for i in range (0,4**k-1):
        if (clump[i] == 1):
            pattern = numberToPattern(i,k)
            freqPatterns.append(pattern)
    freqPatternsString = ' '.join(freqPatterns)
    
    return freqPatternsString
        
#1F
def minSkew(string):
    skew = []
    value = 0
    for i in range (0,len(string)):
        skew.append(value)
        if (string[i] == "G"):
            value = value+1      
        elif (string[i] == "C"):
            value = value-1   
        else:
            continue
    minValue = min(skew)
    minList = []
    for j in range (0,len(skew)):
        if skew[j] == minValue:
            minList.append(j)
    return minList

#1G
def hammingDist(str1,str2):
    if (len(str1)!=len(str2)):
        print("the lengths of two strings are not the same!")
        return 0
    dist = 0
    for i in range (0,len(str1)):
        if (str1[i]!=str2[i]):
            dist = dist + 1
    return dist

#1H
def apxPatternMatch(pattern,string,d):
    posList = []
    for i in range (0,len(string)-len(pattern)+1):
        substring = string[i:(i+len(pattern))]
        distance = hammingDist(substring,pattern)
        if (distance<=d):
            posList.append(i)
    
    return (posList)

#1I
def apxPatternCount(string,pattern,d):
    count = 0
    for i in range (0,len(string)-len(pattern)+1):
        substring = string[i:(i+len(pattern))]
        distance = hammingDist(substring,pattern)
        if (distance<=d):
            count = count+1
    return count
def freqWordWithMismatch(text,k,d):
    freqPatterns = []
    close = []
    freqArray = []
    for i in range (0,4**k):
        close.append(0)
        freqArray.append(0)
    for i in range (0,len(text)-k):#caution
        neighborhood = neighbors(text[i:(i+k)],d)
        for pattern in neighborhood:
            index = patternToNum(pattern)
            close[index] = 1
    for i in range (0,4**k-1):
        if close[i] == 1:
            pattern = numberToPattern(i,k)
            freqArray[i] = apxPatternCount(text,pattern,d)
    maxCount = max(freqArray)
    
    for i in range (0,4**k-1):
        if freqArray[i] == maxCount:
            pattern = numberToPattern(i,k)
            freqPatterns.append(pattern)
        
    return freqPatterns

#1J
def freqWordWithMismatch_withReverse(text,k,d):
    freqPatterns = []
    close = []
    freqArray = []
    for i in range (0,4**k):
        close.append(0)
        freqArray.append(0)
    for i in range (0,len(text)-k):
        neighborhood = neighbors(text[i:(i+k)],d)
        for pattern in neighborhood:
            index = patternToNum(pattern)
            close[index] = 1
    for i in range (0,4**k-1):
        if close[i] == 1:
            pattern = numberToPattern(i,k)
            freqArray[i] = (apxPatternCount(text,pattern,d))+(apxPatternCount(text,reversCom(pattern),d))
    maxCount = max(freqArray)
    
    for i in range (0,4**k-1):
        if freqArray[i] == maxCount:
            pattern = numberToPattern(i,k)
            freqPatterns.append(pattern)
            freqPatternsString = ' '.join(freqPatterns)
        
    return freqPatternsString

#1K
def computingFrequencies(text,k):
    freqArray = []
    for i in range (0,4**k):
        freqArray.append(0)
        
    for i in range (0,len(text)-k+1):
        pattern = text[i:i+k]
        j = patternToNum(pattern)
        freqArray[j] = freqArray[j]+1
    return freqArray

#1L
def lastSymbol(pattern):
    lastSymbol = pattern[-1:]
    return lastSymbol
def prefix(pattern):
    prefix = pattern[0:-1]
    return prefix

def symbolToPattern(symbol):
    if symbol == 'A':
        value = 0 
    elif symbol == 'C':
        value = 1
    elif symbol == 'G':
        value = 2
    else:
        value = 3
    
    return value
def patternToNum(pattern):
    if not pattern:
        return 0
    symbol = lastSymbol(pattern)
    prefixChar = prefix(pattern)
    return 4*patternToNum(prefixChar)+symbolToPattern(symbol)
 
#1M
def numberToSymbol(index):
    if index == 0:
        symbol = "A"
    elif index == 1:
        symbol = "C"
    elif index == 2:
        symbol = "G"
    else:
        symbol = "T"
    return symbol
def quotient(index,num):
    quotient = int(index/num)
    return quotient
def remainder(index,num):
    quot = quotient(index,num)
    remainder = index-quot*num

    return remainder
def numberToPattern(index,k):    
    if k == 1:
        return numberToSymbol(index)
    prefixIndx = quotient(index,4)
    r = remainder(index,4)
    symbol = numberToSymbol(r)
    prefixPattern = numberToPattern(prefixIndx,k-1)
    
    return prefixPattern+symbol

#1N
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
    for string in suffixNeighbors:
        if (hammingDist(suffix(pattern),string) < d):
            for char in nucleotide:
                neighborString = char+string
                neighborhood.append(neighborString)    
        else:
            neighborString = firstSymbol(pattern)+string
            neighborhood.append(neighborString)
    return neighborhood

def haha:
    