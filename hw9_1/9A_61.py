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

def print_trie(trie,index_pre):
    index_suff = index_pre+1
    for node in trie:
        if trie[node] == "$":
            continue
        print (str(index_pre)+"->"+str(index_suff)+":"+node)
        index_suff = print_trie(trie[node],index_suff)
    return index_suff

def exe(data):
    inputs = readInfo(data)
    trie = TrieConstruction(inputs)
    print trie
    print_trie(trie,0)
    
data = open("pattern","r")
exe(data)