def hammingDist(str1,str2):
    if (len(str1)!=len(str2)):
        print("the lengths of two strings are not the same!")
        return 0
    dist = 0
    for i in range (0,len(str1)):
        if (str1[i]!=str2[i]):
            dist = dist + 1
    return dist


def apxPatternCount(string,pattern,d):
    count = 0
    for i in range (0,len(string)-len(pattern)+1):
        substring = string[i:(i+len(pattern))]
        distance = hammingDist(substring,pattern)
        if (distance<=d):
            count = count+1
    return count


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


def freqWordWithMismatch_withReverse(text,k,d):
    freqPatterns = []
    close = []
    freqArray = []
    for i in range (0,4**k):
        close.append(0)
        freqArray.append(0)
    for i in range (0,len(text)-k+1):
        neighborhood = neighbors(text[i:(i+k)],d)
        if isinstance(neighborhood, str):
            index = patternToNum(neighborhood)
            close[index] = 1  
        else:
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
            freqPatterns.append(reversCom(pattern))
    
    freqPatterns = set(freqPatterns)
    freqPatterns = list(freqPatterns)
    freqPatternsString = ' '.join(freqPatterns)
    return freqPatternsString

#test = freqWordWithMismatch_withReverse("ATA",3,1)
print (freqWordWithMismatch_withReverse("TCCTCGCCCTCCTCGCCCCGCTATACGCTATACCTCAAATTCCTCGCCCTCCTCGCCCAAACGTAGAAACGTAGAGCCTGTCCGCTATAAAACGTAGAAACGTAGAAACGTAGTCCTCGCCCAGCCTGTCAGCCTGTCAGCCTGTCCGCTATACGCTATAAGCCTGTCAAACGTAGAAACGTAGAGCCTGTCCCTCAAATAAACGTAGCGCTATAAGCCTGTCAAACGTAGTCCTCGCCCTCCTCGCCCTCCTCGCCCAGCCTGTCAGCCTGTCAAACGTAGAAACGTAGCGCTATACGCTATAAAACGTAGCCTCAAATCGCTATATCCTCGCCCCGCTATAAAACGTAGAAACGTAGTCCTCGCCCTCCTCGCCCCGCTATACCTCAAATAGCCTGTCAAACGTAGCGCTATACGCTATACGCTATATCCTCGCCCCGCTATATCCTCGCCCCCTCAAATCCTCAAATAGCCTGTCAAACGTAGCGCTATAAAACGTAGCGCTATACCTCAAATCGCTATACGCTATACCTCAAATAGCCTGTCCGCTATAAAACGTAGCCTCAAATTCCTCGCCCCGCTATAAGCCTGTCTCCTCGCCCCGCTATAAGCCTGTCCCTCAAATCCTCAAATCCTCAAATAGCCTGTCCCTCAAATTCCTCGCCCAGCCTGTCCGCTATACGCTATACGCTATACCTCAAATAAACGTAGCCTCAAATAAACGTAGCCTCAAATAGCCTGTCAGCCTGTCAAACGTAGCGCTATAAGCCTGTCTCCTCGCCCAAACGTAGCCTCAAATAAACGTAGTCCTCGCCCAAACGTAG",6,2))