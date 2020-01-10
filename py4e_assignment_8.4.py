total=list()
fname=input ("Enter file name:")
try:
    file=open(fname)


    for line in file:
        line=line.rstrip()
        pieces=line.split()
        for word in pieces:
            if word in total:
                continue
            total.append(word)
    total.sort()
    print (total)
except:
    print ("This file "+fname+" cannot be opened")
    
