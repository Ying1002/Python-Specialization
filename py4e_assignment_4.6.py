hrs= input ("Enter hours:")
rate= input ("Enter rate:")
h=float (hrs)
r=float (rate)
def computepay(h,r):
    if h<=40:
        return r*h
    else:
        return 40*r+1.5*r*(h-40)
    
print ("pay:",computepay(h,r))
