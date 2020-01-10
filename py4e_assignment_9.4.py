fname=input ("Enter file:")
file=open (fname)
counts=dict()
names=list()

for line in file:
    words=line.split()
    if len(words)<3 or "From" not in words:continue
    name=words[1]
    names.append(name)

for name in names:
        counts[name] = counts.get(name,0)+1

mostword=None
mostcount=None
for name,count in counts.items():
    if mostcount is None or count>mostcount:
        mostword=name
        mostcount=count
print(mostword,mostcount)
    
