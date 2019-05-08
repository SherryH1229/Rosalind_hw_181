def readInfo(data):
    strings = data.read().rstrip("/n")
    return strings+"$"

def compare_string(a,b):
    minlen = min(len(a),len(b))
    count = 0
    for i in range(minlen):
        if (a[i]!=b[i]):
            break
        count += 1
    return count

def commonString_score(str1,str2):
    com_length = min(len(str1),len(str2)):
    score = 0
    for i in range (com_length):
        if str1[i] == str2[i]:
            score+=1
        else:
            break
    return score

def insert_words(currentNode,j,i,suffix,text):
     #key = root.keys()
    if len(currentNode.keys()) > 0:
        first_Chars = [text[num[0]] for num in currentNode.keys()]
        for k in len(first_Chars):
            if first_Chars[k] == suffix[0]:
                key_pos = (currentNode.keys())[k]
                suff_label = [key_pos[0]:key_pos[1]]
                score = commonString_score(suffix,suff_lable)
                #when inputword is longer than the common string
                if score == len(label):
                    #recursive
                    insert_words(currentNode[key_pos],j+score,i,text[j+score:],text)
                    return
                else:
                    value = current_dict.pop(key)
                    child_dict = {(key[0]+count,key[1]):value}
                    current_dict[(key[0],key[0]+count)] = child_dict
                    child_dict[(j+count,len(text))] = i
    
    else:
        currentNode[i,len(text)] = len(text)
        print currentNode
    return 0

def modifiedSuffixConstruction(text):
    root = dict()
    currentNode = root
    for i in range (len(text)):
        insert_words(currentNode,i,i,text[i:],text)
    return root

def longest_repeat(text):
    def dfs(root,word):
        if (len(root.keys())>1) and (len(longests[-1]) < len(word)):
            # word is repreated and is larger than any longest's
            longests.append(word)

        for key, value in root.iteritems():
            if type(value) == dict:
                label = text[key[0]:key[1]]
                dfs(value,word+label)
        return
    longests = ['',]
    t = modifiedSuffixConstruction(text)
    dfs(t,'')
    return longests[-1]

def exe(data):
    inputs = readInfo(data)
    modifiedSuffixConstruction(inputs)
    
    #print longest_repeat(inputs)
    
data = open("pattern","r")
exe(data)