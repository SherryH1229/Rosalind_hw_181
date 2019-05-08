def readInfo(data):
    strings = data.read().rstrip("/n")
    return strings+"$"

def commonString_score(str1,str2):
    com_length = min(len(str1),len(str2))
    score = 0
    for i in range (com_length):
        if str1[i] == str2[i]:
            score+=1
        else:
            break
    return score

def insert_suffix(current_dict,suff,i,text):
    keys = current_dict.keys()
    first_letters = [text[k[0]] for k in keys]
   

    if suff[0] in first_letters:
        key = keys[first_letters.index(suff[0])]
        label = text[key[0]:key[1]]
     
        count = commonString_score(suff,label)
        
        if count == len(label): 
            insert_suffix(current_dict[key],text[i+count:],i,text)
            return
                
        value = current_dict.pop(key)
        child_dict = {(key[0]+count,key[1]):value}
        current_dict[(key[0],key[0]+count)] = child_dict
        child_dict[(i+count,len(text))] = i
    else:   
        current_dict[i,len(text)] = i
        #print current_dict

def new_suffix_tree(text):
    root = dict()
    for i in range(len(text)):
        insert_suffix(root,text[i:],i,text)
        #break
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
    t = new_suffix_tree(text)
    dfs(t,'')
    return longests[-1]

def exe(data):
    inputs = readInfo(data)
    print longest_repeat(inputs)
    #print new_suffix_tree(inputs)
    #print longest_repeat(inputs)
    
data = open("pattern","r")
exe(data)