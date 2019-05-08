def readInfo(data):
    string = data.readline().strip("\n")
    patterns = data.readline().strip("\n").split(" ")
    return string,patterns

def consturct_secondString(input):
    pos = 0
    char_list = []
    count_dict = dict()

    for char in input:
        if char in count_dict:
            count_dict[char] = count_dict[char]+1
            char_list.append((char,count_dict[char],pos))   
        else:
            count_dict[char] = 1
            char_list.append((char,count_dict[char],pos))
        pos +=1
    return char_list

def BWMatching (firstCol,LastCol,Pattern,Last_to_first):
    top = 0
    bottom = len(LastCol)-1
    while top <= bottom:
        if len(Pattern) > 0:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            if symbol in LastCol[top:bottom+1]:
                topIndex = LastCol.find(symbol,top,bottom+1)
                bottomIndex = LastCol.rfind(symbol,top,bottom+1)
                top = Last_to_first[topIndex]
                bottom = Last_to_first[bottomIndex]
            else:
                return 0
        else:
            return bottom - top +1

def last_to_first_list_conver(last_col,first_col):
    pos_list = [0]*len(last_col)
    index = 0
    for char in last_col:
        pos_list[index] = first_col.index(char)
        index +=1
    return pos_list

def exe(data):
    string,patterns = readInfo(data)
    last_col = consturct_secondString(string)
    first_col = list(last_col)
    first_col.sort()
    last_to_first = last_to_first_list_conver(last_col,first_col)
    last_col_string = ''.join([i[0] for i in last_col])
    first_col_string = ''.join([i[0] for i in first_col])

    count_list = []
    for pattern in patterns:
        count = BWMatching (first_col_string,last_col_string,pattern,last_to_first)
        count_list.append(count)
    
    print ' '.join(map(str,count_list))
    
data = open("pattern","r")
exe(data)