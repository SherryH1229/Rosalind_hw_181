def readInfo(data):
    string = data.readline().strip("\n")
    pos = int(data.readline().strip("\n"))
    return string,pos


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

def last_to_first(input,pos):
    last_col = consturct_secondString(input)
    first_col = list(last_col)
    first_col.sort()
    temp = last_col[pos]
    p = first_col.index(temp)
    return p

def exe(data):
    input,index = readInfo(data)
    print last_to_first(input,index)

data = open("pattern","r")
exe(data)
    