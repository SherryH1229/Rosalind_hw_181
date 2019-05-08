
#-------------3B-------------------
patterns = open("pattern","r")
patternString = []
for line in patterns:
    patternString.append(line.splitlines())

def stringCompByPath(string):
    outputString = string[0]
    for i in range (1,len(string)):
        tempStr = (string[i])[0]
        outputString.append(tempStr[-1])
    print (''.join(outputString))
    
stringCompByPath(patternString)