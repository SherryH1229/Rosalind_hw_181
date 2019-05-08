#-------------------extra func-----------------
def readInfo(data):
    strings = data.read().splitlines()

    return strings

def TrieConstruction(inputs):
    root = dict()
    for input in inputs:
        currentNode = root
        for i in input:
            if i in currentNode:
                currentNode = currentNode[i]
            else:
                currentNode[i] = {}
                currentNode = currentNode[i]
        currentNode["end"] = "$"
    return root
#------------------9B--------------------
def prefix_matching(text,trie):
    index = 0
    symbol = text[index]
    v = trie
    while True:
        if symbol in v:
            #print v
            index += 1
            v = v[symbol]
            if index < len(text):
                symbol = text[index]
        elif v == {'end': '$'}:
            return True
        else:
            return False

def exe(data):
    inputs = readInfo(data)
    text = inputs[0]
    strings = inputs[1:]
    trie = TrieConstruction(strings)
    list = map(str,[i for i in range (len(text))if (prefix_matching(text[i:],trie))])
    print ' '.join(list)
    
data = open("pattern","r")
exe(data)