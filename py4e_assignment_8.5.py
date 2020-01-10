fname=input ("Enter file name:")
file=open(fname)
count=0
for line in file:
    line=line.rstrip()
    pieces=line.split()
    if len(pieces)<3 or pieces[0]!="From":continue
    print (pieces[1])
    count=count+1
print ("There were",count,"lines in the file with From as the first word")
