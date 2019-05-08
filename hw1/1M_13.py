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

print (numberToPattern(5733,7))