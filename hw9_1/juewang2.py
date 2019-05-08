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

def insert_suffix(current_dict,j,i,text):
    keys = current_dict.keys()
    first_letters = [text[k[0]] for k in keys]
   
    word = text[j:]

    if word[0] in first_letters:
        key = keys[first_letters.index(word[0])]
        label = text[key[0]:key[1]]
     
        count = compare_string(word,label)
        
        if count == len(label):
               
            insert_suffix(current_dict[key],j+count,i,text)
            return
                
        value = current_dict.pop(key)
        child_dict = {(key[0]+count,key[1]):value}
        current_dict[(key[0],key[0]+count)] = child_dict
        child_dict[(j+count,len(text))] = i
    else:   
        current_dict[j,len(text)] = i
        #print current_dict

def new_suffix_tree(text):
    root = dict()
    for i in range(len(text)):
        insert_suffix(root,i,i,text)
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
    #print new_suffix_tree(inputs)
    print longest_repeat(inputs)
    
data = open("pattern","r")
exe(data)