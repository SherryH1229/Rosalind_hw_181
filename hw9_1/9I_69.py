def readInfo(data):
    strings = data.read().splitlines()[0]
    return strings

def build_suffArray(inputs):
    suff_array = []
    for i in range (len(inputs)):
        suff_array.append((inputs[i:],i))
    suff_array.sort()

    index_list = [i[1] for i in suff_array]
    
    return index_list

def BW_construct(s):
    suffArray = build_suffArray(s)
    print suffArray
    info = []
    for i in suffArray:
        if i == 0:
            info.append("$")
        else:
            info.append(s[i-1])
    print ''.join(info)

def exe(data):
    inputs = readInfo(data)
    BW_construct(inputs)
    #suff_array = build_suffArray(inputs[0])
    

data = open("pattern","r")
exe(data)