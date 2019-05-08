def readInfo(data):
    strings = data.read().splitlines()
    string = strings[0]
    patterns = strings[1:]
    return string,patterns

def build_suffArray(inputs):
    suff_array = []
    for i in range (len(inputs)):
        suff_array.append((inputs[i:],i))
    suff_array.sort()

    index_list = [i[1] for i in suff_array]
    return index_list

def BW_construct(s,k):
    suffArray = build_suffArray(s)
    info = []
    for i in suffArray:
        if i == 0:
            info.append("$")
        else:
            info.append(s[i-1])

    partial_suffarray = []
    for j in range (len(suffArray)):
        if suffArray[j]%k == 0:
            partial_suffarray.append((j,suffArray[j]))
    return ''.join(info),suffArray

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

def better_BWMatching (first_occur,LastCol,Pattern,suffArray):
    top = 0
    bottom = len(LastCol)-1
    while top <= bottom:
        if len(Pattern) > 0:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            top = first_occur[symbol]+count_symbol(symbol,top,LastCol)
            bottom = first_occur[symbol]+ count_symbol(symbol,bottom+1,LastCol)-1
        else:
            return [suffArray[i] for i in range(top,bottom+1)]
    
def exe(data,k):
    string,patterns = readInfo(data)
    bwt_stirng,partial_suffArray = BW_construct(string+"$",k)

    last_col = bwt_stirng
    first = list(last_col)
    first.sort()
    first_col = ''.join(first)
    first_occur = first_occur_constructor(first_col)

    pos_list = []
    for pattern in patterns:
        poss = better_BWMatching(first_occur,last_col,pattern,partial_suffArray)
        if poss != None:
            pos_list += poss
    
    print ' '.join(map(str,pos_list))
    

data = open("pattern","r")
exe(data,5)
    