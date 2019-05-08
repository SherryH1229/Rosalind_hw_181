def readInfo(data):
    strings = data.read().rstrip("/n")
    return strings

def build_suffArray(inputs):
    #print inputs
    suff_array = []
    for i in range (len(inputs)):
        suff_array.append((inputs[i:],i))
    suff_array.sort()

    index_list = [i[1] for i in suff_array]
    print ', '.join(map(str,index_list))
    
def exe(data):
    inputs = readInfo(data)
    build_suffArray(inputs)

data = open("pattern","r")
exe(data)