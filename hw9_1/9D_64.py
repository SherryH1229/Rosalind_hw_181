#------------extra functions-------------
count_dict = dict()
nodeList = []
def readInfo(data):
    strings = data.read().rstrip("/n")
    return strings+"$"

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
#-------------------9D---------------------
def print_trie(trie,index_pre):  
    index_suff = index_pre+1
    for node in trie:
        if trie[node] == "$":
            continue
        if type(trie[node]) == int:
            #print node
            if node[-1] == "$" and len(node) != 1:
                #print node[:-1]
                nodeList.append(node[:-1])
            continue
        #print node
        nodeList.append(node)
        index_suff = print_trie(trie[node],index_suff)
    return index_suff

def patternCount (text,pattern):
    count = 0
    length = 1+len(text)-len(pattern)
    for i in range (0,length):
        if text[i:(i+len(pattern))] == pattern:
            count = count+1
    return count

def find_longestRepeat(node_list,text):
    set_list = list(set(node_list))
    #print set_list
    maxL = 0
    for node in set_list:
        count = patternCount(text,node)
        if count >= 2:
            lenth = len(node)
            if lenth > maxL:
                possString = node
                maxL = lenth
    #print possString
    return possString

def exe(data):
    inputs = readInfo(data)
    suff_trie = suffixTrie_construct(inputs)
    t = build_suffixTree(suff_trie)
    print_trie(t,0)
    find_longestRepeat(nodeList,inputs)
    

data = open("pattern","r")
exe(data)