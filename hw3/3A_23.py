#-------------3A-------------------
def kmerComp(k,string):
    kmerList = []
    for i in range (len(string)-k+1):
        kmerList.append(string[i:i+k])
    
    kmerList.sort()
    #print(kmerList) 

    for m in kmerList:
        print (m)

kmerComp(5,"CAATCCAAC")



