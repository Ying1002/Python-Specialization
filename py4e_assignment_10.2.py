fname=input ("Enter file:")
file=open (fname)
Int=list()
counts=dict()

for line in file:
    words=line.split()
    if len(words)<7 or "From" not in words:continue
    time=words[5]
    pieces=time.split(":")
    hour=pieces[0]
    Int.append(hour)
for hour in Int:
    counts[hour]=counts.get(hour,0)+1

for hour,count in sorted(counts.items()):
    print (hour,count)
    


    
