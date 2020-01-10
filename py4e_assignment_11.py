fname=input ("Enter file:")
file=open (fname)
numlist=list()
import re

for line in file:
    line=line.rstrip()
    stuff=re.findall("[0-9]+",line)
    if len(stuff)>=1:
        for num in stuff:
            Int=int(num)
            numlist.append(Int)
print("The sum for the sample data:",sum(numlist))
            
    

    


    
