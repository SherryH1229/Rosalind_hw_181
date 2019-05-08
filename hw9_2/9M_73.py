def readInfo(data):
    string = data.readline().strip("\n")
    patterns = data.readline().strip("\n").split(" ")
    return string,patterns

def count_symbol (symbol,pos,lastcol):
    subString = lastcol[:pos]
    c = subString.count(symbol)
    return c

def first_occur_constructor(first_col):
   
    pos_dict = dict()
    for i in range (len(first_col)):
        if first_col[i] not in pos_dict:
            pos_dict[first_col[i]] = i
    return pos_dict

def better_BWMatching (first_occur,LastCol,Pattern):
    top = 0
    bottom = len(LastCol)-1
    while top <= bottom:
        if len(Pattern) > 0:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            top = first_occur[symbol]+count_symbol(symbol,top,LastCol)
            bottom = first_occur[symbol]+ count_symbol(symbol,bottom+1,LastCol)-1
        else:
            return bottom - top +1
    return 0

def exe(data):
    string,patterns = readInfo(data)
    last_col = string
    first = list(last_col)
    first.sort()
    first_col = ''.join(first)
    first_occur = first_occur_constructor(first_col)

    count_list = []
    for pattern in patterns:
        count = better_BWMatching(first_occur,last_col,pattern)
        count_list.append(count)
    
    print ' '.join(map(str,count_list))
    
    
data = open("pattern","r")
exe(data)