#----------------Extra packages------------
import random
#----------------Extra functions------------
def stringCompByPath(string):
    outputString = []
    #print string[0]
    outputString.append(string[0])
    for i in range (1,len(string)):
        tempStr = string[i]
        outputString.append(tempStr[-1])
    return (''.join(outputString))

def getPairs (data):
    pairList = []
    for lines in data:
        pair = []
        info = lines.split("|")
        pair.append(info[0])
        pair.append(''.join(info[1].split()))
        pairList.append(pair)
    return pairList

def stringSpelledByGappedPatterns(GappedPatterns,k,d):
    patterns = getPairs(data)
    firstPatterns = [x[0] for x in patterns]
    secondPatterns = [x[1] for x in patterns]

    PrefixString = stringCompByPath(firstPatterns)
    SuffixString  = stringCompByPath(secondPatterns)
    
    #print PrefixString

    for i in range ((k+d+1),len(PrefixString)):
        if (PrefixString[i]) != (SuffixString[(i-k-d)]):
            return "there is No String Spelled By th Gapped Patterns"
    
    return PrefixString+SuffixString[len(SuffixString)-(k+d):]


data = open("pattern","r")
print(stringSpelledByGappedPatterns(data,30,100))
#print stringSpelledByGappedPatterns(data,4,2)

#GACCGAGCGCCGGA
#GACCGAGCGCCGGA

