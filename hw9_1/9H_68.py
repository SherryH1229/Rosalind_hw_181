def readInfo(data):
    strings = data.read().splitlines()
    return strings

def build_suffArray(inputs):
   
    suff_array = []
    for i in range (len(inputs)):
        suff_array.append((inputs[i:],i))
    suff_array.sort()

    index_list = [i[1] for i in suff_array]
    
    return index_list

def patternMatching_suffArray(text,Pattern,suffArray):
    posArray = []
    minIndex = 0
    maxIndex = len(text)-1
    #print suffArray
    while minIndex <= maxIndex:
        midIndex = int((minIndex+maxIndex)/2)
        suffix_of_text = text[suffArray[midIndex]:suffArray[midIndex]+len(Pattern)]
        
        tempList = [Pattern,suffix_of_text]
        tempList.sort()
        
        if tempList[1] == Pattern:
            minIndex = midIndex+1
        else:
            maxIndex = midIndex-1
        if suffix_of_text == Pattern:
            #first = minIndex
            posArray.append(suffArray[midIndex])
            #print suffArray[midIndex]
        #else:
            #print "pattern not in the text"

    first = minIndex

    maxIndex = len(text)-1
    #print suffArray
    while minIndex <= maxIndex:
        midIndex = int((minIndex+maxIndex)/2)
        if suffArray[midIndex] == len(text)-1:
            suffix_of_text = "$"
        else:
            suffix_of_text = text[suffArray[midIndex]:suffArray[midIndex]+len(Pattern)]
        
        tempList = [Pattern,suffix_of_text]
        #print tempList
        tempList.sort()
        
        if tempList[1] == Pattern:
            maxIndex = midIndex-1
        else:
            
            minIndex = midIndex+1
        if suffix_of_text == Pattern:
            posArray.append(suffArray[midIndex])
            #first = minIndex
            #print suffArray[midIndex]
        #else:
            #print "pattern not in the text"

    last = maxIndex 
    if first > last:
       return "Pattern not in the text"


        #if Pattern
    return posArray
    #return (first,last)
    
def exe(data):
    inputs = readInfo(data)
    suff_array = build_suffArray(inputs[0])
    #print suff_array
    totalOut = []
    strings = inputs[1:]
    for s in strings:
        out = patternMatching_suffArray(inputs[0],s,suff_array)
        totalOut+=out
    print ', '.join(map(str,totalOut))

data = open("pattern","r")
exe(data)