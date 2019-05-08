def readInfo(data):
    info  = map(int,((data.read())[1:-1]).split())
    return info

def ChromosomeToCycle(chroms):
    Node = [0] * (len(chroms)*2+1)
    for j in range (len(chroms)):
        i = chroms[j]
        if i > 0:
            Node[2*(j+1)-1] = 2*i-1
            Node[2*(j+1)] = 2*i
        else:
            Node[2*(j+1)-1] = -2*i
            Node[2*(j+1)] = -2*i-1
    
    return "("+' '.join(map(str,Node[1:]))+")"

def exe(data):
    oriList = readInfo(data)
    print(ChromosomeToCycle(oriList))

data = open("pattern","r")
exe(data)