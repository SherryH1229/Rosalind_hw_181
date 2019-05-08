def readInfo(data):
    strings = data.read().splitlines()
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
    
def find_shortestNonshare(str1,str2,kmer_range):  
    for l in range (1,kmer_range):
        #bool = False
        for i in range (len(str1)-l):
            kmer = str1[i:i+l]
            #print kmer
            if kmer not in str2:
                print kmer
                break
            

def exe(data):
    inputs = readInfo(data)
    print find_shortestNonshare(inputs[0],inputs[1],10)

data = open("pattern","r")
exe(data)