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
 

def computingFrequencies(text,k):
    freqArray = []
    for i in range (0,4**k):
        freqArray.append(0)
        
    for i in range (0,len(text)-k+1):
        pattern = text[i:i+k]
        j = patternToNum(pattern)
        freqArray[j] = freqArray[j]+1

    return freqArray

freqArray = computingFrequencies("TTTCACCGTCTTTGGATCGAGGCTTATAAATTTCAGGAGTTGCATGTGCAAAGCGCTGATGATTAGGCTGGTGACAACTCGTGGCGCCGAGCATCGTCGCTGCCTCGTAGGTCTGTGACCTAGCACACTCATAATTTCAGAGGACACTCACCTCTCCTTGAAAAACCTGAAGTTAGTGTCCTTGAGGGTGTGGGAACGCCGCCATCTACGCATAGCGCCCCTTAAGAGCGCAGGTACGTTGCAGGTGTCAGGCATTTGTCAGTATTCCTAAACTCACAGGTTTTTGTAGAACTGTTGATACTGCAGCATGTGCAGTCAGTGAGGGTGAATGAAAAACTCACCGAGGGCGCAAAGCTTTGAGTACCCCAAACCAACATTACCCCATAGGTTTCTAGGCTGTAACGTTGCAAAAACCGTGAGGTACTAGCTGAACATGCATGCTCTTTTGGCGGATCGGTGGATTCGGTCCCCTAATAAGCTGTAGGACCGGATACCCCTTGGAAAAGGGCGGGTTTCCCAACTTACTGACGGCATACGCAATTGTATCCGACTCACACTATCGAGTTAGTAACGTATGCCCGTCCTAAGTAGGACACCCGTCCGCTGCGGTACCTTGTAAGCTCTTTAGATTACATTGATCGGGCGGGCTTAACTATCCTAGACTTGGTGTCGATCAACGTCCTGCAATTCGTCTGCCAAGTATACGAGGAGATCTCTAGTGTTGCATCC",6)
freqArrayString = ' '.join(str(x) for x in freqArray)
print (freqArrayString)