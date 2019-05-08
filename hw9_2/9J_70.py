def readInfo(data):
    strings = data.read().rstrip("\n")
    return strings

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

def inverse_BW_transformation(input):
    second_string = consturct_secondString(input)
    first_string = list(second_string)
    first_string.sort()
    out = []
    pos = 0
    while len(out) < len(input):
        pos = first_string[pos][2]
        out.append(first_string[pos][0])
   
    return ''.join(out)

def exe(data):
    input = readInfo(data)
    print inverse_BW_transformation(input)

data = open("pattern","r")
exe(data)