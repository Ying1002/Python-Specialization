fname = input("Enter file name: ")
try:
    fh = open(fname)
    container=list()
    for line in fh:
        line=line.rstrip()
        line=line.upper()
        container.append(line)
    print (container[:5])
except: print ("file cannot be opened", fname)
