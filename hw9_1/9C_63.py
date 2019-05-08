def readInfo(data):
    strings = data.read().rstrip("/n")
    return strings

def suffixTrie_construct(string):
    root = dict()
    for i in range (len(string)):
        suffix = string[i:]
        currentNode = root
        for suff in suffix:
            if suff == "$":
                currentNode["$"] = i
            elif suff in currentNode:
                currentNode = currentNode[suff]
            else:
                currentNode[suff] = {}
                currentNode = currentNode[suff]
    return root

def nonBranching_path(currNode,sub_suffTrie):
    while True:
        if len(sub_suffTrie.keys())==1:
            char = sub_suffTrie.keys()[0]
            currNode = currNode+char
            if char == "$":
                break
            sub_suffTrie = sub_suffTrie[char]
        else:
            return currNode,sub_suffTrie
    return currNode,sub_suffTrie[char]

def build_suffixTree(suffTrie):
    if type(suffTrie) == int:
        return suffTrie
    for node in suffTrie.keys():
        sub_suffTrie = suffTrie[node]
        currNode = node
        if type(sub_suffTrie) == int:
            outEdges = sub_suffTrie
        else:
            currNode,outEdges = nonBranching_path(currNode,sub_suffTrie)
        suffTrie.pop(node,None)
        suffTrie[currNode] = outEdges
        build_suffixTree(outEdges)
   
    return suffTrie

def print_trie(trie,index_pre):  
    index_suff = index_pre+1
    for node in trie:
        if trie[node] == "$":
            continue
        if type(trie[node]) == int:
            print node
            continue
        print node
        index_suff = print_trie(trie[node],index_suff)
    return index_suff

def exe(data):
    inputs = readInfo(data)
    suff_trie = suffixTrie_construct(inputs)
    t = build_suffixTree(suff_trie)
    s = print_trie(t,0)

data = open("pattern","r")
exe(data)