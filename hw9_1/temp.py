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
    minIndex = 0
    maxIndex = len(text)-1
    #print suffArray
    while minIndex <= maxIndex:
        midIndex = int((minIndex+maxIndex)/2)
        suffix_of_text = text[suffArray[midIndex]:suffArray[midIndex]+len(Pattern)]
        #if suffix_of_text == Pattern:
            #print suffArray[midIndex]
    
        tempList = [Pattern,suffix_of_text]
        tempList.sort()
        
        if tempList[1] == Pattern:
            minIndex = midIndex+1
        else:
            maxIndex = midIndex-1
    
    #print minIndex
    first = minIndex
    maxIndex = len(text)-1
    #print minIndex
    minIndex = 0
    while minIndex <= maxIndex:
        midIndex = int((minIndex+maxIndex)/2)
        print minIndex
        suffix_of_text = text[suffArray[midIndex]-len(Pattern):suffArray[midIndex]]
        print suffix_of_text
        #print midIndex
        #print suffArray[midIndex]
        #if suffix_of_text == Pattern:
        #    print suffArray[midIndex]
        tempList = [Pattern,suffix_of_text]
        print tempList
        tempList.sort()
        if tempList[0] == Pattern:
            maxIndex = midIndex-1
        else:
            minIndex = midIndex+1

    last = maxIndex
    if first > last:
        return "Pattern not in the text"


        #if Pattern
    return (first,last)
    
def exe(data):
    inputs = readInfo(data)
    suff_array = build_suffArray(inputs[0])
    #print suff_array
    patternMatching_suffArray(inputs[0],inputs[1],suff_array)

data = open("pattern","r")
exe(data)