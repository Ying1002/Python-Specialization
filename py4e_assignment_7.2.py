fname=input ("Enter file name:")
fh=open(fname)
count=0
total=0
for line in fh:
    if "X-DSPAM-Confidence" in line:
        count=count+1
        pos=line.find(" ")
        num=float(line[(pos+1):(pos+7)])
        total=total+num
print("Average spam condfidence:",total/count)
    
    
